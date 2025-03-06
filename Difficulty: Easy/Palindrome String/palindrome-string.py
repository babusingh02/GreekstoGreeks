#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]  # Reverse the string and check if it's equal to the original


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends