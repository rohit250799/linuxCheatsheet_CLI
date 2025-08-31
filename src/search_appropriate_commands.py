from load_from_yaml import import_data_from_yaml_file

def search_command_by_name(command_name_input: str) -> bool:
    yaml_data = import_data_from_yaml_file()

    for command in yaml_data:
        if command_name_input == command: 
            print('Command has been found in the cheatsheet!')
            return True

    print('Command not found in the cheatsheet!')
    return False
