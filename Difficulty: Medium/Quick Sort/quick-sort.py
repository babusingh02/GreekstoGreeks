#User function Template for python3
class Solution:
    # Function to sort a list using the quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partitioning index
            pi = self.partition(arr, low, high)
            
            # Recursively sorting the left and right subarrays
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
    
    # Function to partition the array
    def partition(self, arr, low, high):
        pivot = arr[high]  # Choosing the last element as pivot
        i = low - 1  # Index for smaller element
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
        return i + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().split()))
        n = len(arr)
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        print("~")

# } Driver Code Ends