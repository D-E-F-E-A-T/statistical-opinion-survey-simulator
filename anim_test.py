import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from soss.opinion import VoteGeneratorRule
from soss.population import PopulationAgeRangeGenreBased
from soss.population.sample.ic import ProportionConservator, ProportionOptimist

vote_generator = VoteGeneratorRule([0.2992, 0.2156, 0.1526, 0.1303, 0.1097, 0.0799, 0.0127])
pop = PopulationAgeRangeGenreBased([
    {
        "description": "16 a 24",
        "size_male": 27196,
        "size_female": 26914
    },
    {
        "description": "25 a 34",
        "size_male": 28400,
        "size_female": 29417
    },
    {
        "description": "35 a 44",
        "size_male": 24142,
        "size_female": 26513
    },
    {
        "description": "45 a 59",
        "size_male": 25570,
        "size_female": 28788
    },
    {
        "description": "60+",
        "size_male": 14689,
        "size_female": 18573
    }
])

data_census = vote_generator.create_counter_data()
pop.count(data_census, vote_generator)
vote_generator.counter_data_to_proportion(data_census, pop.get_population_size())

num_interacoes = 0

fig, ax = plt.subplots()

x = range(0, len(data_census))
y_initial = []
for i in range(0, len(x)):
    if i % 2 == 0:
        y_initial.append(0)
    else:
        y_initial.append(0.5)
ax.plot(x, data_census, linewidth=1, color="blue", label="Votação com a população total")
line, = ax.plot(x, y_initial, linewidth=1, color="green", label="Pesquisa com 2.401 pessoas")
line_top_error, = ax.plot(x, y_initial, linewidth=1, color="red", label="Margem de erro")
line_bottom_error, = ax.plot(x, y_initial, linewidth=1, color="red")

xlabels = []
for i in range(0, len(x)):
    xlabels.append(f"Candidato {i + 1}")

ax.set_xticks(x)
ax.set_xticklabels(xlabels, rotation=20, ha='right')
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
ax.set_title("Simulação de eleições e pesquisas eleitorais\n com confiabilidade de 95% e erro percentual\n de 2 pontos para mais ou para menos", wrap=True, pad=10)
ax.legend()

ax.set_xlabel("Pesquisa 0", labelpad=20)

error_text = ax.annotate("Erro Máximo: ", xy=(0, 0))

fig.tight_layout()

def new_sampling():
    sample = pop.get_sample(2401)
    data_sample = vote_generator.create_counter_data()
    sample.count(data_sample, vote_generator)
    vote_generator.counter_data_to_proportion(data_sample, sample.get_sample_size())
    ic1 = ProportionConservator()
    e = ic1.get_error_to(sample, 0.95)
    data_upper = []
    data_lower = []
    for i in data_sample:
        data_lower.append(i - e)
        data_upper.append(i + e)

    # TODO: implements this as confiance interval methods
    def largest_error(a, b):
        if len(a) != len(b):
            raise AssertionError("lists must be same size")
        max_error = 0
        for i in range(0, len(a)):
            error = abs(a[i] - b[i])
            if error > max_error:
                max_error = error
        return max_error

    return data_sample, data_upper, data_lower, largest_error(data_sample, data_census)

def init():  # only required for blitting to give a clean slate.
    sample, upper, lower, _ = new_sampling()
    line_top_error.set_ydata(upper)
    line_bottom_error.set_ydata(lower)
    line.set_ydata(sample)
    return line,

def animate(i):
    global num_interacoes
    print(num_interacoes)
    num_interacoes += 1
    ax.set_xlabel(f"Pesquisa {num_interacoes}", labelpad=20)
    sample, upper, lower, max_error = new_sampling()
    error_text.set_text("Erro Máximo: {:,.2%}".format(max_error))
    line_top_error.set_ydata(upper)
    line_bottom_error.set_ydata(lower)
    line.set_ydata(sample)
    fig.tight_layout()
    return line, ax

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=200, blit=False, save_count=200)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
from matplotlib.animation import ImageMagickWriter
writer = ImageMagickWriter(fps=4, metadata=dict(artist='Me'), bitrate=1800)
ani.save("movie.gif", writer=writer)

#plt.show()
