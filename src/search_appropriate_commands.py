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
    command_suggestions = []
    user_query_input_words_list = user_query_input.split()
    all_commands_description_list = []
    all_commands_categories_list = []


    for command, details in yaml_data.items():
        command_description: str = details['description'].lower()
        command_category: str = details['category']
        all_commands_description_list.append(command_description)
        all_commands_categories_list.append(command_category)
        # suggestion_found = re.findall(user_query_input.lower(), command_description) or re.findall(user_query_input, command_category) or re.findall(user_query_input, command)
        # if suggestion_found: command_suggestions.append(command) 

    for query_word in user_query_input_words_list:
        for single_command_description in all_commands_description_list:
            if query_word in single_command_description:
                print(f'The current single command description is: {single_command_description}') 
                command_to_display = all_commands_description_list.index(single_command_description)
                command_suggestions.append(command_to_display)
        # if query_word in all_commands_categories_list or query_word in all_commands_description_list: 
        #     command_to_display = all_commands_description_list(command_description)
        #     command_suggestions.append(command_to_display) 
            
        
    if command_suggestions: 
        print(f'Suggestions have been found: {command_suggestions}')
        print(f'{all_commands_description_list} is the all commands description list')
        return
    
    print('A suggestion could not be found')
    print(f'{user_query_input_words_list} is user query input words list')
    print(f'{all_commands_description_list} is all commands description list')    
    return suggestion_found