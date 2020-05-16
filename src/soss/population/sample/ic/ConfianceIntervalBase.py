from abc import ABC, abstractmethod

class ConfianceIntervalBase(ABC):
    @abstractmethod
    def get_error_to(self, sample, confiability):
        raise NotImplementedError