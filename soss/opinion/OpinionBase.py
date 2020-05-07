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