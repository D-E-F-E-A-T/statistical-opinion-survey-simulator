from .People import People, GENRE_MALE, GENRE_FEMALE
from .PopulationBase import PopulationBase
from .PopulationRandomBased import PopulationRandomBased

class PopulationAgeRangeGenreBased(PopulationBase):
    def __init__(self, age_genre_data):
        def people_creator(genre):
            return People(genre)
        self.ages = []
        for age in age_genre_data:
            age_object = {
                "description": age["description"],
                "size_male": age["size_male"],
                "size_female": age["size_female"],
                "population_male": PopulationRandomBased(age["size_male"], people_creator, GENRE_MALE),
                "population_female": PopulationRandomBased(age["size_female"], people_creator, GENRE_FEMALE)
            }
            self.ages.append(age_object)
    
    def count(self, counter_data, opinion):
        for age in self.ages:
            age["population_male"].count(counter_data, opinion)
            age["population_female"].count(counter_data, opinion)