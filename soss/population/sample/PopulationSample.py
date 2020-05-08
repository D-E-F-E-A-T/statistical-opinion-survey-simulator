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

    # implements methods (as confiance interval) and count here