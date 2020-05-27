#
# Testing vote generator rule
#
from soss.attributes import VoteGeneratorRule
from soss.population import PopulationAgeRangeGenreBased
from soss.confianceinterval import ProportionConservator, ProportionOptimist

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
vote_generator.counter_data_to_proportion(data)

print("Population: ", pop.get_population_size())
print(data)

sample = pop.get_sample(2401)
print("Sample: ", sample.get_sample_size())
data = vote_generator.create_counter_data()
sample.count(data, vote_generator)
vote_generator.counter_data_to_proportion(data)
print(data)

ic1 = ProportionConservator()
ic2 = ProportionOptimist(data)
e1 = ic1.get_error_to(sample, 0.95)
e2 = ic2.get_error_to(sample, 0.95)

print("Conservator confiance interval:")
print(e1)
print("Optimist confiance interval:")
print(e2)