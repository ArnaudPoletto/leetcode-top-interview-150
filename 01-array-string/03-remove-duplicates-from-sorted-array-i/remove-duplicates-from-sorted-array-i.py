class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        set_idx = 0
        curr = 0
        old_val = None

        len_nums = len(nums) 
        while curr < len_nums:
            curr_val = nums[curr]
            if old_val != curr_val:
                nums[set_idx] = curr_val
                set_idx += 1
                old_val = curr_val
            curr += 1

        return set_idx






