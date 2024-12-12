class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        import math
        for i in range(k):
            largest_number = max(gifts)
            index = gifts.index(largest_number)
            root_largest_number = int(math.sqrt(largest_number))
            gifts[index] = root_largest_number
        return sum(gifts)