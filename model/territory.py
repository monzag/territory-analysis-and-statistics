import os


class Territory:
    '''This is class representing Territory'''

    list_of_territory = []

    def __init__(self, name, types):
        self.name = name
        self.type = types

    @classmethod
    def load_data_from_file(cls):
        '''
        Check file path - if exist: get list of territory, else: raise File not Found Error. 

        Returns:
            list_of_territory - list (class variable)
        '''

        file_name = 'malopolska.csv'
        file_path = os.getcwd() + '/data/' + file_name
        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            cls.list_of_territory = cls.get_list_of_territory(file_path)

        return cls.list_of_territory

    @classmethod
    def get_list_of_territory(cls, file_path):
        '''
        Read data from file and convert it to list of lists.

        Args:
            file_path

        Returns:
            list_of_territory - list (class variable)
        '''

        with open(file_path, 'r') as csvfile:
            read_data = csvfile.readlines()[1:]
            splitted_rows = [line.replace('\n', '').split('|') for line in read_data]

            for row in splitted_rows:
                splitted_data_inside_row = [string.split('\t') for string in row]
                cls.list_of_territory += splitted_data_inside_row

        return cls.list_of_territory


