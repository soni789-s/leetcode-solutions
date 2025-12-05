class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[]
        prefix.append(nums[0])
        for i in range(1,n):
            prefix.append(prefix[-1]+nums[i])
        result=0
        for i in range(1,n):
            left=prefix[i]-nums[i]
            right=prefix[n-1]-prefix[i-1]
            if abs(left-right)%2==0:
                result+=1
        return result