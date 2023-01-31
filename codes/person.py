class Person:
    def __init__(self, name, weight, hunger, energy):
        self.name = name
        self.weight = weight
        self.hunger = hunger
        self.energy = energy

    def rest(self):
        self.energy = self.energy+1
        self.hunger = self.hunger-1

    def run(self, miles):
        # For every mile, the person will lose/gain two units
        change = miles*2
        if self.energy-change >= 0 or self.hunger+change <= 100:
            self.energy = self.energy-change
            self.hunger = self.hunger+change
            return True
        return False