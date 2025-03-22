#User function Template for python3

from collections import deque
from typing import List

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        visited = set()
        queue = deque([0])  # Start BFS from vertex 0
        bfs_traversal = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs_traversal.append(node)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return bfs_traversal

    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr: List[int], d: int) -> None:
        n = len(arr)
        d = d % n  # Handle cases where d > n
        arr[:] = arr[d:] + arr[:d]


        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends