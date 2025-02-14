#User function template for Python 3
class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        
        # First pass to find the potential majority element
        candidate = None
        count = 0
        
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Second pass to verify the candidate
        count = 0
        for num in arr:
            if num == candidate:
                count += 1
        
        # If the candidate appears more than n/2 times, it's the majority element
        if count > n // 2:
            return candidate
        return -1

# Example usage:

        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends