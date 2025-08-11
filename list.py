# 1. Create an empty list called my_list.
my_list = []  # Create an empty list

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)  # Print the current list

# 3. Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

print(my_list)  # Print the list after insertion

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

print(my_list)  # Print the list after extending

# 5. Remove the last element from my_list.
my_list.pop()
print(my_list)  # Print the list after popping

# 6. Sort my_list in ascending order.
my_list.sort()
print(my_list)  # Print the sorted list

# 7. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")  # Print the index of 30
