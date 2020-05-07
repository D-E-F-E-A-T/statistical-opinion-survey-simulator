import math
import random
from .OpinionBase import OpinionBase

class VoteGeneratorRule(OpinionBase):
    def __init__(self, probabilities):
        self.probabilities = probabilities
        self.candidates = len(self.probabilities)
        self.rule = []
        accumulative = 0
        for i in range(0, self.candidates):
            num = math.floor(self.probabilities[i] * 100)
            self.rule.append(num + accumulative)
            accumulative += num
        
    def new(self):
        random_vote = random.randint(0, 100)
        for i in range(0, self.candidates):
            if random_vote <= self.rule[i]:
                return i
        return 0

    def apply_to(self, people):
        people.vote = self.new()

    def get_from(self, people):
        try:
            return people.vote
        except AttributeError:
            self.apply_to(people)
            return people.vote