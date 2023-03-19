def split(arr):
    return(arr[:len(arr)//2],arr[len(arr)//2:])
def merge(left,right):
    li=0
    ri=0
    result=[]
    while li<len(left) and ri<len(right):
        if left[li]<=right[ri]:
            result.append(left[li])
            li+=1
        else:
            result.append(right[ri])
            ri+=1
    if(li<len(left)):
        result.extend(left[li:])
    elif (ri<len(right)):
        result.extend(right[ri:])
    return result
def mergesort(arr):
    if arr is None:
        return None
    if len(arr)<2:
        return arr
    left,right=split(arr)
    return merge(mergesort(left),mergesort(right))
nums=[45,65,69,3,20,73]
print(mergesort(nums))
        
