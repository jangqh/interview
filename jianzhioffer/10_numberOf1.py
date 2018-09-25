# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:59:38 2018

@author: 10144678
"""

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    
    def NumberOf1_a(self, n):
        """右移，负数出错
        """
        count = 0
        while(n):
            if n & 1:
                count += 1
            n = n >> 1
        return count
    
    def NumberOf1_b(self, n):
        """
        """
        count = 0
        flag = 1
        while flag:
            if(n & flag):
                count += 1
            flag = flag << 1
        return count
        
    def NumberOf1_c(self, n):
        """用一个数-1位与这个数，相当于把这个数的最右边的1变成0，当所有位的1都为0时，计数
        """
        count = 0 
        if n < 0:
            n = n & 0xfffffffff
        
        while n:
            count += 1
            n = (n-1) & n
        return count
    
    def NumberOf1_d(self, n):
        if n < 0:
            s = bin(n & 0xfffffff)
        else:
            s = bin(s)
        return s.count('1')
    
    def powerOf2(self, n):
        """判断一个数是不是2的整数次幂
        """
        if n&(n-1) == 0:
            return True
        else:
            return False
    
    def andOr(self,m, n):
        """判断两个数的二进制表示有多少位不同
        直接比较为禁止的异或
        """
        different = m^n
        count = 0
        while different:
            count += 1
            different = different & (different - 1)
        return count


    
s = Solution()
print(s.NumberOf1_d(-7))
print(s.powerOf2(64))
print(s.andOr(10, 13))