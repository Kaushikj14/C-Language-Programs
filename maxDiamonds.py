def maxDiamonds(self, A, N, K):
        # code here 
        res=[]
        
        A.sort(reverse=True)
        
        heapq.heappush(res,-A[0])
        
        k=K
        ans=0
        i=1
        while len(res)>0 and k:
            a = -heapq.heappop(res)
            ans+=a
            heapq.heappush(res,-(a//2))
            
            if i<N:
                heapq.heappush(res,-A[i])
                i+=1
            k-=1
            
        return ans
