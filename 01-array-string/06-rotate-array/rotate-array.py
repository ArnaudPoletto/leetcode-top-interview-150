import math

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # SOLUTION 1: O(1) space
        nums_len = len(nums)
        k = k % nums_len

        if k == 0:
            return
        
        iter_len = nums_len // math.gcd(nums_len, k)
        iter_num = nums_len // iter_len

        for i in range(0, iter_num):
            curr = i
            curr_value = nums[i]
            for _ in range(iter_len):
                next_curr = (curr + k) % nums_len
                next_curr_value = nums[next_curr]
                nums[next_curr] = curr_value
                curr_value = next_curr_value
                curr = next_curr

        # SOLUTION 2: O(n) space
        """
        nums_len = len(nums)
        k = k % nums_len
        nums[::] = nums[nums_len-k:] + nums[0:nums_len-k]
        """