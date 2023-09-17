class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize a variable to keep track of the non-equal elements count
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k