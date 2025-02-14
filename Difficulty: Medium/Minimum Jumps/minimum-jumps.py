#User function Template for python3
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If the array has less than 2 elements, no jump is required
        if n <= 1:
            return 0
        
        # If the first element is 0, it's not possible to move
        if arr[0] == 0:
            return -1
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n):
            # Update the farthest position that can be reached
            farthest = max(farthest, i + arr[i])
            
            # If we've reached the end of the current range, we need to make a jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we have reached or exceeded the last index, return the result
                if current_end >= n - 1:
                    return jumps
        
        # If we finish the loop and can't reach the end, return -1
        return -1

# Example u

	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends