class Solution:
    def kthSmallest(self, nums, k):
        # Code here
        heap=[]
        n=len(nums)
        for ind in range(0,k):
            heapq.heappush(heap,-nums[ind])
        for ind in range(k,n):
            if(nums[ind]<-heap[0]):
                heapq.heappop(heap)
                heapq.heappush(heap,-nums[ind])
        return -heap[0]
        
        

