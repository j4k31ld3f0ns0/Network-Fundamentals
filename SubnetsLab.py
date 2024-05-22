import ipaddress

ipInterface = ipaddress.ip_interface('192.168.5.0/2')
print(f"the subnet mask for a two bit subnet is 11000000.00000000.00000000.00000000")
print(f"2 bit value {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface('192.168.5.0/13') 
print('the subnet mask for a 13 bit subnet is 11111111.11111000.00000000.000000000')
print(f"the 13 bit value is {ipInterface.netmask}")

print('the IP address is 137.195.5.56/21 Find the following information')
ipInterface=ipaddress.ip_interface('137.195.5.56/21')
ipNetwork = ipInterface.network
print(f'The network address is {ipNetwork.network_address}') 
print(f'The network address is {ipNetwork.broadcast_address}') 
print(f"The number of hosts is {len(list((ipNetwork.hosts())))}")
print(f"The valid address range is {ipNetwork.network_address+1} to {ipNetwork.broadcast_address-1}")

print(f"With this subnet mask 255.255.240.0 answer the following questions")
ipInterface = ipaddress.ip_interface('137.195.5.56/255.255.240.0')
ipNetwork = ipInterface.network
print(f"The number of bits used in the subnet mask is {ipNetwork.prefixlen}")
print(f"The number of hosts is {len(list(ipNetwork.hosts()))}")

ipInterface = ipaddress.ip_interface('137.195.5.56/255.255.240.0')
ipNetwork = ipInterface.network
print(ipNetwork)
bitsBorrowed = 4
ipSubnetLength = ipNetwork.prefixlen + bitsBorrowed
print(f"the subnet mask length is {ipSubnetLength}")
print(f"the 56 subnets neeeded are less than the {len(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=bitsBorrowed)))} subnets created")