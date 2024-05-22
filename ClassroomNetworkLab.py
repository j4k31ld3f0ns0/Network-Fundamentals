#Classroom 1 - 30 computers
#Classroom 2 - 30 computers
#Classroom 3 - 14 computers
#Classroom 4 - 14 computers
#Classroom 5 - 14 computers
#Lab 1 - 6 computers
#Lab 2 - 6 computers
# 138.191.0.0/25 is our address and subnet mask
#We have 128 total addresses to work with, 2^7 = 128

import ipaddress
import time
ipInterface = ipaddress.ip_interface('138.191.0.0/25')
ipNetwork = ipInterface.network

classroom = (list(ipaddress.ip_network(ipNetwork).subnets(prefixlen_diff=2)))
# print(classroom[0]) #classroom 1
# print(classroom[1]) #classroom 2
# print(classroom[2]) #for smallclass 1
# print(classroom[3]) #for smallclass 2

smallClassroom1 = (list(ipaddress.ip_network(classroom[2]).subnets(prefixlen_diff=1)))
# print(smallClassroom1[0]) #for classroom 3
# print(smallClassroom1[1]) #for classroom 4

smallClassroom2 = (list(ipaddress.ip_network(classroom[3]).subnets(prefixlen_diff=1)))
# print(smallClassroom2[0]) #for classroom 5
# print(smallClassroom2[1]) #for labs

labs = (list(ipaddress.ip_network(smallClassroom2[1]).subnets(prefixlen_diff=1)))
# print(labs[0]) #for lab 1
# print(labs[1]) #for lab 2
print(f"IP address and network information longest mask order")
print("---------------------------------------------------------------------------------------")
time.sleep(1)

print('Lab 1')
print(labs[0])
print(f"Lab 1 network address: {labs[0].network_address}")
print(f"Lab 1 broadcast address: {labs[0].broadcast_address}")
print(f"Lab 1 number of hosts: {len(list(labs[0].hosts()))}")
print(f"Lab 1 valid host range: {labs[0].network_address+1} to {labs[0].broadcast_address-1}")

print("---------------------------------------------------------------------------------------")
time.sleep(1)

print('Lab 2')
print(labs[1])
print(f"Lab 2 network address: {labs[1].network_address}")
print(f"Lab 2 broadcast address: {labs[1].broadcast_address}")
print(f"Lab 2 number of hosts: {len(list(labs[1].hosts()))}")
print(f"Lab 2 valid host range: {labs[1].network_address+1} to {labs[1].broadcast_address-1}")

print("---------------------------------------------------------------------------------------")
time.sleep(1)

print('Small Classroom 1')
print(smallClassroom1)
print(f"Small Classroom 1 network address: {smallClassroom1[1].network_address}")
print(f"Small Classroom 1 broadcast address: {smallClassroom1[1].broadcast_address}")
print(f"Small Classroom 1 number of hosts: {len(list(smallClassroom1[1].hosts()))}")
print(f"Small Classroom 1 valid host range: {smallClassroom1[1].network_address+1} to {smallClassroom1[1].broadcast_address-1}")

print("---------------------------------------------------------------------------------------")
time.sleep(1)

print('Small Classroom 2')
print(smallClassroom2[0])
print(f"Small Classroom 2 network address: {smallClassroom2[0].network_address}")
print(f"Small Classroom 2 broadcast address: {smallClassroom2[0].broadcast_address}")
print(f"Small Classroom 2 number of hosts: {len(list(smallClassroom2[0].hosts()))}")
print(f"Small Classroom 2 valid host range: {smallClassroom2[0].network_address+1} to {smallClassroom2[0].broadcast_address-1}")

#the small classroom code seems a bit buggy with the List instantiation for those variables, double check those pls