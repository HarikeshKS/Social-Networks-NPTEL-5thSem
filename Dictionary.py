d1={x:x**2 for x in range(0,10)}     # Just a way to create a dictionary
print(d1)

# For listing the data inside the dictionary:
print(d1.keys())
print(d1.values())
print(d1.items())

# Creating dictionary for even values:
d2={x:x**2 for x in range(0,10) if x%2==0}     # Just a way to create a dictionary
print("d2 = ",d2)

# For checking the presence of any key in the dictionary: 
print(1 in d1)
print(1 in d2)