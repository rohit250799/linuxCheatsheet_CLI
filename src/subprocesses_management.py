import subprocess

def search_command_using_man(user_query_input) -> None:
    result = subprocess.run(["man", "-k", user_query_input], capture_output=True, text=True)
    print(result.stdout)

def display_current_ip_address():
    all_ip_address: str = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
    wifi_ipv4_address = all_ip_address.stdout.split()
    return wifi_ipv4_address[0]

def display_current_ip_v6_address():
    all_ip_address: str = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
    wifi_ipv6_address = all_ip_address.stdout.split()
    return wifi_ipv6_address[4]