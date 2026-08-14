class Solution(object):
    def maxArea(self, height):
       left = 0
       max_water = 0
       right = len(height)-1
       while left <right:
          width = right-left
          ht = min(height[left],height[right])
          sub_max_water = width*ht 
          max_water = max(max_water,sub_max_water)

          if height[left] > height[right]:
                right-=1
          else:
                left +=1
       return max_water

       
             
        