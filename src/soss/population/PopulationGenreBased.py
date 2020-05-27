import math
from .People import GENRE_MALE, GENRE_FEMALE
from .PopulationBase import PopulationBase

class PopulationGenreBased(PopulationBase):
    def __init__(self, size, male_proportion, subpopulation_creator, people_creator, *args):
        self.size = size
        self.male_proportion = male_proportion
        self.size_male = math.ceil(self.size * male_proportion)
        self.size_female = self.size - self.size_male
        self.males = subpopulation_creator(people_creator, self.size_male, GENRE_MALE, *args)
        self.females = subpopulation_creator(people_creator, self.size_female, GENRE_FEMALE, *args)
    
    def count(self, counter_data, opinion):
        self.males.count(counter_data, opinion)
        self.females.count(counter_data, opinion)

    def get_population_size(self):
        return self.males.get_population_size() + self.females.get_population_size()

    # TODO: def get_sample(self, size, *args):