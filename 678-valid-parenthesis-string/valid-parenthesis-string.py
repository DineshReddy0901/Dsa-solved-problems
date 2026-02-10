class Solution(object):
    def checkValidString(self, s):
        open_1 =0
        open_2 =0
        for char in s:
            if char == '(':
                open_1 +=1
                open_2+=1
            elif char == ')':
                open_1 -=1
                open_2 -=1
            else:
                open_1 -=1
                open_2+=1
            if open_2 < 0:
                return False
            if open_1 < 0:
                open_1 = 0
        return open_1 ==0
            










        # one_stack = []
        # two_stack = []
        # for char in enumerate(s):
        #     if char == '(':
        #         one_stack.append(char)
        #     elif char== '*':
        #         two_stack.append(i)
        #     else:
        #         if one_stack:
        #             one_stack.pop()
        #         elif two_stack:
        #             two_stack.pop()
        #         else:
        #             return False
        # return True
        # while one_stack and two_stack:
        #     if one_stack[-1]<two_stack[-1]:
        #         one_stack.pop()
        #         two_stack.pop()
        #     else:
        #         return False
        # return not open_stack

       
                
        
        

        
        

        
        