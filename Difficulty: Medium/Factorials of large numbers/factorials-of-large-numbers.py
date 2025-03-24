#User function Template for python3

import math

class Solution:
    def factorial(self, n):
        result = math.factorial(n)  # Compute factorial
        return list(map(int, str(result)))  # Convert to list of digits

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        print(" ".join(
            str(i) for i in
            ans))  # Join each digit to form the full number without spaces
        print("~")

# } Driver Code Ends