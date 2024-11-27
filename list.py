#1: Create an empty list called my_list
my_list = []

# 2: Append the elements 10, 20, 30, 40 to my_list at the end of the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3: Insert the value 15 at the second position in the list, (position, value)
my_list.insert(1, 15)

# 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5: Remove the last element from my_list using pop() method
my_list.pop()

# 6: Sort my_list in ascending order using sort() method which arranges the elements in ascending order by default
my_list.sort()

# 7: Find and print the index of the value 30 in my_list using index() method
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Printing the final list
print("Final sorted list:", my_list)
