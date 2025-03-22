
class Solution:
    def peakElement(self, arr):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return mid
            
            # If the left neighbor is greater, then the peak lies on the left side
            if mid > 0 and arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:  # Otherwise, the peak lies on the right side
                left = mid + 1
        
        return -1  # This line should never be reached due to the problem constraints





#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends