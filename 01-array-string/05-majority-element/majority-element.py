class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Moore Voting Algorithm
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1

        return candidate
