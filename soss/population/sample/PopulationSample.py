import math
import scipy.stats

class PopulationSample:
    def __init__(self):
        self.peoples = []
    
    def append(self, people):
        self.peoples.append(people)

    def append_other(self, other_sample):
        for people in other_sample.peoples:
            self.append(people)

    def get_sample_size(self):
        return len(self.peoples)

    def count(self, counter_data, opinion):
        for people in self.peoples:
            opinion.count_to(counter_data, people)

    def get_error_conservator_ic(self):
        z = abs(scipy.stats.norm(0, 1).ppf(0.05 / 2))
        e = z / math.sqrt(4 * self.get_sample_size())
        return e

    def get_error_optimist_ic(self, proportion):
        size = self.get_sample_size()
        z = abs(scipy.stats.norm(0, 1).ppf(0.05 / 2))
        if type(proportion) == list:
            result = []
            for num in proportion:
                error = z * math.sqrt(num * (1 - num) / size)
                result.append(error)
            return result
        return z * math.sqrt(proportion * (1 - proportion) / size)

    # implements methods (as confiance interval) and count here