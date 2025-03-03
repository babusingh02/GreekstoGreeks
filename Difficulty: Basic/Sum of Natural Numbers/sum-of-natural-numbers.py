
class Solution:
    def seriesSum(self, n: int) -> int:
        return (n * (n + 1)) // 2  # Using the formula for the sum of the first n natural numbers

        



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
        print("~")

# } Driver Code Ends