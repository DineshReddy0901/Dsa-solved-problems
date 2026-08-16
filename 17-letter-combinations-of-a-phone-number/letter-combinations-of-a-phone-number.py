class Solution(object):
    def letterCombinations(self, digits):
        Hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        res = []

        def backtracking(index, current):
            if index == len(digits):
                res.append("".join(current))
                return

            letters = Hashmap[digits[index]]

            for letter in letters:
                current.append(letter)
                backtracking(index + 1, current)
                current.pop()

        backtracking(0, [])
        return res
        # res = []
        # def backtracking(index,current):
        #     if index == len(digits):
        #         res.append("".join(current))
        #         return
            
        #     letters = Hashmap[digits[index]]

        #     for letter in letters:
        #         current.append(letter)
        #         backtracking(index+1,current)

        #         current.pop()
        # backtracking(0, [])
        # return res



     