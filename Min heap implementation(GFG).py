class minHeap:
    
    def __init__(self):
        # Initialize your data members
        self.arr=[]
        self.count=0
        
    def heapifyUp(self,arr,ind):
        if(ind>0):
            parent=(ind-1)//2
            if(arr[ind]<arr[parent]):
                arr[ind],arr[parent]=arr[parent],arr[ind]
                self.heapifyUp(arr,parent)
    def heapifyDown(self,arr,ind):
        smallest=ind
        lchild=2*ind+1
        rchild=2*ind+2
        if(lchild<self.count and arr[lchild]<arr[smallest]):
            smallest=lchild
        if(rchild<self.count and arr[rchild]<arr[smallest]):
            smallest=rchild
        if(smallest!=ind):
            arr[smallest],arr[ind]=arr[ind],arr[smallest]
            self.heapifyDown(arr,smallest)
            
    # Insert x into the heap
    def push(self, x: int):
        # code here
        self.arr.append(x)
        self.heapifyUp(self.arr,self.count)
        self.count+=1

    # Remove the top (minimum) element
    def pop(self):
        # code here
        self.arr[0],self.arr[self.count-1]=self.arr[self.count-1],self.arr[0]
        self.arr.pop()
        self.count-=1
        self.heapifyDown(self.arr,0)
        
    # Return the top element or -1 if empty
    def peek(self) -> int:
        # code here
        if(self.count==0):
            return -1
        return self.arr[0]

    # Return the number of elements in the heap
    def size(self) -> int:
        return self.count
        
