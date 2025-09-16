import argparse
import sys

from load_from_yaml import display_all_command_categories_num, display_all_command_num, display_all_available_commands_in_cheatsheet, display_all_available_categories_in_cheatsheet
from search_appropriate_commands import search_command_by_name, search_for_commands
from subprocesses_management import search_command_using_man, display_current_ip_address, display_current_ip_v6_address
from network_management import find_nearest_subnet_number

parser = argparse.ArgumentParser(prog='Linux CLI cheatsheet', description='display a linux command cheatsheet')
subparsers = parser.add_subparsers(dest='myCommand', required=True)

parser_commands = subparsers.add_parser('commands', help='Required to display commands')
parser_commands.add_argument('-a', '--all', help='Display all the commands in the cheatsheet, with their description', dest='allCommands')
parser_commands.add_argument('--search', help='Search if the entered command exists in the cheatsheet', dest='searchCommandByName')

parser_categories = subparsers.add_parser('categories', help='Required to display command categories')
parser_categories.add_argument('-a', '--all', help='Display all the commands categories in the cheatsheet', dest='allCategories')

parser_suggestions = subparsers.add_parser('suggestions', help='Suggest commands based on the input')
parser_suggestions.add_argument('s', help='Display suggestions in brief')

parser_networking = subparsers.add_parser('network', help='Required to perform networking tasks')
parser_networking.add_argument('ipaddress', help='Display the current IPv4 address of the user')
parser_networking.add_argument('-v6', '--ipv6', action='store_true', help='DIsplay the current IPv6 address of the user', dest='ipaddressv6')

parser_networking.add_argument('subnetcalculate', action='store_true', help='Calculate the subnet for the provided value')
parser_networking.add_argument('-smask', '--subnetmask', help='stores the subnet mask as input', dest='smaskValue')

args = parser.parse_args()    

if args.myCommand == 'commands':
    display_all_command_num()
    if args.allCommands:
        print('The available commands are: \n')
        display_all_available_commands_in_cheatsheet()

    
    elif args.searchCommandByName:
        command_to_be_searched = args.searchCommandByName
        command_existence = search_command_by_name(command_to_be_searched)
    print(f'\n {command_existence}')

elif args.myCommand == 'categories':
    display_all_command_categories_num()
    if args.allCategories:
        print('The abvailable categories are: \n')
        display_all_available_categories_in_cheatsheet()
    print('\n Required data is available above')    

elif args.myCommand == 'suggestions':
    searching_result = search_for_commands(user_query_input=args.s)
    if searching_result: 
        print(searching_result)
        sys.exit(0) 
    else: 
        print(f'No suggestions have been found for your query: {args.s} \n')
        customer_continuation_input = int(input("Press 0 if you want to exit and 1 if you want to search for the command online: "))
        if customer_continuation_input == 1:
            search_command_using_man(args.s)
            print('All the suggested commands are displayed above')
        else:
            print('You have exit the command line!')
            sys.exit(0)

elif args.myCommand == 'network':
    current_ipv6_address = display_current_ip_v6_address()
    current_ip_address = display_current_ip_address()
    if args.ipaddress and args.ipaddressv6: 
        print(f'The current ipv6 address (inetv6) is: {current_ipv6_address}')
        sys.exit(0)
    else:
        print(f'The current ipv4 address (inet) is: {current_ip_address}')
        if args.subnetcalculate:
            print(find_nearest_subnet_number())
            if args.smaskValue:
                print(f'The subnet value is: {args.smaskValue}')
        sys.exit(0)

