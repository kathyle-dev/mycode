#! /usr/bin/env python3

#create a list
proto = ["ssh", "http", "https"]

#print the list
print(proto)

#print the second element of the list
print(proto[1])

#use extend to add to the list
proto.append("dns")

#print the list
print(proto)

#create a new list of ints
proto2 = [ 22, 80, 443, 53 ]

#extend the first list by passing in the second list
proto.extend(proto2)

#print the first list
print(proto)

#create a list, similar to the first, that will have append() used on it
protoa = ["ssh", "http", "https"]

#append this list with "dns"
protoa.append("dns")

#append this list with the second list
protoa.append(proto2)

#now print the appended list
print(protoa)
