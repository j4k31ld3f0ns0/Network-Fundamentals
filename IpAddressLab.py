import ipaddress
##This takes an IP address and subnet mask value and assigns it to a variable called ipNetworkAddress, then we print out the value
ipNetworkAddress = ipaddress.ip_interface('137.190.163.195/21') #32 - 24 = host number | The number at the end dictates how many devices are available on the subnet ("anby operation"?)
numberOfSubnets = int(input("Enter how many subnets: "))
print(ipNetworkAddress)
#This takes that IpAddress value and subnet mask and determines the network address and assigns it to a variable networkAddress
networkAddress = ipNetworkAddress.network
print(networkAddress)
## This prints out the network address
print(f"The network address is {ipaddress.ip_network(networkAddress).network_address}")
firstUsableAddress = (ipaddress.ip_network(networkAddress).network_address) + 1
## This prints out the first address that can be assigned to a client device (computer/printer/device)
print(f"The first usable address is {firstUsableAddress}")
## This prints out the broadcast address for the network
broadcastAddress = ipaddress.ip_network(networkAddress).broadcast_address
print(f"the broadcast address is {broadcastAddress}")
## This prints out the last address that can be assigned to a client device (computer/printer/device)
print(f"The last usable address is {ipaddress.ip_network(networkAddress).broadcast_address}")
# This prints out the total number of addresses available to assign
print(f"the total number of available addresses is {(ipaddress.ip_network(networkAddress).num_addresses)-2}")
# This prints out how many subnets are created if we borrow extra bits
print(f"The number of subnets created by adding {numberOfSubnets} bits is :{len(list(ipaddress.ip_network(networkAddress).subnets(prefixlen_diff=numberOfSubnets)))}")
## This lists the number prefix length of the network(i.e. /24)
print(f"The prefix length is /{ipaddress.ip_network(networkAddress).prefixlen}")
## This will list the number of hosts or devices in the subnet
print(f"The number of hosts in the network is :{len(list(ipaddress.ip_network(networkAddress).hosts()))}")
## This will list all the IP Addressses of the devices in the subnet
print(list(ipaddress.ip_network(networkAddress)))