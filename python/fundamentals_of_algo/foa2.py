def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
def qs(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        qs(arr,low,pi-1)
        qs(arr,pi+1,high)
arr=['ram','ameya','steve','james']
n = len(arr)
qs(arr,0,n-1)
print("Sorted array is: ")
for i in range(n):
    print("%s"%arr[i])
