"""
I model this problem as a directed graph.

Each course is a node, and each prerequisite pair [a, b] means there is an edge from b to a, because we need to take b before a.
    # pre -> course
    #     ^ indegree

Then I use topological sort with BFS.

First, I calculate the indegree of each course. The indegree means how many prerequisites a course still has.

Courses with indegree 0 can be taken immediately, so I put them into a queue.

Then, while the queue is not empty, I take one course and reduce the indegree of its next courses.

If a next course’s indegree becomes 0, it means all prerequisites are completed, so I add it to the queue.

At the end, if I was able to take all courses, I return true. Otherwise, there must be a cycle, so I return false.

"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # O(E)
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1


        queue = deque()

        # O(V)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        finishied = 0
        
        # while: O(V), while + for: O(E) -> O(E)
        while queue:
            cur = queue.popleft()
            finishied += 1
            for nxt in graph[cur]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    queue.append(nxt)
        

        return finishied == numCourses

numCourses = 2
prerequisites = [[1,0],[0,1]]

numCourses = 2
prerequisites = [[1,0]]

sol = Solution()
result = sol.canFinish(numCourses, prerequisites)

print(result)