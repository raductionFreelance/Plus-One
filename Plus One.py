class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        snumbers=""
        result=[]
        for i in digits:
            k=str(i)
            snumbers += k
        numbers=int(snumbers)+1
        snumbers=str(numbers)
        for i in snumbers:
            n=int(i)
            result.append(n)
        return result
