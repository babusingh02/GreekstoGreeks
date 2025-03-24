# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0  # Initialize prefix sum
        sum_indices = {}  # Dictionary to store prefix sum and first occurrence index
        max_length = 0  # Variable to store maximum subarray length
        
        for i, num in enumerate(arr):
            prefix_sum += num  # Update prefix sum
            
            if prefix_sum == k:
                max_length = i + 1  # Update max_length if sum from index 0 to i is k
            
            if (prefix_sum - k) in sum_indices:
                max_length = max(max_length, i - sum_indices[prefix_sum - k])
            
            if prefix_sum not in sum_indices:  # Store first occurrence of prefix sum
                sum_indices[prefix_sum] = i
        
        return max_length

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends