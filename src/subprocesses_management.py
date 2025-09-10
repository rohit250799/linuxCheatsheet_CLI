import subprocess

def search_command_using_man(user_query_input):
    result = subprocess.run(["man", "-k", user_query_input], capture_output=True, text=True)
    print(result.stdout)