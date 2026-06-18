class Solution(object):
    def combinationSum(self, candidates, target):
        path = []
        def backtracking(start,present,target):
            if target ==0:
                path.append(present[:])
                return
            if target<0:
                return
            for i in range(start,len(candidates)):
                present.append(candidates[i])
                backtracking(i,present,target-candidates[i])
                present.pop()
        backtracking(0,[],target)
        return path


        