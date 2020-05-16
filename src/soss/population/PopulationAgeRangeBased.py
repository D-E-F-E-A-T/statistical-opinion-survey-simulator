from .PopulationBase import PopulationBase

class PopulationAgeRangeBased(PopulationBase):
    def __init__(self, ages, subpopulation_creator, people_creator, *args):
        self.ages = []
        for age_description in ages:
            age_data = {
                "description": age_description["description"],
                "population": subpopulation_creator(people_creator, age_description["size"], *args),
                "size": age_description["size"]
            }
            self.ages.append(age_data)

    def count(self, counter_data, opinion):
        for age in self.ages:
            age["population"].count(counter_data, opinion)

    def get_population_size(self):
        num = 0
        for age in self.ages:
            num += age["population"].get_population_size()
        return num