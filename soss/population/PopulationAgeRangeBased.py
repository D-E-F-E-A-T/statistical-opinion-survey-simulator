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