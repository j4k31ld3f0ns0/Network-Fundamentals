import ipaddress
import time

ipInterface = ipaddress.ip_interface('192.168.0.0/16')
ipNetwork = ipInterface.network

print(f"{ipInterface}")
print(f"{ipNetwork}")

## We need to break our network up into smaller groups to match our organization. We have 11 colleges and divisions. We need ??? subnets.
#we need 4 bits to have 11 subnets
college = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=4))
print(college)
### 0000 -> 0001 -> 0010 -> 0011 -> 0101 -> 0110 -> 0111 -> 1000 -> 1001 -> 1010 -> 1011 ->  1100 -> 1101 -> 1110 -> 1111
print(college[0])
print(college[1])
print(college[2])
print("The following  is a list of the college and division network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------")
print(f"The college of Engineering and Applied Science network address and subnet mask values are: {college[0]}")
print(f"The college of Engineering and Applied Science valid host address range: {college[0].network_address+1} - {college[0].broadcast_address-1}")

print(f"The college of Arts and Humanities network address and subnet mask values are: {college[1]}")
print(f"The college of Arts and Humanities valid host address range: {college[1].network_address+1} - {college[1].broadcast_address-1}")

time.sleep(3) #how long to wait in seconds
EAST = list(ipaddress.ip_network(college[0]).subnets(prefixlen_diff=3))
print(EAST)
print(EAST[0])
print(EAST[1])

print("The following  is a list of the departments within College of Engineering and Applied Science network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------")
print(f"The Computer Science Department network address and subnet mask values are: {EAST[0]}")
print(f"The Computer Science Department valid host address range: {EAST[0].network_address+1} - {EAST[0].broadcast_address-1}")

print(f"The x Department network address and subnet mask values are: {EAST[1]}")
print(f"The x Department valid host address range: {EAST[1].network_address+1} - {EAST[1].broadcast_address-1}")

print(f"The y Department network address and subnet mask values are: {EAST[2]}")
print(f"The y Department valid host address range: {EAST[2].network_address+1} - {EAST[2].broadcast_address-1}")

print(f"The z Department network address and subnet mask values are: {EAST[3]}")
print(f"The z Department valid host address range: {EAST[3].network_address+1} - {EAST[3].broadcast_address-1}")

print(f"The a Department network address and subnet mask values are: {EAST[4]}")
print(f"The a Department valid host address range: {EAST[4].network_address+1} - {EAST[4].broadcast_address-1}")

print(f"The b Department network address and subnet mask values are: {EAST[5]}")
print(f"The b Department valid host address range: {EAST[5].network_address+1} - {EAST[5].broadcast_address-1}")

print(f"The c Department network address and subnet mask values are: {EAST[6]}")
print(f"The c Department valid host address range: {EAST[6].network_address+1} - {EAST[6].broadcast_address-1}")

print(f"The d Department network address and subnet mask values are: {EAST[7]}")
print(f"The d Department valid host address range: {EAST[7].network_address+1} - {EAST[7].broadcast_address-1}")