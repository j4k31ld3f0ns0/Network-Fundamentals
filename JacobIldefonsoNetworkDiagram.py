import ipaddress
import time

ipInterface = ipaddress.ip_interface('138.191.0.0/16')
ipNetwork = ipInterface.network

print(f"{ipInterface}")
print(f"{ipNetwork}")

## We need to break our network up into smaller groups to match our organization. We have 11 colleges and divisions. We need ??? subnets.
#we need 4 bits to have 11 subnets
college = list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=4))
print(college)
print("The following  is a list of the college and division network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------")

print(f"The college of Engineering and Applied Science network address and subnet mask values are: {college[0]}")
print(f"The college of Engineering and Applied Science valid host address range: {college[0].network_address+1} - {college[0].broadcast_address-1}")

print(f"The college of Arts & humanities network address and subnet mask values are: {college[1]}")
print(f"The college of Arts & humanities valid host address range: {college[1].network_address+1} - {college[1].broadcast_address-1}")

print(f"The college of Education network address and subnet mask values are: {college[2]}")
print(f"The college of Education valid host address range: {college[2].network_address+1} - {college[2].broadcast_address-1}")

print(f"The college of Business & Economics network address and subnet mask values are: {college[3]}")
print(f"The college of Business & Economics valid host address range: {college[3].network_address+1} - {college[3].broadcast_address-1}")

print(f"The college of Health network address and subnet mask values are: {college[4]}")
print(f"The college of Health valid host address range: {college[4].network_address+1} - {college[4].broadcast_address-1}")

print(f"The college of Science network address and subnet mask values are: {college[5]}")
print(f"The college of Science valid host address range: {college[5].network_address+1} - {college[5].broadcast_address-1}")

print(f"The college of Social & Behavioral Science network address and subnet mask values are: {college[6]}")
print(f"The college of Social & Behavioral Science valid host address range: {college[6].network_address+1} - {college[6].broadcast_address-1}")

print(f"The Division of Information Technology network address and subnet mask values are: {college[7]}")
print(f"The Division of Information Technology valid host address range: {college[7].network_address+1} - {college[7].broadcast_address-1}")

print(f"The Division of Student Affairs network address and subnet mask values are: {college[8]}")
print(f"The Division of Student Affairs valid host address range: {college[8].network_address+1} - {college[8].broadcast_address-1}")

print(f"The Division of Facilities Management network address and subnet mask values are: {college[9]}")
print(f"The Division of Facilities Management valid host address range: {college[9].network_address+1} - {college[9].broadcast_address-1}")

print(f"The Division of Administrative Services network address and subnet mask values are: {college[10]}")
print(f"The Division of Administrative Services valid host address range: {college[10].network_address+1} - {college[10].broadcast_address-1}")

##Subdividing the individual departments
EAST = list(ipaddress.ip_network(college[0]).subnets(prefixlen_diff=3))
AAH = list(ipaddress.ip_network(college[1]).subnets(prefixlen_diff=3))
EDU = list(ipaddress.ip_network(college[2]).subnets(prefixlen_diff=3))
BAE = list(ipaddress.ip_network(college[3]).subnets(prefixlen_diff=3))
HLT = list(ipaddress.ip_network(college[4]).subnets(prefixlen_diff=3))
SCI = list(ipaddress.ip_network(college[5]).subnets(prefixlen_diff=3))
SBS = list(ipaddress.ip_network(college[6]).subnets(prefixlen_diff=3))
DIT = list(ipaddress.ip_network(college[7]).subnets(prefixlen_diff=3))
DSA = list(ipaddress.ip_network(college[8]).subnets(prefixlen_diff=3))
DFM = list(ipaddress.ip_network(college[9]).subnets(prefixlen_diff=3))
DAS = list(ipaddress.ip_network(college[10]).subnets(prefixlen_diff=3))

print("Each department is subdivided equally, therefore the individual IP addresses are redudant to name for a given department. Pick and choose and the result is the same.")

print("The following  is a list of the departments within College of Engineering and Applied Science network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1) #how long to wait in seconds
x=0
for dept in EAST:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within College of Arts & Humanties network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in AAH:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within College of Education network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in EDU:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within College of Business and Economics network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in BAE:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within College of Health network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in HLT:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within College of Science network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in SCI:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within College of Social and Behavioral Science network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in SBS:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within Division of Information Technology network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in DIT:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within Division of Student Affairs network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in DSA:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within Division of Facilities Management network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in DFM:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0
print("The following  is a list of the departments within Division of Administrative Services network addresses and subnetmasks")
print("---------------------------------------------------------------------------------------------------------------------------------")
for dept in DAS:
    x = x+1
    print(f"Department {x}'s network address and subnet mask values are: {dept}")
    print(f"The valid host range is {dept.network_address+1} - {dept.broadcast_address-1}")
x=0