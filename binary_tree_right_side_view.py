# https://leetcode.com/problems/binary-tree-right-side-view/

# BFS approach:
# Time Complexity- O(n) Space Complexity- O(n)

from collections import deque
class Solution:
    def rightSideView(self, root) -> list[int]:
        result = []
        # handling the edge case
        if root is None:
            return result
        # define the queue
        q = deque()
        # add the root of the tree in the deque
        q.append(root)

        while q:
            # number of the node at the current level
            size = len(q)
            # iterate over the deque
            for i in range(size):
                # pop the leftmost node from the deque
                curr = q.popleft()
                # to pick the right most node check the condition when the i is equal to size(we took length while declaring, so size - 1)
                if i == size - 1:
                    # append the current value in to the result selt which is the rightmost node
                    result.append(curr.val)
                # check the left part of the tree
                if curr.left:
                    # append into the queue
                    q.append(curr.left)
                # check the left part of the tree
                if curr.right:
                    # append into the queue
                    q.append(curr.right)
        # return the result
        return result
    
