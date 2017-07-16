import sys
import os
from collections import Counter

from model.territory import Territory
from model.provinces import Province
from model.county import County
from model.community import Community

from view import view


def get_data_from_file():
    '''
    Load data from file, create object Province.
    Add county to Province attribute list.
    Add community to County attribute list.
    Add location to Community attribute list.
    '''

    Territory.load_data_from_file()

    province = Province.get_province()
    province.add_county()

    for county in province.list_of_county:
        county.add_community()
        for community in county.list_of_community:
            community.add_location()

    return province


def run_app():
    '''
    Get data from file, display welcome screen, show menu, user chose option and start proper action.
    '''

    province = get_data_from_file()
    view.print_welcome_screen()

    start = True
    while start:
        view.get_pause()
        os.system('clear')
        view.print_menu()
        view.exit_message()
        user_choice = view.get_input()
        get_action(user_choice, province)


def get_action(user_choice, *args):
    '''
    Check that user input is in dictionary's keys and if yes, start proper function (value of dictionary). 
    If not print error message. When user chose 0, exit program.

    Args:
        user_choice - string
    '''

    action = {'1': get_statistic_list, '2': get_three_max_city, '3': get_county_with_max_communities, 
              '4': get_locations_with_more_category, '5': get_advanced_search, '6': find_region}

    if user_choice in action:
        action[user_choice](*args)

    elif user_choice == '0':
        close_program()

    else:
        view.error_message()


def get_statistic_list(*args):
    '''
    Get dictionary with statistic, convert it to sorted list and display table.
    '''

    dict_of_statistic = count_statistic()
    convert_to_list = dict_of_statistic.items()
    list_of_statistic = sorted(convert_to_list, reverse=True)
    view.print_table(list_of_statistic)


def count_statistic():
    '''
    Count data in list_of_territory on index 5 (type territory).

    Returns:
        dict_of_statistic - dictionary
    '''

    index_type = 5
    dict_of_statistic = Counter()
    for row in Territory.list_of_territory:
        types = row[index_type]
        dict_of_statistic[types] += 1

    return dict_of_statistic


def get_three_max_city(*args):
    '''
    Get list city, sorted it by length and descending and convert to list in lists (necessary to print_table).
    Display table with three city (or less if list is smaller)
    '''

    amount_max_city = 3
    list_city = get_list_city()
    sorted_list_city = sorted(list_city, key=len, reverse=True)
    sorted_list_in_lists = [[item] for item in sorted_list_city]
    if len(sorted_list_city) > amount_max_city:
        view.print_table(sorted_list_in_lists[:3])

    else:
        view.print_table(sorted_list_in_lists)


def get_list_city():
    '''
    Find city in list_of_territory (position 3) and add it to list_city.

    Returns:
        list_city - list
    '''

    index_rgmi = 3
    number_city = '4'
    index_name_city = 4
    list_city = []
    for row in Territory.list_of_territory:
        if row[index_rgmi] == number_city:
            list_city.append(row[index_name_city])

    return list_city


def get_county_with_max_communities(province):
    '''
    Find county with the longest list of community. Show county's name.

    Args:
        province - obj
    '''

    max_list_of_community = []
    for county in province.list_of_county:
        if len(county.list_of_community) > len(max_list_of_community):
            max_list_of_community = county.list_of_community
            max_county = county.name

    text = "county's name with the largest number of communities: " + str(max_county) + '\n'
    view.print_message(text)


def get_locations_with_more_category(province):
    '''
    Find list_of_location (attribute Community object) longer that 1.
    Display locations with more than one category.

    Args:
        province - obj
    '''

    for county in province.list_of_county:
        for community in county.list_of_community:
            if len(community.list_of_locations) > 1:
                view.print_list_of_object(community.list_of_locations)


def get_advanced_search(*args):
    '''
    Get input from user and check that input occur in list_of_territory in position 4 (name).
    Display results in table.
    '''

    list_of_search_result = []
    index_name_city = 4
    index_type = 5

    user_choice = view.get_input()
    for row in Territory.list_of_territory:
        if user_choice.lower() in row[index_name_city].lower():
            list_of_search_result.append([row[index_name_city], row[index_type]])

    check_empty_list(list_of_search_result)


def check_empty_list(list_of_search_result):
    '''
    Check list: if is empty, show text about not finding, else - display table with data. 

    Args:
        list_of_search_result - list
    '''

    if len(list_of_search_result) < 1:
        view.print_message('Not found')
    else:
        view.print_table(list_of_search_result)


def find_region(province):
    '''
    Show list of regions, chose one and find subregions.

    Args:
        province - object
    '''

    view.print_message(province.name)
    view.print_list_of_object(province.list_of_county)
    county = find_community(province)
    find_location(county)


def find_community(province):
    '''
    Find communities by county (chose by user).

    Args:
        province - object

    Returns:
        county - obj
    '''
    bad_answer = True
    while bad_answer:
        user_choice = view.get_input()
        if user_choice.isdigit():
            for county in province.list_of_county:
                if int(user_choice) == county.number:
                    view.print_message(county.name)
                    bad_answer = False
                    return county

        view.error_message()


def find_location(county):
    '''
    Find locations by community (chose by user).

    Args:
        county - object

    Returns:

    '''

    bad_answer = True
    while bad_answer:
        view.print_list_of_object(county.list_of_community)
        user_choice = view.get_input()
        if user_choice.isdigit():
            for community in county.list_of_community:
                if int(user_choice) == community.number:
                    view.print_message(community.name)
                    view.print_list_of_object(community.list_of_locations)
                    bad_answer = False
                    return bad_answer

        view.error_message()


def close_program():
    '''
    Display end screen and close program.
    '''

    view.end_screen()
    sys.exit()








