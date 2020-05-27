import math
import scipy.stats
from .ConfianceIntervalBase import ConfianceIntervalBase

class ProportionOptimist(ConfianceIntervalBase):
    def __init__(self, proportion):
        self.proportion = proportion

    def get_error_to(self, sample, confiability):
        prob = (1 - confiability) / 2
        z = abs(scipy.stats.norm(0, 1).ppf(prob))
        size = sample.get_sample_size()
        if type(self.proportion) == list:
            result = []
            for num in self.proportion:
                error = z * math.sqrt(num * (1 - num) / size)
                result.append(error)
            return result
        return z * math.sqrt(self.proportion * (1 - self.proportion) / size)