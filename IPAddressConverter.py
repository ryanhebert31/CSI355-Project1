# Ryan Hebert & Ben K
# IP Calculator 
# Docs consulted: https://docs.python.org/3/library/ipaddress.html 

from ipaddress import AddressValueError, IPv4Address, ip_network

def main():
    ip = str(input("Enter IP Address: "))
    prefix = int(input("Enter Prefix Length: "))
    ipWithPrefix = ip + "/" + str(prefix)
    
    try:
        net = ip_network(ipWithPrefix, strict = False)
    except AddressValueError:
        print("ERROR: Not a valid IP address")
        return

    hosts = list(net.hosts())
    
    print(f"Subnet ID: \t\t {net.network_address}")
    print(f"First Host: \t\t {hosts[0]}")
    print(f'Broadcast Address: \t {net.broadcast_address}')
    print(f'Last Host: \t\t {hosts[len(hosts) - 1]}')
    print(f'Subnet Mask: \t\t {net.netmask}')

main()