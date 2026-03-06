import pandas as pd
dict_= {"a":1,"b":{"d":3,"e":5}}

#op {a:1, b.d:3, b.e:5}

# res = {}


# # import pandas as pd

# d = pd.json_normalize(dict_)
# print(d.to_dict(orient='records')[0])
# {'a': 1, 'b.d': 3, 'b.e': 5}  


# sortcolors
# class Solution:
#     def sortColors(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         dict_ = {}

#         for color in nums :
#             if color not in dict_:
#                 dict_[color] = 0
#             dict_[color] += 1
        
#         idx = 0
#         for color in range(3):
#             freq = dict_.get(color, 0)
#             nums[idx : idx + freq] = [color] * freq
#             idx += freq
#         return nums

# ans = Solution()
# print(ans.sortColors([2,0,2,1,1,0]))

# a = [1,2,3,4]
# a[0:3] = [1]*3
# print(a)

#pascals triange

class Solution:
    def pascals_triangle(self , numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res

ans = Solution()
print(ans.pascals_triangle(5))
        