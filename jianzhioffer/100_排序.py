# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:37:13 2018

@author: 10144678
"""
"""
https://www.cnblogs.com/onepixel/articles/7674659.html
https://www.cnblogs.com/MrFiona/p/5978491.html
积累排序算法：
1.插入排序: 希尔排序、插入排序
2.选择排序：简单选择排序、堆排序
3.交换排序：冒泡排序、快速排序
4.并归排序：二路归并排序、多路归并排序
5：线性时间非比较类排序：基数排序、桶排序
"""
import random

class Sorting:
    def shell_sort(self, lists):
        count = len(lists)
        step = 2
        group = count / step
        while group > 0:
            for i in range(group):
                j = i + group
                while j < count:
                    k = j - group
                    key = lists[j]
                    while k >= 0:
                        if lists[k] > key:
                            lists[k + group] = lists[k]
                            lists[k] = key
                        k -= group
                    j += group
            group /= step
        return lists
        
    def insertSort(self, lst):
        """插入排序:
           1. 从第一个元素开始，该元素可以认为已经被排序；
           2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
           3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
           4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
           5. 将新元素插入到该位置后.
        """
        count = len(lst)
        for i in range(1, count):
            key = lst[i]  # 取下一个元素，从第二个开始，到结尾
            j = i-1
            while j >= 0:
                if lst[j] > key:
                    lst[j+1] = lst[j]
                    lst[j] = key
                j -=1
        return lst
                
    def bubbleSort(self, lst):
        """冒泡排序：
        1.比较相邻元素，如果第一个比第二个大，就交换
        """
        count = len(lst)
        for i in range(count):
            for j in range(i+1, count):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
        
    def selectSort(self, lst):
        """选择排序：
        首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        然后，再从剩余未排序元素中继续寻找最小（大）元素，
        然后放到已排序序列的末尾。
        """
        count = len(lst)
        for i in range(count):
            min = i
            for j in range(i+1, count):
                if lst[min] > lst[j]:
                    min = j
            lst[min], lst[i] = lst[i], lst[min]
        return lst
        
        
    def quickSort(self,lst, left, right):
        """快速排序：
        基准，分区，递归
        """
        if left >= right:
            return lst
        key = lst[left]
        low = left
        high = right
        while left < right:
            while left < right and lst[right] >= key:
                right -= 1
            while left < right and lst[left] <= key:
                left += 1
            lst[left], lst[right] = lst[right], lst[left]
        lst[right] = key
        self.quickSort(lst, low, left-1)
        self.quickSort(lst, left+1, high)
        return lst
        
###########################################################
    def merge(self, left, right):
        """合并
        """
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
#        print("left:", left, "right:",right,"result:", result)
        return result

    def mergeSort(self, lst):
        """归并排序：
        """
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.mergeSort(lst[:mid])
        right = self.mergeSort(lst[mid:])
        return self.merge(left, right)

#################################################
    def adjustHeap(self, lst, i, size):
        """
        """
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < size // 2:
            if lchild < size and lst[lchild] > lst[max]:
                max = lchild
            if rchild < size and lst[rchild] > lst[max]:
                max = rchild
            if max != i:
                lst[max], lst[i] = lst[i], lst[max]
                self.adjustHeap(lst, max, size)
    
    def buildHeap(self, lst, size):
        """创建堆
        """
        for i in range(0, (size//2))[::-1]:
            self.adjustHeap(lst, i, size)


    def heapSort(self, lst):
        """堆排序：
        1.将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
        2.将堆顶元素R[1]与最后一个元素R[n]交换，
        此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
        3.由于交换后新的堆顶R[1]可能违反堆的性质，
        因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，
        然后再次将R[1]与无序区最后一个元素交换，
        得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。
        """
        size = len(lst)
        self.buildHeap(lst, size)
        for i in range(0, size)[::-1]:
            lst[0], lst[i] = lst[i], lst[0]
            self.adjustHeap(lst, 0, i)
        return lst

#############################################################
    def adjust_heap(self, lists, i, size):
        """调整堆
        """
        lchild = 2 * i + 1
        rchild = 2 * i + 2     
        max = i
        if i < size / 2:
            if lchild < size and lists[lchild] > lists[max]:
                max = lchild
            if rchild < size and lists[rchild] > lists[max]:
                max = rchild
            if max != i:
                lists[max], lists[i] = lists[i], lists[max]
                self.adjust_heap(lists, max, size)
 
    def build_heap(self, lists, size):
        """创建堆
        """
        for i in range(0, (size//2))[::-1]:
            print(i)
            self.adjust_heap(lists, i, size) 

    def heap_sort(self, lists):
        """堆排序
        """
        size = len(lists)
        self.build_heap(lists, size)
        for i in range(0, size)[::-1]:
            lists[0], lists[i] = lists[i], lists[0]
            self.adjust_heap(lists, 0, i)
        return lst
##########################################################################
if __name__ == '__main__':
#    lst1 = input().split()
#    lst11 = [int(i) for i in lst1]
    lst = [6,1,2,7,9,3,4,5,11,8]
    lst = [random.randint(0, 100) for _ in range(10)]
    print(lst)
    s = Sorting()
    # 插入排序
    r1 = s.insertSort(lst)
#    r2 = s.shell_sort(lst)
    r3 = s.bubbleSort(lst)
    r4 = s.quickSort(lst, 0, len(lst)-1)
    r5 = s.mergeSort(lst)
    r6 = s.heapSort(lst)
    r7 = s.heap_sort(lst)
    print(r6)
    
