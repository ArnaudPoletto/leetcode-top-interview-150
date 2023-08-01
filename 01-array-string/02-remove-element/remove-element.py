class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        inc_curr = 0
        nums_length = len(nums)
        dec_curr = nums_length

        while inc_curr < dec_curr:
            if nums[inc_curr] == val:
                # Find last valid element, and stop if end of valid elements
                while dec_curr >= 0 and nums[dec_curr - 1] == val:
                    dec_curr -= 1
                if inc_curr >= dec_curr:
                    break

                # Replace the last valid element with the inc_curr to be removed
                nums[inc_curr] = nums[dec_curr - 1]
                dec_curr -= 1
            inc_curr += 1

        return max(dec_curr, 0)