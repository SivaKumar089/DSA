def quick(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[low] = arr[low], arr[j] 
    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot = quick(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr 


arr = [5, 3, 8, 4, 2, 7, 1, 10]
print(quick_sort(arr, 0, len(arr) - 1))
