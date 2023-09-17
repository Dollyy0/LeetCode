class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        array_length = len(nums)
        found = False

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                
                if nums[i] + nums[j] == target:
                    found = True
                    ans.append(i)
                    ans.append(j)
                    break
            if found == True:
                break
        if found == False:
            print ("not found")
        return ans


        