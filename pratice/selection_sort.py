

def selection_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        min_value=arr.pop(min_index)
        arr.insert(i,min_value)
    return arr



arr=[5,4,3,2,1]

print(selection_sort(arr))