from abc import ABC, abstractmethod

class PopulationBase(ABC):
    @abstractmethod
    def count(self, counter_data, opinion):
        raise NotImplementedError

    @abstractmethod
    def get_population_size(self):
        raise NotImplementedError