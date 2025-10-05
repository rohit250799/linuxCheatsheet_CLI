import yaml, os

def import_data_from_yaml_file() -> dict | None:
    filename = os.path.join(os.path.dirname(__file__), "commands_list.yaml")
    try:
        with open(filename, "r") as file:
            imported_yaml_data = yaml.load(file, Loader=yaml.FullLoader)
        return imported_yaml_data
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please ensure file exists.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None
    
def display_all_command_num() -> int | None:
    yaml_data = import_data_from_yaml_file()
    command_set = set()

    for command, details in yaml_data.items():
        if command not in command_set:
            command_set.add(command)

    print(f'The total number of unique commands is: {len(command_set)}')
    return

def display_all_available_commands_in_cheatsheet() -> None:
    yaml_data = import_data_from_yaml_file()
    commands_name_set = set()

    for command, details in yaml_data.items():
        if command not in commands_name_set:
            description = details['description']
            command_and_description = (command, description)
            commands_name_set.add(command_and_description)

    for command_name, command_description in commands_name_set:
        print(f'{command_name} - {command_description}')

    return

def display_all_command_categories_num() -> None:
    yaml_data = import_data_from_yaml_file()
    unique_command_categories = set()
    
    for command, details in yaml_data.items():
        categories = details['category']
        if categories not in unique_command_categories:
            unique_command_categories.add(categories)

        
    print(f'The total number of categories is: {len(unique_command_categories)}')
    return

def display_all_available_categories_in_cheatsheet() -> None:
    yaml_data = import_data_from_yaml_file()
    categories_name_set = set()

    for category, details in yaml_data.items():
        category_name = details['category']
        categories_name_set.add(category_name)

    for category in categories_name_set:
        print(f'{category} \n')

    return



