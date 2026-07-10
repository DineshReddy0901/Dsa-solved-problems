class Solution(object):
    def removeKdigits(self, num, k):
       n = len(num) 
       stack = []
       for i in num:
          while stack and k>0 and stack[-1]>i:
                    stack.pop()
                    k = k-1
          else:
            stack.append(i)
       while k > 0:
          stack.pop()
          k -= 1

       ans = "".join(stack).lstrip("0")

       return ans if ans else "0"

                

       
      
        
         

