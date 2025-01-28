class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B): 
        C = {}
        for i in B:
            if i[0] in C:
                C[i[0]].append(i[1])
            else:
                C[i[0]] = [i[1]]

        q = [B[0][0]]
        v = [] 
        while q:
            cur = q.pop()
            v.append(cur)
            for i in C.get(cur, []):
                if i in v:
                    return 1 
                q.append(i)
            

        return 0


Solution().solve(5, [[1,4],[2,1],[4,3],[4,5],[2,3],[2,4],[1,5],[5,3],[2,5],[5,1],[4,2],[3,1],[5,4],[3,4],[1,3],[4,1],[3,5],[3,2],[5,2]])