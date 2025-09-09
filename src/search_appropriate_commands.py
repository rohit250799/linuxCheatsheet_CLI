import re

from collections import defaultdict
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

def create_commands_and_description_dict(yaml_data: dict = import_data_from_yaml_file()) -> dict:
    commands_and_description_dict = {}
    for command, details in yaml_data.items():
        command_description: str = details['description'].lower()
        commands_and_description_dict[command] = command_description
    
    return commands_and_description_dict

def initialize_inverted_index():
    commands_and_description_dict = create_commands_and_description_dict()

    #building inverted index
    inverted_index = defaultdict(list)

    for command_name, command_description in commands_and_description_dict.items():
        words = command_description.lower().split()
        for word in set(words):
            inverted_index[word].append(command_name)

    return inverted_index

def search_for_commands(user_query_input: str):
    query_words = user_query_input.lower().split()
    results = None
    inverted_index = initialize_inverted_index()

    for word in query_words:
        if word in inverted_index:
            if results is None: results = set(inverted_index[word])
            else: results &= set(inverted_index[word])
        else: return []

    return list(results) if results else []