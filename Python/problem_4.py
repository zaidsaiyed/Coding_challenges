'''
Difficulty: Hard
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

class Solution():
    
    def missing_pos_int(self, nums):
        
        lenght = len(nums)    
        for i in range(lenght):
            while 1 <= nums[i] <= lenght and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(lenght):
            if nums[i] != i + 1:
                return i + 1

        return lenght + 1
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.missing_pos_int([3, 4, -1, 1]))

'''
Time Complexity: O(n) 
Space Complexity: O(1)
'''
