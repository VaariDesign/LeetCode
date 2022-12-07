class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_water = 0
        
        while(i < j):
            water_level = (j - i) * min(height[i], height[j])
            if max_water < water_level:
                max_water = water_level
                
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1  
        return max_water
