from model.territory import Territory
from model.location import Location


class Community(Territory):
    '''This is class representing community - inherit from Territory'''

    def __init__(self, name, types, number):
        super().__init__(name, types)
        self.number = number
        self.list_of_locations = []

    def add_location(self):
        '''
        Create list_of_locations built of Location objects. Except Vallue Error when data isn't integer.
        '''

        option = [4, 5]
        amount = 1
        for row in Territory.list_of_territory:
            try:
                if self.name == row[4] and int(row[3]) in option:
                    location = Location(row[4], row[5], amount)
                    self.list_of_locations.append(location)
                    amount += 1

            except ValueError:
                continue
