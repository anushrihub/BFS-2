# https://leetcode.com/problems/cousins-in-binary-tree/
# BFS approach:
# Time Complexity- O(n) Space Complexity- O(n)

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # intialise the dequeue
        q = deque()
        # add the root node in the deque
        q.append(root)
        # define the flags
        x_found = False
        y_found = False

        while q:
            size = len(q)
            # iterate over the queue
            for _ in range(size):
                # take out the left element
                curr = q.popleft()
                # checking the siblings for the currently popped node
                # if there is value for left and right
                if curr.left is not None and curr.right is not None:
                    # compare the given values at left and right
                    if curr.left.val == x and curr.right.val == y:
                        # it will return false because in this it wont be cousins but siblings
                        return False
                    # compare the given values at right and left
                    if curr.right.val == x and curr.left.val == y:
                        # it will return false because in this it wont be cousins but siblings
                        return False
                # check if current node is x that is do we find the value on this level
                # we are iterating through the queue, so we would find the both values on same level if they are exist in this way
                if curr.val == x:
                    x_found = True
                # check if current node is y
                if curr.val == y:
                    y_found = True

                # add children into the queue, if the left node is present 
                if curr.left is not None:
                    q.append(curr.left)
                # add children into the queue, if the right node is present
                if curr.right is not None:
                    q.append(curr.right)
        
            # check if both values are found, if yes return True
            if x_found and y_found:
                return True
            # check if both values are found, if either of them found return False
            if x_found or y_found:
                return False
            
        return True

# DFS:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_level = -1
        self.y_level = -1
        self.x_parent = None
        self.y_parent = None

        def helper(node, level, parent):
            # base case
            if node is None:
                return
            # check if the current node is X
            if node.val == x:
                self.x_level = level
                self.x_parent = parent
            # check if the current node is Y
            if node.val == y:
                self.y_level = level
                self.y_parent = parent
            # if we dont found the match go deeper
            if self.x_parent is None or self.y_parent is None:
                helper(node.left, level + 1, node)
            # if we dont found the match go deeper
            if self.x_parent is None or self.y_parent is None:
                helper(node.right, level + 1, node)

        helper(root, 0, None)
        return self.x_level == self.y_level and self.x_parent != self.y_parent
