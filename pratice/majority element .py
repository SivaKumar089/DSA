def majorityElement(arr):
        cantidate=None
        count=0

        for num in arr:
            if count== 0:
                cantidate=num
            
            if num==cantidate:
                count+=1
            else:
                count-=1
        
        return cantidate



arr=[2,2,1,1,1,1,2,2]
print(majorityElement(arr))
