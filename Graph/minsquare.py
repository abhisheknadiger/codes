
class Solution:


    def cnt(self, num):
        if num in self.d:
            return self.d[num]

        ways = 0
        for i in range(int(math.sqrt(num))):
            ways += (self.cnt(i*i,) + self.cnt( num - i *  i))
        return ways
    def countMinSquares(self, A):
        self.d = {0:1, 1: 1, 2: 1, 3:1, 4: 2}

        return self.cnt(A)




Solution().countMinSquares(13)


# https://www.linkedin.com/posts/im-nsk_give-me-2-minutes-i-will-tell-you-7-ways-activity-7280939088474468352-xnTY?utm_source=share&utm_medium=member_desktop