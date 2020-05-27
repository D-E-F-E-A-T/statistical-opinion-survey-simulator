import math
from .People import People, GENRE_MALE, GENRE_FEMALE
from .PopulationBase import PopulationBase
from .PopulationRandomBased import PopulationRandomBased
from ..sample import PopulationSample

class PopulationAgeRangeGenreBased(PopulationBase):
    def __init__(self, age_genre_data):
        def people_creator(genre, age_range):
            p = People(genre)
            p.age_range = age_range
            return p
        self.ages = []
        for age in age_genre_data:
            age_object = {
                "description": age["description"],
                "size_male": age["size_male"],
                "size_female": age["size_female"],
                "population_male": PopulationRandomBased(age["size_male"], people_creator, GENRE_MALE, age["description"]),
                "population_female": PopulationRandomBased(age["size_female"], people_creator, GENRE_FEMALE, age["description"])
            }
            self.ages.append(age_object)
    
    def count(self, counter_data, opinion):
        for age in self.ages:
            age["population_male"].count(counter_data, opinion)
            age["population_female"].count(counter_data, opinion)

    def get_population_size(self):
        num = 0
        for age in self.ages:
            num += age["population_male"].get_population_size()
            num += age["population_female"].get_population_size()
        return num

    def get_sample(self, size, *args):
        sample = PopulationSample()
        population_size = self.get_population_size()
        for age in self.ages:
            male_proportion = (age["size_male"] / population_size)
            male_size = round(size * male_proportion)
            female_proportion = (age["size_female"] / population_size)
            female_size = round(size * female_proportion)
            sample_male = age["population_male"].get_sample(male_size)
            sample_female = age["population_female"].get_sample(female_size)
            sample.append_other(sample_male)
            sample.append_other(sample_female)
        return sample