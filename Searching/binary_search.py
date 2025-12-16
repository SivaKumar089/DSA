def binary_search(arr, data):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == data:
            return mid
        elif arr[mid] > data:
            right = mid - 1
        else:
            left = mid + 1

    return -1
            

arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 5))
