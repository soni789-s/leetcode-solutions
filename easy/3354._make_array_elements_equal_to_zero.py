class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                ans += self.simulate(nums, i, 'left')
                ans += self.simulate(nums, i, 'right')

        return ans

    def simulate(self, nums, start, direction):
        temp = nums[:]  
        idx = start
        direc = direction

        while 0 <= idx < len(temp):
            if temp[idx] == 0:
                if direc == 'left':
                    idx -= 1
                else:
                    idx += 1
            else:
                temp[idx] -= 1
                if direc == 'left':
                    direc = 'right'
                    idx += 1
                else:
                    direc = 'left'
                    idx -= 1

        return 1 if all(x == 0 for x in temp) else 0
