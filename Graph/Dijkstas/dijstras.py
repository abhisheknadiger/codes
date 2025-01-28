
import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        AL = {}
        for u,v,w in B:
            if u not in AL:
                AL[u] = [(v,w)]
            else:
                AL[u].append((v,w))
           
            if v not in AL:
                AL[v] = [(u,w)]
            else:
                AL[v].append((u,w))
       
        min_heap = []
        distances = [float("inf") for _ in range(A)]
        distances[C] = 0
        heapq.heappush(min_heap, (0,C)) #w,v
        while min_heap:
            dist, node = heapq.heappop(min_heap)

            for neigh, w in AL.get(node, []):
                ndist = dist+w
                if distances[neigh]>ndist:
                    distances[neigh] = ndist
                    heapq.heappush(min_heap, (ndist, neigh))
       
        distances = [-1 if dist==float("inf") else dist for dist in distances]
        return distances
           