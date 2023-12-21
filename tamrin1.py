def my_sort(arr,l,h):
    if l>h:
        return
    
    #if first element is bigger than last,swap them
    if arr[l]>arr[h]:
        arr[l],arr[h]=arr[h],arr[l]

    #if there are more than 2 elements in the array
    if h-l+1>2:
        t=(int)((h-l+1)/3)

        my_sort(arr,l,(h-t))

        my_sort(arr,l+t,(h))

        my_sort(arr,l,(h-t))

arr=[2,4,5,3,1]
n=len(arr)
my_sort(arr,0,n-1)

for i in range(0,n):
    print(arr[i],end='   ')