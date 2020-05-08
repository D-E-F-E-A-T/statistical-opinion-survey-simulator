import random
from .PopulationBase import PopulationBase
from .sample import PopulationSample

class PopulationRandomBased(PopulationBase):
    def __init__(self, size, people_creator, *args):
        self.size = size
        self.peoples = []
        for _ in range(0, self.size):
            self.peoples.append(people_creator(*args))
            
    def count(self, counter_data, opinion):
        for people in self.peoples:
            opinion.count_to(counter_data, people)

    def get_population_size(self):
        return len(self.peoples)

    def get_sample(self, size, *args):
        sample = PopulationSample()
        if size > self.size:
            raise AssertionError("the sample size is larger than the population size")
        computed = []
        for _ in range(0, size):
            num = random.randint(0, self.size - 1)
            while num in computed:
                num = random.randint(0, self.size - 1)
            computed.append(num)
            sample.append(self.peoples[num])
        return sample