import re

from load_from_yaml import import_data_from_yaml_file

def search_command_by_name(command_name_input: str) -> bool:
    yaml_data = import_data_from_yaml_file()

    for command in yaml_data:
        if command_name_input == command: 
            print('Command has been found in the cheatsheet!')
            return True

    print('Command not found in the cheatsheet!')
    return False

def change_command_data() -> bool:
    pass

def suggest_command(user_query_input: str) -> None:
    yaml_data: dict = import_data_from_yaml_file()
    suggestion_found = None

    for command, details in yaml_data.items():
        command_description = details['description']
        command_category = details['category']
        suggestion_found = re.findall(user_query_input, command_description)
        if suggestion_found: 
            print(f'A suggestion has been found: {command}')
            return
        
    print('A suggestion could not be found')    
    return suggestion_found