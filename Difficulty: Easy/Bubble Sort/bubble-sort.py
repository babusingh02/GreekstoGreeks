#User function Template for python3

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr):
        n = len(arr)
        
        for i in range(n - 1):  # Number of passes
            swapped = False  # Optimization to check if swapping occurred
            
            for j in range(n - i - 1):  # Compare adjacent elements
                if arr[j] > arr[j + 1]:  # Swap if the left element is greater
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True  # Mark as swapped
            
            if not swapped:  # If no swaps occurred, array is already sorted
                break

# Example usage:
sol = Solution()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends