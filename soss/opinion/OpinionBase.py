from abc import ABC, abstractmethod

class OpinionBase(ABC):

    @abstractmethod
    def new(self):
        raise NotImplementedError

    @abstractmethod
    def apply_to(self, people):
        raise NotImplementedError

    @abstractmethod
    def get_from(self, people):
        raise NotImplementedError

    @abstractmethod
    def create_counter_data(self):
        raise NotImplementedError

    @abstractmethod
    def counter_data_to_proportion(self, counter_data, size):
        raise NotImplementedError

    @abstractmethod
    def count_to(self, counter_data, people):
        raise NotImplementedError