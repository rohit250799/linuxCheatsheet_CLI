import argparse

parser = argparse.ArgumentParser(prog='Linux CLI cheatsheet', description='display a linux command cheatsheet')
parser.add_argument("commands", help="display all the available linux commands available in the linux cheatsheet")
parser.add_argument("-v", "--verbose", action="store_true", help="increases output verbosity")
args = parser.parse_args()


def display_all_commands() -> str:
    commandsList = ['ls', 'cd', 'pwd', 'mkdir', 'rm']
    print('\n'.join(commandsList))

def display_all_commands_verbose() -> None:
    commands_map = {
        'ls': 'Used to list files and directories in the current directory',
        'cd': 'Used to change directory',
        'pwd': 'Used to print the present working directory',
        'mkdir': 'Used to create a directory from the terminal',
        'rm': 'Used to remove a file'
    }
    
    for command in commands_map.items():
        print(command)
    
    return

if args.commands and not args.verbose:
    display_all_commands()    

if args.verbose:
    display_all_commands_verbose()
    print("Since verbosity was been turned on")
