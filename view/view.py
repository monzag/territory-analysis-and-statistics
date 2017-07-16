def print_welcome_screen():
    '''
    Display start screen.
    '''

    print('''
    ####################################
    #                                  #
    #    Meet the regions of Poland    #
    #                                  #
    ####################################
    ''')


def print_menu():
    '''
    Display data in menu with proper number.
    '''

    tittle = 'Choose option: '
    options = ['List statistics', 'Display 3 cities with longest names',
               "Display county's name with the largest number of communities",
               'Display locations, that belong to more than one category', 'Advanced search', 'Find region']

    number = 1
    print(tittle)
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1


def get_input():
    '''
    Get input from user.

    Returns:
        user_input - string
    '''

    user_input = input('Your choice: ')

    return user_input


def print_list_of_object(list_of_object):
    '''
    Convert list of object to list of data object (list in lists).
    Display table with data.

    Args:
        list_of_object - list
    '''

    list_of_data_object = []
    for item in list_of_object:
        list_of_data_object.append([item.number, item.name, item.type])

    print_table(list_of_data_object)


def print_message(text):
    '''
    Display text.

    Args:
        text - string
    '''

    print('\n' + str(text) + '\n')


def error_message():
    '''
    Display error message
    '''

    print('\nBad choice. Try one more time!\n')


def exit_message():
    '''
    Display option '0' - exit program.
    '''

    print('{}. {}'.format(0, 'exit\n'))


def print_table(list_of_data):
    '''
    Display table with data from list_of_data.

    Args:
        list_of_data - list in lists
    '''

    for row in list_of_data:
        out_row = draw_out_row(list_of_data, row)
        print(out_row)
        middle_row = draw_data_row(list_of_data, row)
        print(middle_row)
    print(out_row)


def find_max_string(data, index):
    '''
    Find max length of data in column.

    Args:
        data - list of lists
        index - int

    Returns:
        length longest string - int
    '''

    longest_string = ''
    for row in data:
        if len(str(row[index])) > len(longest_string):
            longest_string = str(row[index])

    return len(longest_string)


def draw_data_row(data, row):
    '''
    Draw row with data (with proper width and format).

    Args:
        data - list of lists
        row - list

    Returns:
        row_data - string
    '''

    row_data = '|'
    addit = 2
    index = 0
    for item in row:
        max_string = find_max_string(data, index)
        cell_width = max_string + addit
        row_data = row_data + (str(item).center(cell_width, ' ')) + '|'
        index += 1

    return row_data


def draw_out_row(data, row):
    '''
    Draw out row (with proper width and format).

    Args:
        data - list of lists
        row - list

    Returns:
        out_row - string
    '''

    index = 0
    addit = 3
    out_row = ''
    for item in row:
        max_string = find_max_string(data, index)
        cell_width = max_string + addit
        out_row += '-' * cell_width
        index += 1

    return out_row


def get_pause():
    '''
    Input before os clear
    '''

    input('')


def end_screen():
    '''
    Display end screen
    '''

    print('''
    ####################################
    #                                  #
    #        Have a nice day! ;)       #
    #                                  #
    ####################################
    ''')


