# Trees

### Definition

Trees are a series of linked lists where more than two nodes can be attached to another node.  There are multiple types of trees: binary trees, binary search trees, and balanced binary search trees.
Trees are useful in many different situations, from file storage to family trees.  Trees are a good way to sort data by category as well, instead of having lots of information in a single list.

Trees normally have a node that is considered the 'root' node.  This is where the tree starts, and is a parent to all other nodes.


### Types of Trees

Binary Trees are trees that can only have two children.  They are the typical fork-shaped trees:\
|     O   |
|    / \  |
|   O   O |
|  / \    |
| O   O   |

Binary Search Trees use a unique method of organization.  When adding a datapoint to the tree, the root node is compared to the datapoint.  If the new datapoint value is lower than the root value, it is placed as a child to the left.
If it is greater than the root value, it is placed as a child to the right.  If there is already a child to the side it is placed on, it is compared to that child and the loop repeats until it is placed in a location with no child.

|     5     |
|    / \    |
|   3   6   |
|  / \   \  |
| 2   4   7 |

Balanced Binary Search Trees are a special version of Binary Search Trees that automatically sort the data in the tree so that the difference between depth/height of the tree's branches is at a minimum.
A binary search tree is considered 'balanced' if it has a difference in depth/height of less than two.  Balanced binary search trees have an efficiency of O(logn) because, when searching for a value, you only need to look through
1 + log2(n) values where 'n' is the number of datapoints.


### Terms

Node - A datapoint in a tree.

Root - The starting node of a tree.  Also known as the base

Subtree - A tree that is part of another tree

Leaf - A node that is at the end of a tree

Parent - A node with another node attached to it

Child - A node attached to another node

Depth/Height - The number of connections to get to a certain node

Traverse - The action of searching through all nodes of a tree

Pre-order and Post-order - Methods of organizing the data of a tree into a list; not necessary at this time.


### Uses

Trees have many uses in data storage.  As previously mentioned, a good example of trees as data storage is file storage.  On your computer storage, each file is considered a node.  Folders are nodes that have children.
Thus, a folder could look like this: (F = folder, D = document)

|        F         |
|      /   \       |
|    F       F     |
|    |      / \    |
|    D     D   F   |
|              |   |
|              D   |

Binary Search Trees are a good way to organize data in large quantities that allows them to be accessed in a shorter amount of time than would be available with a list.  Think of a list of 20 numbers in numerical order.
If you needed to check if a certain number was in a tree, you would need to start from the beginning and go until you either found a number that is above the value (not in the list), or find the number in the list.
In the case of a binary search tree or balanced binary search tree, it would take much less time given the big O number.


### Trees in Python

Since there is no built-in tree data structure in python, to create a tree one needs to create a class.  There are multiple methods to implement this system.  One if which is as follows:

```
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
    
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
```

Important note:  You cannot use .delete() on the root of the tree.

This is a lot to look through, but the idea comes down to the following functions:
(For big O notation, 'n' is the size of the tree.)

BSTNode(): Create an empty Binary Search Tree, or a tree with one value inside the parentheses.\
O(1)

.insert(): Insert a new value into the tree.\
O(logn)

.get_min(): Finds the lowest value in the tree.\
O(logn)

.get_max(): Find the highest value in the tree.\
O(logn)

.delete(): Deletes the value placed in the parentheses.\
O(logn)

.exists(): Finds if the value placed in the parentheses exists.\
O(logn)

.inorder(): Returns list placed in parentheses with all tree's values in value-order.\
O(nlog(n))

.preorder(): Returns list placed in parentheses with tree's preorder notation.\
O(n)

.postorder(): Returns list placed in parentheses with tree's postorder notation.\
O(nlog(n))

### Python Examples

For examples, please continue to the Tree.py file.


### Errors

Since trees are more complicated than other data structures, they are more prone to errors.  Remember when using this implementation of trees (binary tree) that only numbers are expected as values.
These numbers can be int-s or float-s, but strings or other characters may produce unwanted results.