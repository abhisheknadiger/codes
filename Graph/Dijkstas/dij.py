import sys 
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def returnminIndex(self, A, v):

        mini = 0
        while mini < len(A):
            if A[mini] != sys.maxsize and not v[mini]:
                break
            mini += 1
        if mini == len(A):
            return 
        for i in range(1, len(A)):
            if A[mini] > A[i] and not v[i]:
                mini = i 
        return mini
    
    def solve(self, A, B, C):
        import sys 
        d = [sys.maxsize for i in range(A)]
        v = [False for i in range(A)]

        d[C] = 0
        D = {}
        for i in B:
            if i[0] in D:
                D[i[0]].append((i[1], i[2]))
            else:
                D[i[0]] = [(i[1], i[2])]
            if i[1] in D:
                D[i[1]].append((i[0], i[2]))
            else:
                D[i[1]] = [(i[0], i[2])]
        
        st = C
        while True:
            if not st:
                break
            v[st] = True 
            for i in D.get(st, []):
                if v[i[0]]:
                    continue
                if d[i[0]] > d[st] + i[1]:
                    d[i[0]] = d[st] + i[1]
            st = self.returnminIndex(d, v)

        for i in range(len(d)):
            if d[i] >= sys.maxsize:
                d[i] = -1

        return d


Solution().solve(8,[[0,2,4],[1,2,10],[5,7,4],[2,3,6],[3,7,2],[0,5,2]],7)