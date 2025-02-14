class Solution:
    def getSecondLargest(self, arr):
        # If there are less than 2 distinct elements
        if len(arr) < 2:
            return -1
        
        first = second = -1  # Initial values are set to -1
        
        for num in arr:
            # Update first and second if a new largest number is found
            if num > first:
                second = first
                first = num
            # Update second if num is not equal to first and greater than second
            elif num > second and num != first:
                second = num
        
        # If second is still -1, it means no second largest was found
        return second if second != -1 else -1

# Example usage:



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends