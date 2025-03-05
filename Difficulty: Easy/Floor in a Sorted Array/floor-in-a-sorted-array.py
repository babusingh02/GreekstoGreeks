class Solution:
    # Function to find the floor index of x in a sorted array
    def findFloor(self, arr, x):
        low, high = 0, len(arr) - 1
        floor_index = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                floor_index = mid  # Update floor index
                low = mid + 1  # Move right to find the last occurrence
            else:
                high = mid - 1  # Move left
        
        return floor_index
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends