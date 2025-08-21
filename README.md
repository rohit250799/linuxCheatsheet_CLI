# linuxCheatsheet_CLI
a Linux command cheatsheet CLI tool in Python

Currently, the cheatsheet will focus on 5 commands, which are also the most common ones:

1. ls

2. cd

3. pwd

4. mkdir

5. rm 

As the project progresses, new commands will be appended to the cheatsheet CLI iteratively. 


How to use this from the terminal:

1. on running: python3 main.py commands from the terminal, a simple list of all the commands in the cheatsheet should be shown
2. on running: python3 main.py commands --verbose or -v from the terminal, a list of all the commands in the cheatsheet is 
to be shown with more details (like help text) 
3. on runnung: python3 main.py commands -cdes mkdir, the command description is printed out in the terminal (if command is present in the cheetsheet),
else an unrecognized arguments message is printed out. In this context, 'mkdir' is the command input by the user. You can replace it with any other linux commands to test.
4. on running: python3 main.py commands -h, the user can get a generalised description about the CLI tool - like how to use it and in which order to put down different
arguments.  


