class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV, l, r = 0, 0, len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                vol = heights[l] * (r - l)
                l += 1
            else:
                vol = heights[r] * (r - l)
                r -= 1
            maxV = max(vol, maxV)

        return maxV
            