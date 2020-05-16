import math
import random
from .OpinionBase import OpinionBase

class DoenceState(OpinionBase):
    def __init__(self, doence_name, has_doence_probability, know_has_doence_probability):
        self.doence_name = doence_name
        self.has_doence_probability = has_doence_probability
        self.know_has_doence_probability = know_has_doence_probability

    def new(self):
        prob_has = random.random()
        if prob_has < self.has_doence_probability:
            prob_known = random.random()
            known = prob_known < self.know_has_doence_probability
            return {
                "has": True,
                "know": known
            }
        return {
            "has": False,
            "know": False
        }

    def apply_to(self, people):
        if not hasattr(people, 'doences'):
            people.doences = {}
        people.doences[self.doence_name] = self.new()

    def get_from(self, people):
        try:
            return people.doences[self.doence_name]
        except KeyError:
            self.apply_to(people)
            return people.doences[self.doence_name]
    
    def create_counter_data(self):
        states = [0, 0]
        return states
    
    def counter_data_to_proportion(self, counter_data, size):
        size_has = counter_data[0]
        counter_data[0] /= size
        counter_data[1] /= size_has

    def count_to(self, counter_data, people):
        state = self.get_from(people)
        if state["has"]:
            counter_data[0] += 1
        if state["know"]:
            counter_data[1] += 1