class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])  # Split the words, reverse the list, and join with a single space




#{ 
 # Driver Code Starts
class Main:
    if __name__ == "__main__":
        t = int(input())  # Read the number of test cases

        for _ in range(t):
            s = input().strip()  # Read the input string

            # Remove surrounding quotes from the string
            str_ = s[1:-1]

            obj = Solution()  # Create an object of the Solution class
            ans = obj.reverseWords(str_)  # Reverse the words in the string

            # Print the result with surrounding quotes
            print(f'"{ans}"')

# } Driver Code Ends