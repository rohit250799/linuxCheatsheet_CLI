import argparse
import subprocess

from load_from_yaml import display_all_command_categories_num, display_all_command_num, display_all_available_commands_in_cheatsheet, display_all_available_categories_in_cheatsheet
from search_appropriate_commands import search_command_by_name, search_for_commands

parser = argparse.ArgumentParser(prog='Linux CLI cheatsheet', description='display a linux command cheatsheet')
subparsers = parser.add_subparsers(dest='myCommand', required=True)

parser_commands = subparsers.add_parser('commands', help='Required to display commands')
parser_commands.add_argument('-a', '--all', help='Display all the commands in the cheatsheet, with their description', dest='allCommands')
parser_commands.add_argument('--search', help='Search if the entered command exists in the cheatsheet', dest='searchCommandByName')

parser_categories = subparsers.add_parser('categories', help='Required to display command categories')
parser_categories.add_argument('-a', '--all', help='Display all the commands categories in the cheatsheet', dest='allCategories')

parser_suggestions = subparsers.add_parser('suggestions', help='Suggest commands based on the input')
parser_suggestions.add_argument('s', help='Display suggestions in brief')

args = parser.parse_args()    

if args.myCommand == 'commands':
    display_all_command_num()
    if args.allCommands:
        print('The available commands are: \n')
        display_all_available_commands_in_cheatsheet()

    
    elif args.searchCommandByName:
        command_to_be_searched = args.searchCommandByName
        search_command_by_name(command_to_be_searched)
    print('\n Required data is available above')

elif args.myCommand == 'categories':
    display_all_command_categories_num()
    if args.allCategories:
        print('The abvailable categories are: \n')
        display_all_available_categories_in_cheatsheet()
    print('\n Required data is available above')    

elif args.myCommand == 'suggestions':
    searching_result = search_for_commands(user_query_input=args.s)
    print(searching_result) if searching_result else print(f'No suggestions have been found for your query: {args.s}')
    print('\n The required data has been displayed above')

