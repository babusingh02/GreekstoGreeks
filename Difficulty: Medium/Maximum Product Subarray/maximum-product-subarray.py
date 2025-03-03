#User function Template for python3
class Solution:
    def maxProduct(self, arr):
        if not arr:
            return 0
        
        max_product = arr[0]  # Stores maximum product so far
        min_product = arr[0]  # Stores minimum product so far
        result = arr[0]  # Stores the final result
        
        for i in range(1, len(arr)):
            if arr[i] < 0:  # Swap max and min when encountering a negative number
                max_product, min_product = min_product, max_product
            
            max_product = max(arr[i], max_product * arr[i])  # Update max
            min_product = min(arr[i], min_product * arr[i])  # Update min
            
            result = max(result, max_product)  # Update final result
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends