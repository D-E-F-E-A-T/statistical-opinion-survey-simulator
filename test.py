#
# Testing vote generator rule
#
from soss.opinion import VoteGeneratorRule
from soss.population import PopulationAgeRangeGenreBased

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

data = vote_generator.create_counter_data()
pop.count(data, vote_generator)

print(data)

print(pop.get_population_size())

#print(vote_generator.get_from(p))