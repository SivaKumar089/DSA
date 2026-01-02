
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        insert_index=i
        current_value=arr.pop(i)

        for j in range(i-1,-1,-1):
            if arr[j]>current_value:
                insert_index=j
        arr.insert(insert_index,current_value)
    return arr

arr=[5,4,3,2,1]
print(insertion_sort(arr))