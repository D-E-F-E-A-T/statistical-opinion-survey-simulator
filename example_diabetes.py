# Import used modules
from soss.opinion import DoenceState
from soss.population import PopulationRandomBased, People, GENRE_UNKNOWN
from soss.population.sample.ic import ProportionConservator, ProportionOptimist

# create a new doence state for diabetes, with a 
# probability of 0.4 (40%) for the people has diabetes
# and a probability of 0.55 (55%) for the peoples with
# diabetes known if has the doence
diabetes_state = DoenceState("Diabetes", 0.4, 0.55)

# creates a function for create peoples for this experiment
def create_people():
    # the genre not interfer in this example, because
    # we use an random population
    p = People(GENRE_UNKNOWN)
    # apply a new diabetes state to this people
    diabetes_state.apply_to(p)
    # and return this
    return p

# create a new population with 1500000 peoples
population = PopulationRandomBased(1500000, create_people)

# create a new counter data for an census with 1500000 peoples
diabetes_census = diabetes_state.create_counter_data()
# count the information in the peoples of the population
population.count(diabetes_census, diabetes_state)
# transform the census data to proportion
diabetes_state.counter_data_to_proportion(diabetes_census, population.get_population_size())
# show the information
print("Census with 1.500.000 peoples")
print(diabetes_census)

# create a new sample with 2401 peoples
sample = population.get_sample(2401)
# create a new counter data for the survey
diabetes_sample = diabetes_state.create_counter_data()
# count the information in the people of the sample
sample.count(diabetes_sample, diabetes_state)
# transform the data to proportion
diabetes_state.counter_data_to_proportion(diabetes_sample, sample.get_sample_size())
# show the information
print("Survey with 2.401 peoples")
print(diabetes_sample)

# confiance interval error
print("confiance interval with 95% of confiability")
print("conservator confiance interval for the proportion")
ic1 = ProportionConservator()
print("error is +\\-", ic1.get_error_to(sample, 0.95))
ic2 = ProportionOptimist(diabetes_sample)
print("optimist confiance interval for the proportion")
print("error is +\\-", ic2.get_error_to(sample, 0.95))

# Observation:
# 
# The optimist confiance interval for the proportion
# has two values because this takes into account the 
# proportion, then the value is not the same for two
# different proportions