
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

    # Function to calculate the trapped rainwater.
    def maxWater(self, arr: List[int]) -> int:
        if not arr or len(arr) < 3:
            return 0
        
        n = len(arr)
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])
        
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - arr[i]
        
        return water



#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends