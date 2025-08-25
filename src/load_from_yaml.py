import yaml

def import_data_from_yaml_file() -> str:
    try:
        with open('commands_list.yaml', 'r') as file:
            imported_yaml_data = yaml.load(file, Loader=yaml.FullLoader)

        return imported_yaml_data
    
    except FileNotFoundError:
        print(f"Error: {file} not found. Please ensure file: {file} exists")
        return
    
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return
    
def display_all_command_num() -> int | None:
    yaml_data = import_data_from_yaml_file()
    command_set = set()

    for command, details in yaml_data.items():
        if command not in command_set:
            command_set.add(command)
            description = details['description']
            examples = details['examples']
            category = details['category']

    print(f'The total number of unique commands is: {len(command_set)}')
    return

def display_all_command_categories_num() -> None:
    yaml_data = import_data_from_yaml_file()
    unique_command_categories = set()
    category_num = 0
    
    for command, details in yaml_data.items():
        categories = details['category']
        if categories not in unique_command_categories:
            unique_command_categories.add(categories)

        
    print(f'The total number of categories is: {len(unique_command_categories)}')
    return


def find_entered_command_in_imported_yaml_data(command_entered):
    pass    



