class Solution(object):
    def selfDividingNumbers(self, left, right):
        
        def Selfdivide(number):
             n = number
             while n:
                digit = n%10
                if digit==0 or number % digit!=0:
                    return False
                n//=10
             return True

        res = []
        for number in range(left,right+1):
            if Selfdivide(number):
                res.append(number)
        
        return res