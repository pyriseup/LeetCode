# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:52:16 2017

@author: pyriseup
"""

class Solution:
    def twoSum(self, nums, target):
        """
        用嵌套列表解析遍历nums,查找出所有符合条件的结果，并返回第一个结果。
        这个方法可以只用一行代码写出，但执行效率会低很多。
        """
        return [[i,j+i+1] for i,x in enumerate(nums) for j,y in enumerate(nums[i+1:]) if x+y==target][0]