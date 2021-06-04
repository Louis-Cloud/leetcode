class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)

        max_hor = horizontalCuts[0]
        max_vert = verticalCuts[0]

        for i in range(len(horizontalCuts) - 1):
            cut_length = horizontalCuts[i + 1] - horizontalCuts[i]
            max_hor = max(max_hor, cut_length)

        for i in range(len(verticalCuts) - 1):
            cut_length = verticalCuts[i + 1] - verticalCuts[i]
            max_vert = max(max_vert, cut_length)

        return (max_hor * max_vert) % (10**9 + 7)