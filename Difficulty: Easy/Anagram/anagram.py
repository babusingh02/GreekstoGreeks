#User function Template for python3

class Solution:
    # Function to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends