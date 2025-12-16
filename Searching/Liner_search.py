


def linear_search(arr, data):
    i = 0
    n = len(arr)

    while i < n:
        if arr[i] == data:
            return i
        i += 1
    
    return -1


arr=[1,2,3,4,5]
    

print(linear_search(arr,6))
        


