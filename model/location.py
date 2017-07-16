from model.territory import Territory


class Location(Territory):
    '''This is class representing location - inherit from Territory'''

    def __init__(self, name, types, number):
        super().__init__(name, types)
        self.number = number


