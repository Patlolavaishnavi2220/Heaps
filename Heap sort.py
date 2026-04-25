class Solution:
    def heapSort(self, arr):
        #code here
        def heapifyDown(arr,ind,n):
            largest=ind
            lchild=2*ind+1
            rchild=2*ind+2
            if(lchild<n and arr[lchild]>arr[largest]):
                largest=lchild
            if(rchild<n and arr[rchild]>arr[largest]):
                largest=rchild
            if(largest!=ind):
                arr[largest],arr[ind]=arr[ind],arr[largest]
                heapifyDown(arr,largest,n)
        n=len(arr) #n is nothing but array "size"
        #step 1:- convert array to max heap
        for ind in range(n//2,-1,-1): 
            heapifyDown(arr,ind,n)
        #step 2:- 
        last=n-1
        while(last>0):
            arr[0],arr[last]=arr[last],arr[0]
            last-=1
            if(last>0):
                heapifyDown(arr,0,last+1)
        return arr
            
            
