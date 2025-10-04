from subprocesses_management import display_current_ip_address
import ipaddress

#for subnet mapping (hosts are keys and mapped to [subnets and subnet mask in list format])
subnet_mapping_dict = {
    65536: [1, 16],
    32768: [2, 17],
    16384: [4, 18],
    8192: [8, 19],
    4096: [16, 20],
    2048: [32, 21],
    1024: [64, 22],
    512: [128, 23],
    256: [256, 24],
    128: [512, 25],
    64: [1024, 26],
    32: [2048, 27],
    16: [4096, 28],
    8: [8192, 29],
    4: [16384, 30],
    2: [32768, 31],
    1: [65536, 32]
}

def find_v4_or_v6(network_id: str = display_current_ip_address()) -> str:
    if not network_id: return 'Invalid network id'
    if isinstance(ipaddress.ip_network(network_id), ipaddress.IPv4Network): return 'v4'
    elif isinstance(ipaddress.ip_network(network_id), ipaddress.IPv6Network): return 'v6'
    else: raise ValueError('An incorrect value has been used') 

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

def calculate_new_subnet_mask(network_id: str, new_subnet_number: int):
    cidr_notation = network_id.split('/')
    original_subnet_mask = cidr_notation[1]
    
    free_bits = 32 - int(original_subnet_mask)

    total_addresses_in_network = 2 ** free_bits

    hosts_per_subnet: int = total_addresses_in_network / new_subnet_number

    if hosts_per_subnet in subnet_mapping_dict:
        subnet_column = subnet_mapping_dict.get(hosts_per_subnet) 
        new_subnet, new_subnet_mask = subnet_column
        print(f'The new subnet is: {new_subnet}')
        print(f'The new subnet mask is: {new_subnet_mask}')
        print(f'Total addresses per subnet is: {hosts_per_subnet}')
        print(f'Usable addresses per subnet: {hosts_per_subnet - 2}')
        return new_subnet, new_subnet_mask 
    else: 
        print('No matching values have been found')
        return ''
    
def print_usable_hosts(network_id: str, smask: str) -> list:
    normalized_addr = ".".join(str(int(part)) for part in network_id.split("."))
    original_network = ipaddress.ip_network(f"{normalized_addr}/{smask}", strict=False)
    print(f"The original network is: {original_network}")

    smask = int(smask)
    new_prefix = original_network.prefixlen + (smask - 1).bit_length()
    if new_prefix >= 33:
        raise ValueError("Too many subnets requested!")

    print(f"The new subnet mask is: /{new_prefix}")

    new_subnets = list(original_network.subnets(new_prefix=new_prefix))
    print(f"Total subnets created: {len(new_subnets)}")

    # Printing details for each subnet
    for i, subnet in enumerate(new_subnets, 1):
        hosts = list(subnet.hosts())
        print(f"\nSubnet {i}: {subnet}")
        print(f"  Network ID: {subnet.network_address}")
        print(f"  Broadcast: {subnet.broadcast_address}")
        print(f"  Total addresses: {subnet.num_addresses}")
        print(f"  Usable hosts: {hosts if hosts else 'None'}")



def find_nearest_subnet_number(ipaddress, smask_value):
    #current_ip_address = display_current_ip_address()
    print(f'The provided default subnet mask is: {smask_value} and the current ip address is: {ipaddress}')
    return
    #return 'The subnet number is: 10'