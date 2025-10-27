class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count_ones=[]
        for string in bank:
            count=0
            for letter in string:
                if letter=='1':
                    count+=1
            if count!=0:
                count_ones.append(count)
        result=0
        for i in range(1,len(count_ones)):
            result+=(count_ones[i-1]*count_ones[i])
        return result
        