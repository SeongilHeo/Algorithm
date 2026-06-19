"""
We need to detect the edge that creates a cycle.

I use Union-Find for this problem.

Union-Find helps us check whether two nodes are already connected.

I create a find function to get the root of a node.
The find function follows the parent links recursively until it reaches the representative root.
## 
For example, we may have a structure like 1 -> 2 -> 3 in the Union-Find tree.

In this case, node 1 is the root, so find(1), find(2), and find(3) all return 1.
## 
Then I create a union function.
The union function takes two nodes and compares their roots.

If the two nodes have different roots, they are not connected yet, so we merge the two groups.

If they have the same root, it means they are already connected.
So adding this edge would create a cycle.

Therefore, I iterate through all edges and run union for each edge.
When union returns false, I return that edge as the redundant connection.
"""
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False
            
            parent[root_b] = root_a
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
            
            
