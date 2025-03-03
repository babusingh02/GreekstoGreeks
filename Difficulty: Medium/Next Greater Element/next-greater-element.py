# User function Template for python3

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n  # Initialize result array with -1
        stack = []  # Stack to keep indexes of elements
        
        for i in range(n):
            # While stack is not empty and the current element is greater than stack's top element
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                result[index] = arr[i]  # Assign the next greater element
            
            stack.append(i)  # Push current index onto stack
        
        return result



#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends