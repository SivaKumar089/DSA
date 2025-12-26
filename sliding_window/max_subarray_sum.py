def max_subarray(arr):
    max_sum = arr[0]
    current = 0
    
    for num in arr:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum =", max_subarray(arr))
