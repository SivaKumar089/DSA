

def Selection_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
            arr.insert(i,arr.pop(min_index))    
    return arr

arr=[5,4,3,2,1]

print(Selection_sort(arr))