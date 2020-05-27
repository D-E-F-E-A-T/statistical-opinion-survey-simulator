import math
import scipy.stats
from .ConfianceIntervalBase import ConfianceIntervalBase

class ProportionConservator(ConfianceIntervalBase):
    def get_error_to(self, sample, confiability):
        prob = (1 - confiability) / 2
        z = abs(scipy.stats.norm(0, 1).ppf(prob))
        error = z / math.sqrt(4 * sample.get_sample_size())
        return error

    @staticmethod
    def get_sample_size(confiability, error):
        prob = (1 - confiability) / 2
        z = abs(scipy.stats.norm(0, 1).ppf(prob))
        n = (z / error)**2 / 4
        return math.ceil(n)