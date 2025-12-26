arr=[1,2,3,4]
count=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        count+=1
        print(arr[i:j+1])

print(count)