from subprocesses_management import display_current_ip_address
import ipaddress

def find_v4_or_v6(network_id: str) -> str:
    if isinstance(ipaddress.ip_network(network_id), ipaddress.IPv4Network): return 'v4'
    elif isinstance(ipaddress.ip_network(network_id), ipaddress.IPv6Network): return 'v6'
    else: raise ValueError('An incorrect value has been ised') 

def find_network_id_class(network_id) -> str:
    network_id_first_octet_list:list = []

    for c in network_id:
        if c != '.':
            network_id_first_octet_list.append(c)
        else: break

    network_id_first_octet = int(''.join(map(str, network_id_first_octet_list)))

    if network_id_first_octet >= 0 and network_id_first_octet <= 126: return 'A'
    elif network_id_first_octet >= 128 and network_id_first_octet <= 191: return 'B'
    elif network_id_first_octet >= 192 and network_id_first_octet <= 233: return 'C'
    else: return 'Invalid id'

def calculate_free_bits_for_network(input_subnet_mask: int) -> int:
    print(f'The entered subnet mask is: {input_subnet_mask}')
    return 32 - input_subnet_mask

# def calculate_total_hosts_for_each_subnet(subnet_number: int, free_bits: int = calculate_free_bits_for_network()):
#     total_addresses = 2 ** free_bits
#     hosts_in_each_subnet = total_addresses / subnet_number

#     return hosts_in_each_subnet

def calculate_all_new_network_ids():
    pass



def find_nearest_subnet_number(ipaddress, smask_value):
    #current_ip_address = display_current_ip_address()
    print(f'The provided default subnet mask is: {smask_value} and the current ip address is: {ipaddress}')
    return
    #return 'The subnet number is: 10'