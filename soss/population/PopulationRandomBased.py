from .PopulationBase import PopulationBase

class PopulationRandomBased(PopulationBase):
    def __init__(self, size, people_creator, *args):
        self.size = size
        self.peoples = []
        for _ in range(0, self.size):
            self.peoples.append(people_creator(*args))
            
    def count(self, counter_data, opinion):
        for people in self.peoples:
            opinion.count_to(counter_data, people)