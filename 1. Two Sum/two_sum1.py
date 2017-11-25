# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:52:16 2017

@author: pyriseup
"""

class Solution:
    def twoSum(self, nums, target):
        """
        遍历nums，每次迭代时将当前迭代出的数值的索引保存到一个字典中，
        并使用target与当前数值的差作为字典的key，如果在之后的迭代过程
        中发现迭代出的数值已存在于字典中，便找到了匹配的答案。
        """
        dic = {}
        for i,j in enumerate(nums):
            if j in dic:
                return [dic[j], i]
            else:
                dic[target - j] = i
        return [-1, -1]