def heapifDown(arr,index):
    smallest=index
    lchild=2*index+1
    rchild=2*index+2
    if(lchild<len(arr) and arr[lchild]<arr[smallest]):
        smallest=lchild
    if(rchild<len(arr) and arr[rchild]<arr[smallest]):
        smallest=rchild
    if(smallest!=index):
        arr[index],arr[smallest]=arr[smallest],arr[index]
        heapifDown(arr,smallest)
def heapifUp(arr,index):
    if(index>0):
        parent=(index-1)//2
        if(arr[index]<arr[parent]):
            arr[index],arr[parent]=arr[parent],arr[index]
            heapifUp(arr,parent)
arr=[1,4,5,6,7,10,6,8]
t=int(input("enter number of Queries"))
for _ in range(t):
    index,val=map(int,input().split())
    if(arr[index]>val):
        arr[index]=val
        heapifUp(arr,index)
    elif(arr[index]<val):
        arr[index]=val
        heapifDown(arr,index)
print(arr)
        
