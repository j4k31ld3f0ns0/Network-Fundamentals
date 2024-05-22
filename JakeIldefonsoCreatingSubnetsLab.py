import ipaddress

ipInterface = ipaddress.ip_interface("192.168.5.0/2") #placeholder
print(f"the subnet mask for a 2 bit subnet is 11000000.00000000.00000000.00000000")
print(f"the 2 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/13")
print(f"the subnet mask for a 13 bit subnet is 11111111.11111000.00000000.00000000")
print(f"the 13 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/5")
print(f"the subnet mask for a 5 bit subnet is 11111000.00000000.00000000.00000000")
print(f"the 5 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/11")
print(f"the subnet mask for a 11 bit subnet is 11111111.11100000.00000000.00000000")
print(f"the 11 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/9")
print(f"the subnet mask for a 9 bit subnet is 11111111.10000000.00000000.00000000")
print(f"the 9 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/10")
print(f"the subnet mask for a 10 bit subnet is 11111111.11000000.00000000.00000000")
print(f"the 10 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/4")
print(f"the subnet mask for a 4 bit subnet is 11110000.10000000.00000000.00000000")
print(f"the 4 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/14")
print(f"the subnet mask for a 14 bit subnet is 11111111.11111100.00000000.00000000")
print(f"the 14 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/6")
print(f"the subnet mask for a 6 bit subnet is 11111100.00000000.00000000.00000000")
print(f"the 6 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/8")
print(f"the subnet mask for a 9 bit subnet is 11111111.00000000.00000000.00000000")
print(f"the 8 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("192.168.5.0/12")
print(f"the subnet mask for a 12 bit subnet is 11111111.11110000.00000000.00000000")
print(f"the 12 bit value is {ipInterface.netmask}")

ipInterface = ipaddress.ip_interface("132.8.150.67/22")
ipNetwork = ipInterface.network
print(f'The network address is {ipNetwork.network_address}') 
print(f'The network address is {ipNetwork.broadcast_address}') 
print(f"The number of hosts is {len(list((ipNetwork.hosts())))}")
print(f"The valid address range is {ipNetwork.network_address+1} to {ipNetwork.broadcast_address-1}")

ipInterface = ipaddress.ip_interface("166.0.13.8/255.255.252.0")
ipNetwork = ipInterface.network
print(f'The network address is {ipNetwork.network_address}') 
print(f'The network address is {ipNetwork.broadcast_address}') 
print(f"The number of hosts is {len(list((ipNetwork.hosts())))}")
print(f"The valid address range is {ipNetwork.network_address+1} to {ipNetwork.broadcast_address-1}")

ipInterface = ipaddress.ip_interface('137.195.5.56/255.255.255.192')
ipNetwork = ipInterface.network
print(f"The number of bits used in the subnet mask is {ipNetwork.prefixlen}")
print(f"The number of hosts is {len(list(ipNetwork.hosts()))}")

ipInterface = ipaddress.ip_interface('137.195.5.56/255.255.252.0')
ipNetwork = ipInterface.network
print(f"The number of bits used in the subnet mask is {ipNetwork.prefixlen}")
print(f"The number of hosts is {len(list(ipNetwork.hosts()))}")

ipInterface = ipaddress.ip_interface('137.195.5.56/255.255.255.248')
ipNetwork = ipInterface.network
print(f"The number of bits used in the subnet mask is {ipNetwork.prefixlen}")
print(f"The number of hosts is {len(list(ipNetwork.hosts()))}")

#56 Remote sites (subnets required)
#One class B IP address
#What mask would you use with a max amount of hosts at each site being 1000?

ipInterface = ipaddress.ip_interface('137.195.5.56/255.255.252.0')
ipNetwork = ipInterface.network
print(ipNetwork)
bitsBorrowed = 6
ipSubnetLength = ipNetwork.prefixlen + bitsBorrowed
print(f"the subnet mask length is {ipSubnetLength}")
print(f"You would need {len(list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=bitsBorrowed)))} subnets created to satisfy the 56 remote sites")