def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    leftHalf=arr[:mid]
    righthalf=arr[mid:]


    leftSort=merge_sort(leftHalf)
    rightSort=merge_sort(righthalf)

    return merge(leftSort,rightSort)


def merge(left,right):
    
    result=[]
    i=j=0

    while i< len(left) and j< len(right):
        if left[i] <right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr=[5,4,3,2,1]

print(merge_sort(arr))
