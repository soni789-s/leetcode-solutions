class Solution:
    def totalMoney(self, n: int) -> int:
        remaining_days=n%7
        weeks=n//7
        result=0
        end_day=7
        for start in range(weeks):
            total_sum=(end_day*(end_day+1))//2 - (start*(start+1))//2
            result+=total_sum
            end_day+=1
        
        start_value = weeks + 1
        for i in range(remaining_days):
            result += start_value + i

        return result