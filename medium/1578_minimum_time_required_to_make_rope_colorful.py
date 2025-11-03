class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''ans=0
        start=0
        for last in range(1,len(colors)):
            if colors[start]!=colors[last]:
                ans+=max(neededTime[start:last])
                start=last
        ans+=max(neededTime[start:])
        return sum(neededTime)-ans'''

        total_time = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total_time += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return total_time