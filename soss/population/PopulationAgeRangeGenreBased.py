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

    def get_population_size(self):
        num = 0
        for age in self.ages:
            num += age["population_male"].get_population_size()
            num += age["population_female"].get_population_size()
        return num