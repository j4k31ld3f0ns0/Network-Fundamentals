import ipaddress

#1 - 192.168.2.76/28 - Network address/First usable address
ipNetworkAddress = ipaddress.ip_interface('192.168.2.76/28')
networkAddress = ipNetworkAddress.network

print(f"The network address is {ipaddress.ip_network(networkAddress).network_address}")
print(f"The first usable address is {ipaddress.ip_network(networkAddress).network_address + 1}")

#2 - 192.168.2.76/9 - Network address/First usable address
ipNetworkAddress = ipaddress.ip_interface('192.168.2.76/9')
networkAddress = ipNetworkAddress.network

print(f"The network address is {ipaddress.ip_network(networkAddress).network_address}")
print(f"The first usable address is {ipaddress.ip_network(networkAddress).network_address + 1}")

#3 - 192.168.2.137/27 - Network address/First usable address
ipNetworkAddress = ipaddress.ip_interface('192.168.2.137/27')
networkAddress = ipNetworkAddress.network

print(f"The network address is {ipaddress.ip_network(networkAddress).network_address}")
print(f"The first usable address is {ipaddress.ip_network(networkAddress).network_address + 1}")

#4 - 101.10.2.8/15 - Total addresses/Usable addresses
ipNetworkAddress = ipaddress.ip_interface('101.10.2.8/15')
networkAddress = ipNetworkAddress.network

print(f"the total number of addresses is {(ipaddress.ip_network(networkAddress).num_addresses)}")
print(f"the total number of usable addresses is {(ipaddress.ip_network(networkAddress).num_addresses)-2}")

#5 - 101.10.2.8/29 - Total addresses/Usable addresses
ipNetworkAddress = ipaddress.ip_interface('101.10.2.8/29')
networkAddress = ipNetworkAddress.network

print(f"the total number of addresses is {(ipaddress.ip_network(networkAddress).num_addresses)}")
print(f"the total number of usable addresses is {(ipaddress.ip_network(networkAddress).num_addresses)-2}")

#6 - 192.168.2.137/27 - Broadcast address/Last usable address
ipNetworkAddress = ipaddress.ip_interface('192.168.2.137/27')
networkAddress = ipNetworkAddress.network

print(f"the broadcast address is {ipaddress.ip_network(networkAddress).broadcast_address}")
print(f"The last usable address is {ipaddress.ip_network(networkAddress).broadcast_address-1}")

#7 - 110.10.2.55/30 - Broadcast address/Last usable address
ipNetworkAddress = ipaddress.ip_interface('110.10.2.55/30')
networkAddress = ipNetworkAddress.network

print(f"the broadcast address is {ipaddress.ip_network(networkAddress).broadcast_address}")
print(f"The last usable address is {ipaddress.ip_network(networkAddress).broadcast_address-1}")

#8 - 110.10.10.64/20 - subnet prefix length
ipNetworkAddress = ipaddress.ip_interface('110.10.10.64/20')
networkAddress = ipNetworkAddress.network

print(f"The prefix length is /{ipaddress.ip_network(networkAddress).prefixlen}")

#9 - 110.10.10.64/25 - X subnets with Y addresses in each subnet
ipNetworkAddress = ipaddress.ip_interface('110.10.10.64/25')
networkAddress = ipNetworkAddress.network

numberOfSubnets = 32-28
print(f"The number of subnets created by adding {numberOfSubnets} bits is :{len(list(ipaddress.ip_network(networkAddress).subnets(prefixlen_diff=numberOfSubnets)))}")

#10 - 156.78.51.24/25 Total addresses
ipNetworkAddress = ipaddress.ip_interface('156.78.51.24/25')
networkAddress = ipNetworkAddress.network

print(f"the total number of addresses is {(ipaddress.ip_network(networkAddress).num_addresses)}")

#11 - 156.78.51.24/30 Total addresses
ipNetworkAddress = ipaddress.ip_interface('156.78.51.24/30')
networkAddress = ipNetworkAddress.network

print(f"the total number of addresses is {(ipaddress.ip_network(networkAddress).num_addresses)}")

#12 - 166.25.132.0/3 Total addressses
ipNetworkAddress = ipaddress.ip_interface('166.25.132.0/3')
networkAddress = ipNetworkAddress.network

print(f"the total number of addresses is {(ipaddress.ip_network(networkAddress).num_addresses)}")
