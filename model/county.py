from model.territory import Territory
from model.community import Community


class County(Territory):
    '''This is class representing county - inherit from Territory'''

    def __init__(self, name, types, number):
        super().__init__(name, types)
        self.number = number
        self.list_of_community = []

    def add_community(self):
        '''
        Create list_of_community built of Community objects. Except Vallue Error when data isn't integer.
        '''

        first_index_community = 0
        for row in Territory.list_of_territory:
            try:
                index_community = int(row[2])
                if index_community != first_index_community and self.number == int(row[1]):
                    community = Community(row[4], row[5], index_community)
                    self.list_of_community.append(community)
                    first_index_community = index_community
            except ValueError:
                continue
