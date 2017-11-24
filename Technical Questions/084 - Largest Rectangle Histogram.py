# https://www.youtube.com/watch?v=ZmnqCZp9bBs
# Follow up: if 0 is permitted
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        index = 0
        max_area = -1
        stack = []
        
        while index < len(heights):
            # Everytime I access something I need to make sure I can actually do it
            while stack and heights[stack[-1]] > heights[index]:
                top = stack.pop()
                if stack: max_area = max(max_area, heights[top] * (index - stack[-1] - 1))
                else: max_area = max(max_area, heights[top] * index)
            stack.append(index)
            index += 1

        while stack:
            top = stack.pop()
            if stack: max_area = max(max_area, heights[top] * (index - stack[-1] - 1))
            else: max_area = max(max_area, heights[top] * index)
            
        return max_area
