#User function Template for python3

class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place each number in its correct index position (1-based)
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]  # Swap
        
        # Step 2: Find the first missing positive number
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1  # Missing number found
        
        # Step 3: If all numbers are in place, return n + 1
        return n + 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends