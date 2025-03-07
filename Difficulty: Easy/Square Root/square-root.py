#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
        if n == 0 or n == 1:
            return n  # Square root of 0 is 0, and of 1 is 1
        
        left, right = 1, n // 2  # Square root cannot be greater than n//2 for n > 1
        ans = 1  # To store floor value
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == n:
                return mid  # Perfect square case
            elif mid * mid < n:
                ans = mid  # Store mid as potential answer
                left = mid + 1  # Move right to find a closer value
            else:
                right = mid - 1  # Move left to decrease square value
        
        return ans  # Return floor of sqrt(n)

# Example usage:
sol = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends