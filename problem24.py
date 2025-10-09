from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans

# Time Complexity: O(n!)
# Space Complexity: O(n)

s = Solution()
myList = s.permute([0,1,2,3,4,5,6,7,8,9])

print(myList[999999])
2783915460