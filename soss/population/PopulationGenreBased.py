import math
from .People import GENRE_MALE, GENRE_FEMALE

class PopulationGenreBased:
    def __init__(self, size, male_proportion, people_creator):
        self.size = size
        self.male_proportion = male_proportion
        self.size_male = math.ceil(self.size * male_proportion)
        self.size_female = self.size - self.size_male
        self.males = []
        self.females = []
        for _ in range(0, self.size_male):
            self.males.append(people_creator(GENRE_MALE))
        for _ in range(0, self.size_female):
            self.females.append(people_creator(GENRE_FEMALE))