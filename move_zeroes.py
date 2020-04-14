class Solution:
    #def moveZeroes(self, nums: list[int]) -> None:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        nums_len = len(nums)
        while i < nums_len:
            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
                print(f'Popping {nums[i]} for index {i}')
                print(n)
                nums_len -= 1
            else:
                i += 1
                print('Moving on')

