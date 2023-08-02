class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        set_idx = 0
        curr = 0

        memory = [None, None, None]

        nums_len = len(nums)
        while curr < nums_len:
            if memory[0] != memory[1] or memory[1] != memory[2]:
                nums[set_idx] = nums[curr]
                set_idx += 1
            # Shift memory
            memory[0:2] = memory[1:3]
            memory[2] = nums[curr]
            # Go through the entire list
            curr += 1
            print(memory, nums)

        return set_idx

