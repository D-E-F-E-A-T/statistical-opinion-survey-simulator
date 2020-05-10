from soss.opinion import DoenceState
from soss.population import PopulationRandomBased, People, GENRE_UNKNOWN

diabetes_state = DoenceState("Diabetes", 0.4, 0.55)

def create_people():
    p = People(GENRE_UNKNOWN)
    diabetes_state.apply_to(p)
    return p

population = PopulationRandomBased(1500000, create_people)

diabetes_census = diabetes_state.create_counter_data()
population.count(diabetes_census, diabetes_state)
diabetes_state.counter_data_to_proportion(diabetes_census, population.get_population_size())
print("Census with 1.500.000 peoples")
print(diabetes_census)

sample = population.get_sample(2401)
diabetes_sample = diabetes_state.create_counter_data()
sample.count(diabetes_sample, diabetes_state)
diabetes_state.counter_data_to_proportion(diabetes_sample, sample.get_sample_size())
print("Survey with 2.401 peoples")
print(diabetes_sample)