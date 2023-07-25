'''
Difficulty: Easy

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [15, 10, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

class Solution():
    
    def sum(self, list, k):
        
        seen = set()
        for num in list:
            if (k - num) in seen:
                return True
            else:
                seen.add(num)
        return False
    
if __name__ == "__main__":
    sol = Solution()
    list = [15, 10, 3, 7]
    k = 17
    print(sol.sum(list, k))
    
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''