
def sum_of_sub_array(arr,d,m):
    sum =0
    n=len(arr)
    count=0

    for i in range(m):
        sum+=arr[i]

    if sum== d:
        count+=1

    for i in range(m,n):
        sum+=arr[i]
        sum-=arr[i-m]

        if sum== d:
            count+=1
    return count            


arr=[1,2,1,3,4,2,1]
d=3
m=2
print(sum_of_sub_array(arr,d,m))