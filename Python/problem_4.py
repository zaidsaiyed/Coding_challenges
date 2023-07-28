'''
Difficulty: Hard

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

class Solution():
    
    def missing_pos_int(self, list):
        
        list.sort()
        counter = 1
        new_list = []
        for num in list:
            if num > 0 and not num in new_list:
                new_list.append(num)
                
        for i in new_list:
            if i == counter:
                counter += 1
                continue
        return counter
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.missing_pos_int([3, 4, -1, 1]))
'''
Time Complexity: O(n log n) 
Space Complexity: O(n)
'''