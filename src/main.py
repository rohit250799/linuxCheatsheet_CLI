import argparse
import sys

from load_from_yaml import display_all_command_categories_num, display_all_command_num, display_all_available_commands_in_cheatsheet, display_all_available_categories_in_cheatsheet
from search_appropriate_commands import search_command_by_name, search_for_commands
from subprocesses_management import search_command_using_man, display_current_ip_address, display_current_ip_v6_address
from network_management import find_network_id_class, calculate_new_subnet_mask, find_v4_or_v6, print_usable_hosts

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
network_command_subparsers = parser_networking.add_subparsers(dest='network_commands', help='Subcommands for the network command')

ip_address_parser = network_command_subparsers.add_parser('ipaddress', help='Display the current ip address of the user')
ip_address_parser.add_argument('-v', '--version', default=4, type=int, choices=[4, 6], help='Stores the version if ip address', dest='version')

subnet_calculate_parser = network_command_subparsers.add_parser('subnet', help='Calculate subnet based on user input')
subnet_calculate_parser.add_argument('-nid', '--networkid', help='stores the network id provided as input', dest='networkId')
subnet_calculate_parser.add_argument('-smask', '--subnetmask',     
                               choices=['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'], 
                               help='stores the subnet mask as input', dest='smaskValue')
subnet_calculate_parser.add_argument('-snum', '--subnetnumber', type=int, help='stores the number of subnets that are to be created', dest='newSubnetNum')

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

if args.myCommand == 'categories':
    display_all_command_categories_num()
    if args.allCategories:
        print('The abvailable categories are: \n')
        display_all_available_categories_in_cheatsheet()
    print('\n Required data is available above')    

if args.myCommand == 'suggestions':
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

if args.myCommand == 'network':
    current_ipv6_address = display_current_ip_v6_address()
    current_ip_address = display_current_ip_address()

    if args.network_commands == 'ipaddress':

        if args.version == 6 and find_v4_or_v6(current_ipv6_address) == 'v6': print(f'The current ipv6 address is: {current_ipv6_address}')
        else: 
            print(f'The current ipv4 address is: {current_ip_address}')
            print(f'The current ip address class is: {find_network_id_class(current_ip_address)}')

    elif args.network_commands == 'subnet':
        print('Successfully entered the subnet code block')
        if args.networkId and args.smaskValue and args.newSubnetNum:
            print(f'The network type is: {find_v4_or_v6(args.networkId)}')
            print(f'The smask value is: {args.smaskValue}')
            print(f'The new subnet number is: {args.newSubnetNum}')

            new_network_id = args.networkId + '/' + args.smaskValue

            new_subnet_data = calculate_new_subnet_mask(new_network_id, args.newSubnetNum)
            print(new_subnet_data)

            print(f'The usable hosts are: {print_usable_hosts(args.networkId, args.smaskValue)}')
            sys.exit(0) 
        else:
            print('Incomplete data is provided')
            sys.exit(1)

else: 
    print('The program will end!')
    sys.exit(1)











