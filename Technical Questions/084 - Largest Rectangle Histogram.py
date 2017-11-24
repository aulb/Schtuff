# https://www.youtube.com/watch?v=ZmnqCZp9bBs
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # max_area = 0
        # # Stack index
        # stack = []
        # for index, height in enumerate(heights):
        #     # Add to stack if height == heights @ top of stack 
        #     # Or if empty
        #     if (stack and heights[stack[-1]] <= height) or not stack:
        #         stack.append(index)
        #     else:
        #         # While the height of the element at the top of stack is greater
        #         # Or we are at the end
        #         while stack and (heights[stack[-1]] > height or index == len(heights) - 1):
        #             top = stack.pop()

        #             area = heights[top]
        #             if stack:
        #                 area = heights[top] * (index - stack[-1] - 1)
        #             max_area = max(area, max_area)

        # return max_area
