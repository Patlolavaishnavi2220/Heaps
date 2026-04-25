from os import *
from sys import *
from collections import *
from math import *

def buildHeap(arr, n):
    def heapifyDown(arr,ind):
        largest=ind
        lchild=2*ind+1
        rchild=2*ind+2
        if(lchild<n and arr[lchild]>arr[largest]):
            largest=lchild
        if(rchild<n and arr[rchild]>arr[largest]):
            largest=rchild
        if(ind!=largest):
            arr[largest],arr[ind]=arr[ind],arr[largest]
            heapifyDown(arr,largest)
    for ind in range(n//2-1,-1,-1):
        heapifyDown(arr,ind)
    return arr
        
