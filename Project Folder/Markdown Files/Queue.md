# Queues

### Definition

A queue is a data storage system that operates on a first-in first-out (FIFO) basis.  This means that the oldest item in the list is the next to be pulled out.
Queues are structured like a list, but only the oldest item is accessable.  



### Terms

Euqueue - add to queue

Dequeue - remove from queue 

Front - next in line to be removed

Back - most recently added to queue



### Uses

Queues have many uses, both in and outside of software.  When you think of a queue, what is the first thing that comes to your mind?  Probably a line of people waiting for something,
whether it is a grocery store, movie theater, or a rollercoaster.  Another type of queue is waiting to access something online, whether it's a database or a server (especially for popular games).  
This type of queue is a bit more complicated since there are multiple inputs but only one output.  Thus, there needs to be a program that can take in multiple inputs and order them by the time they
requested access.



### Queues in Python

Queues are not a built-in data structure, so they must be coded in as a new function or class (class is preferable).
The easiest way to create a queue is to take and pull from a list, since it is an indexed series of data.

Here is a simple class to set up a queue:

class Queue():
    
    def __init__(self, list):
    
        self.list = list
    
    
    
    def add(self, next):
    
        self.list.append(next)
    
    
    
    def remove(self):
        
        out = self.list.pop(0)
        return out
    

    def size(self):

        length = len(list)
        return length

.add(): Adds item to queue
O(1)

.remove(): Removes item from queue
O(n) where n is the number of items in the queue

.size(): Returns the size of the queue
O(1)



### Python Examples

Continue into the python file for examples of the above functions as well as example applications; otherwise read through the code here.

The queue is set as an empty list.
    Queue = []

The strings 'John' and 'Steve' are added to the queue.

    Queue.append('John')
    Queue.append('Steve')

John is at the front since he was added first.

    Next = Queue.pop(0)

John is popped out of the queue since he is at position 0.

Next, we are going to create a queue class for ease of use.

This class sets up a queue so we simply need to use the .add and .remove function to add to the queue and pull the next in line.

class Queue():
    
    def __init__(self, list):
    
        self.list = list
    
    
    
    def add(self, next):
    
        self.list.append(next)
    
    
    
    def remove(self):
        
        out = self.list.pop(0)
        return out
    
    

    def size(self):
    
        length = len(list)
        return length

------------------ Examples -------------------------


# For this example, let's set up a scenario where people are waiting on hold on a caller list.

Create a queue called "callers" that John and Steve are already a part of.

    Callers = Queue(["John", "Steve"])
    print(Callers.list)


Amy calls:

    Callers.add("Amy")
    print(Callers.list)


Lucy calls:

    Callers.add("Lucy")
    print(Callers.list)


John is pulled out of the queue:

    Callers.remove()
    print(Callers.list)


Everyone else is pulled out:

    for _ in range(0,len(Callers.list)):
        Callers.remove()

    print(Callers.list)




What will be output in the following example?

Numbers = Queue([3, 2, 1, 6, 5])
print(Numbers.size())
Numbers.add(3)
print(Numbers.size())
Output = Numbers.remove()
print(Output)



### Python Example Solution

5
6
3