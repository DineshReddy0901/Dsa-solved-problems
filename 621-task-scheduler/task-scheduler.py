class Solution(object):
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        countMax = list(freq.values()).count(maxFreq)
    
        return max(len(tasks), (maxFreq - 1) * (n + 1) + countMax)

        
        
        
        