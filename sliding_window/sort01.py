
def sort01(arr):
    low=0
    high=len(arr)-1

    while low < high:
        if arr[low]==0:
            low+=1
        else:
            arr[high],arr[low]=arr[low],arr[high]
            high-=1
    return arr




arr=[0, 1, 1, 0, 1]
sort01(arr)
print(arr)