class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num , freq in count.items():
            heapq.heappush(heap,(-freq,num))
        res = []

        while k > 0:
            f,d = heapq.heappop(heap)
            res.append(d)
            k -=1
        
        return res


        


        