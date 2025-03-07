#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        if not arr:  # If array is empty, return 0
            return 0
        
        # Two-pointer approach
        unique_index = 0  # Position to place unique elements
        
        for i in range(1, len(arr)):
            if arr[i] != arr[unique_index]:  # Found a new distinct element
                unique_index += 1
                arr[unique_index] = arr[i]  # Move distinct element forward
        
        return unique_index + 1  # Return the length of the unique elements

# Example Usage:
sol = Solution()


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends