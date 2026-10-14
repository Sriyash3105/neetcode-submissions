class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0
        for i,h in enumerate(heights):
            while stack and (heights[stack[-1]] > h):
                past_index = stack.pop()
                height = heights[past_index] 
                if stack :
                    width = i - stack[-1]-1
                else:
                    width = i    
               
                maxArea = max(maxArea,height*width)
            stack.append(i)
        while stack:
            past_index = stack.pop()
            height = heights[past_index]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1
            maxArea = max(maxArea, height * width) 
        return maxArea           
