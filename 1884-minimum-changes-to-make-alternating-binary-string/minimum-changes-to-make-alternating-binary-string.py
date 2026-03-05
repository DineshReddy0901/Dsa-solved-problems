class Solution(object):
    def minOperations(self, s):
                n = len(s)
                start_with_0 = 0
                start_with_1 = 0
                for i in range(len(s)):
                    expected_0 = '0' if i%2 ==0 else '1'
                    expected_1 = '1' if i%2 == 0 else '0'

                    if s[i]!= expected_0:
                       start_with_0 +=1
                    if s[i]!= expected_1:
                       start_with_1 +=1
                return min(start_with_0,start_with_1)              




        