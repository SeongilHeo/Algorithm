"""We need to create a deep copy of the graph.

Each node has a value and a list of neighbors, so we need to copy both the nodes and their connections.

I use DFS to traverse the graph from the given node.

I also use a dictionary called old_to_new.
The key is the original node, and the value is the cloned node.

This dictionary helps us in two ways.
First, it prevents us from cloning the same node multiple times.
Second, it prevents infinite recursion when the graph has cycles.

In the DFS function, if the current node has already been cloned, I return the cloned node from the dictionary.

Otherwise, I create a new node with the same value as the current node.
Then I store the mapping from the original node to the cloned node.

After that, I iterate through all neighbors of the current node.
For each neighbor, I recursively clone it and append the cloned neighbor to the current cloned node’s neighbors list.

Finally, I return the cloned version of the starting node."""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]
            
            copy = Node(cur.val)
            old_to_new[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        
        return dfs(node)
