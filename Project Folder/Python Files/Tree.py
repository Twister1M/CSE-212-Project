# Here is a series of examples of trees in python:

# Create a Binary Search Tree, code pulled from https://blog.boot.dev/computer-science/binary-search-tree-in-python/

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


""" -------------------------------------------------------- """

newTree = BSTNode()
print("Tree created.")
newTree.insert(2)
print("2 inserted into tree.")
newTree.insert(3)
print("3 inserted into tree.")
newTree.insert(5)
print("5 inserted into tree.")
newTree.insert(4)
print("4 inserted into tree.")
newTree.insert(6)
print("6 inserted into tree.")

orderedList = newTree.inorder([])
print(f"Tree in value order is {orderedList}")

print(f"It is {newTree.exists(3)} that 3 is in the tree.")

newTree.delete(3)

orderedList = newTree.inorder([])
print(f"Tree in value order is {orderedList}")

print(f"It is {newTree.exists(3)} that 3 is in the tree.")

print(f"Min is {newTree.get_min()}")

print(f"Max is {newTree.get_max()}")

preorderedList = newTree.preorder([])

postorderedList = newTree.postorder([])

print(f"Tree in pre-order is {preorderedList}")

print(f"Tree in post-order is {postorderedList}")