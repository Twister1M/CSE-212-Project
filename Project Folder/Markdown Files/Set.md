# Sets

### Definition

A set is a data storage technique that is somewhat unique when it comes to storage in that the position of elemnts does not matter.  A set is a 'list' of items where the order is not stored and each item can only be stored once.
For example, if you tried to add the word 'banana' to a set twice, you would only find it in the set once.  A set is unordered, its items are unchangeable, and it is unindexed.  This means the only information about it available is
what the data inside of it is, and the data cannot be directly changed - it must be removed and then added.  Sets are extremely fast in its three functions - adding, removing, and finding (is it a part of the set).



### Terms

Add - add to set

Remove - remove from set

Membership - determines if a value is a member of a set

Size - the size of the set



### Uses

Sets are very useful in keeping basic traffic information through a system, whether that system is digital or physical.  One example is a sign-in system at a place of work.  Users would sign in to work, and then sign out when they leave.
A set would work here because it simply needs to keep track of those who are present, and can quickly remove them when they leave.  While a list would work as well, it would be slower.

For a more complicated example, if you needed to see the ID's of users who use a system in the past hour, a set could be used to store this data.
Since it doesn't store duplicates, the set would be of minimum possible size at all times, and the set can be added/removed from after a one-hour period of non-activity from each user.



### Sets in Python

In python, to create a set, the function set() is used, where the data is placed inside the parentheses.
Since sets are a built-in data storage type, sets have many methods (functions that apply to them).  Some of the most important are as follows:

set(data): creates a set\
O(1)

set.add(item): adds an item to the set\
O(1)

set.remove(item): removes an item from the set\
O(1)

set1.union(set2): combines two sets\
O(1)

set1.difference(set2): returns a set containing the items that are in set 1 but not in set 2\
O(n)

set.clear(): empties a set\
O(1)

len(set): length of a set\
O(1)

checking for an item in a set:\

    if value in set:
        return True
    else
        return False

O(1)



### Python Examples

Continue into the python file for examples of the above functions as well as example applications; otherwise read through the code here.

Here is a series of examples of sets in python:

Create a set:

    MySet1 = set()



Add values to the set using the .add method:

    MySet1.add(2)
    MySet1.add(3)
    MySet1.add("Steve")
    MySet1.add(6.3)



Print to console:

    print(MySet1)



Remove a value:

    MySet1.remove(2)
    print(MySet1)



Combine two sets:

    MySet2 = set({"John", 5, 3})
    MySet3 = MySet1.union(MySet2)
    print(MySet3)

Notice how a new set is created to store the union.  Unions must be set to a variable.



Difference between two sets

    MySet4 = set({"Andrew", 3, 4, 6.3})
    MySet5 = MySet3.difference(MySet4)
    print(MySet5)



Clear a set for later use

    MySet1.clear()
    print(MySet1)



-------------------- Examples -------------------------



1. What will the variable 'output' be assigned?

    Set1 = set({1,2,3})
    Set2 = set({3,1,1,2})
    output = Set1.union(Set2)



2. What is found in set1 that isn't in set2?

    Set1 = set({3, "apple", 7.23, 3})
    Set2 = set({4, "apple", 7.12, "apple"})
    difference = Set1.difference(Set2)



3. What will be the length of the set?

    Set = set()
    Set.add(3)
    Set.add(3)
    Set.add(7)
    Set.add(6)
    Set.add(7)
    Set.add(3)
    Set.add(4)

### Python Example Solutions

1. {1, 2, 3}
2. {3, 7.23}
3. 4