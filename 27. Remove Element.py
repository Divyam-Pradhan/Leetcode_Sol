class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pntr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pntr] = nums[i]
                pntr +=1
        return pntr
