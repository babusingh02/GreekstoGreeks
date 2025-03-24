#User function Template for python3
from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        arr = list(map(str, arr))  # Convert all numbers to strings
        
        # Custom sorting: if x+y > y+x, x should come first
        arr.sort(key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1))
        
        result = ''.join(arr)
        return '0' if result[0] == '0' else result  # Handle leading zeros case



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends