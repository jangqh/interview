# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:06:11 2018

@author: 10144678
"""

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

1.开始，中间和结束都相等的话只能顺序查找
2.如果中间大于开始，说明，前面是递增的，所以查找后半部分
3.如果中间小于开始，说明，前面是包含最小值的
4.使用while
"""

class Solution:
    def minNumberInRotateArray(self, array):
        if len(array) == 0:
            return 0
        front, rear = 0, len(array)-1
        mid_index = 0
        while array[front] >= array[rear]:
            if rear - front == 1:
                mid_index = rear
                return
            mid_index = (front + rear) // 2
            if array[front] == array[rear] and array[front] == array[mid_index]:
                # 顺序查找
                result = array[0]
                for i in array[front:rear+1]:
                    if i < result:
                        result = i
                return result
                
            if array[mid_index] >= array[front]:
                front = mid_index
            elif array[mid_index] <= array[front]:
                rear = mid_index
        return array[mid_index]
        

Test  = Solution()
array1 = [3,4,5,6,7,1,2,3]
array2 = [1,2,3,4,5,6]
array3 = [1,1,1,0,1]
array4 = [1,0,1,1,1,1]
print(Test.minNumberInRotateArray(array1))
print(Test.minNumberInRotateArray(array2))
print(Test.minNumberInRotateArray(array3))
print(Test.minNumberInRotateArray(array4))
