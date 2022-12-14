# Here is a series of examples of sets in python:

# Create a set
MySet1 = set()

# Add values to the set using the .add method
MySet1.add(2)
MySet1.add(3)
MySet1.add("Steve")
MySet1.add(6.3)

# Print to console
print(MySet1)

# Remove a value
MySet1.remove(2)
print(MySet1)

# Combine two sets
MySet2 = set({"John", 5, 3})
MySet3 = MySet1.union(MySet2)
print(MySet3)
# Notice how a new set is created to store the union.  Unions must be set to a variable.

# Difference between two sets
MySet4 = set({"Andrew", 3, 4, 6.3})
MySet5 = MySet3.difference(MySet4)
print(MySet5)

# Clear a set for later use
MySet1.clear()
print(MySet1)

""" -------------------------------------------------------- """

# 1. What will the variable 'output' be assigned?

Set1 = set({1,2,3})
Set2 = set({3,1,1,2})
output = Set1.union(Set2)


# 1. What is found in set1 that isn't in set2?

Set1 = set({3, "apple", 7.23, 3})
Set2 = set({4, "apple", 7.12, "apple"})
difference = Set1.difference(Set2)


# 1. What will be the length of the set?

Set = set()
Set.add(3)
Set.add(3)
Set.add(7)
Set.add(6)
Set.add(7)
Set.add(3)
Set.add(4)
