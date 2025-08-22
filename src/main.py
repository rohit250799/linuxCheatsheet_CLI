import argparse
import subprocess

parser = argparse.ArgumentParser(prog='Linux CLI cheatsheet', description='display a linux command cheatsheet')
parser.add_argument("commands", default=argparse.SUPPRESS, help="display all the available linux commands available in the linux cheatsheet")
parser.add_argument("-v", "--verbose", action="store_true", help="increases output verbosity")
parser.add_argument("-cdes","--commandDescription", help="describe the particular command provided as an argument")
parser.add_argument('-ge','--getExample', help="Get an example of how the command works")
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

def display_command_example(command_input: str) -> None: #now only working for ls command, others to be added soon
    if not command_input or command_input not in commands_map:
        print('Command input invalid')
        return
    
    if command_input == 'cd':
        pass 
    
    commandOutput = subprocess.run([command_input], capture_output=True, text=True)
    print(commandOutput.stdout)
    return

if args.commands and not args.verbose and not args.commandDescription and not args.getExample:
    display_all_commands()    

if args.verbose:
    display_all_commands_verbose()
    print("Since verbosity was been turned on")

if args.commandDescription:
    display_command_description(args.commandDescription)
    print('Description text displayed in the above line')

if args.getExample:
    display_command_example(args.getExample)
    print('The inplemented output has been shown above')