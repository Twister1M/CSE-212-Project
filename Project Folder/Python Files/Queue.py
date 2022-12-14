# Here is a few example of queues in python:

# The queue is set as an empty list.
Queue = []

# The strings 'John' and 'Steve' are added to the queue.

Queue.append('John')
Queue.append('Steve')

# John is at the front since he was added first.

Next = Queue.pop(0)

print("Pulled " + Next + "\n")

# John is popped out of the queue since he is at position 0.

# Next, we are going to create a queue class for ease of use.

# This class sets up a queue so we simply need to use the .add and .remove function to add to the queue and pull the next in line.

class Queue():
    
    def __init__(self, list):
        
        self.list = list
    
    
    
    def add(self, next):
        
        self.list.append(next)
    
    
    
    def remove(self):
        
        out = self.list.pop(0)
        return out
    
    
    def size(self):
        
        length = len(self.list)
        return length


""" ---------------------------------------------------------- """


# For this example, let's set up a scenario where people are waiting on hold on a caller list.

# Create a queue called "callers" that John and Steve are already a part of.
Callers = Queue(["John", "Steve"])
print(Callers.list)

# Amy calls:
Callers.add("Amy")
print(Callers.list)

# Lucy calls:
Callers.add("Lucy")
print(Callers.list)

# John is pulled out of the queue:
Callers.remove()
print(Callers.list)

# Everyone else is pulled out:
for _ in range(0,len(Callers.list)):
    Callers.remove()

print(Callers.list)


""" ---------------------------------------------------------- """

# What will be output in the following example?

Numbers = Queue([3, 2, 1, 6, 5])
print(Numbers.size())
Numbers.add(3)
print(Numbers.size())
Output = Numbers.remove()
print(Output)