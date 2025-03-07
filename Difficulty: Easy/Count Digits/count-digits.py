#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count = 0
        temp = n  # Store original number
        
        while temp > 0:
            digit = temp % 10  # Extract last digit
            if digit != 0 and n % digit == 0:  # Check divisibility
                count += 1
            temp //= 10  # Remove last digit
        
        return count

# Example usage:
sol = Solution()

   # Output: 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends