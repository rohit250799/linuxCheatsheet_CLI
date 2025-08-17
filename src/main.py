import argparse

parser = argparse.ArgumentParser(prog='Linux CLI cheatsheet', description='display a linux command cheatsheet')
parser.add_argument("commands", default=argparse.SUPPRESS, help="display all the available linux commands available in the linux cheatsheet")
parser.add_argument("-v", "--verbose", action="store_true", help="increases output verbosity")
parser.add_argument("commandDescription", help="describe the particular command provided as an argument")
parser.add_argument("commandInput", help="take the command as input, to describe it")
args = parser.parse_args()

commands_map = {
    'ls': 'Used to list files and directories in the current directory',
    'cd': 'Used to change directory',
    'pwd': 'Used to print the present working directory',
    'mkdir': 'Used to create a directory from the terminal',
    'rm': 'Used to remove a file'
}

def display_all_commands() -> str | None:
    commandsList = commands_map.keys()
    print('\n'.join(commandsList))
    return

def display_command_description(command_input: str) -> None:
    if not command_input or command_input not in commands_map:
        print('Command input invalid')
        return
    commandOutput = commands_map[command_input]
    print(commandOutput)
    return
    

def display_all_commands_verbose() -> None:
    
    for command in commands_map.items():
        print(command)
    
    return

if args.commands and not args.verbose:
    display_all_commands()    

if args.verbose:
    display_all_commands_verbose()
    print("Since verbosity was been turned on")

if args.commandDescription and args.commandInput:
    if args.commands: display_command_description(command_input=args.commandInput)
    else: SystemExit.code(2)