import argparse
import subprocess

from load_from_yaml import display_all_command_categories_num, display_all_command_num, display_all_available_commands_in_cheatsheet, display_all_available_categories_in_cheatsheet

parser = argparse.ArgumentParser(prog='Linux CLI cheatsheet', description='display a linux command cheatsheet')
subparsers = parser.add_subparsers(dest='myCommand', required=True)

parser_commands = subparsers.add_parser('commands', help='Required to display commands')
parser_commands.add_argument('-a', '--all', help='Display all the commands in the cheatsheet, with their description', dest='allCommands')

parser_categories = subparsers.add_parser('categories', help='Required to display command categories')
parser_categories.add_argument('-a', '--all', help='Display all the commands categories in the cheatsheet', dest='allCategories')

args = parser.parse_args()    

if args.myCommand == 'commands':
    display_all_command_num()
    if args.allCommands:
        print('The available commands are: \n')
        display_all_available_commands_in_cheatsheet()
    print('\n Required data is available above')

elif args.myCommand == 'categories':
    display_all_command_categories_num()
    if args.allCategories:
        print('The abvailable categories are: \n')
        display_all_available_categories_in_cheatsheet()
    print('\n Required data is available above')    
