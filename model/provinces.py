import os
from model.territory import Territory
from model.county import County


class Province(Territory):
    '''This is class representing province - inherit from Territory'''

    def __init__(self, name, types, number):
        self.list_of_county = []
        self.number_of_province = number
        super().__init__(name, types)

    @classmethod
    def get_province(cls):
        '''
        Create new object Province. As attribute - proper data from list_of_territory.
        '''

        for row in cls.list_of_territory:
            if row[1] == '':
                return cls(row[4], row[5], row[0])

    def add_county(self):
        '''
        Create list_of_county built of County objects. Except Vallue Error when data isn't integer.
        '''

        first_index_county = 0
        for row in Territory.list_of_territory:
            try:
                index_county = int(row[1])
                if index_county != first_index_county and self.number_of_province == row[0]:
                    county = County(row[4], row[5], index_county)
                    self.list_of_county.append(county)
                    first_index_county = index_county
            except ValueError:
                continue



