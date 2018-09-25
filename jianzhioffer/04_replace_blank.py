# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:10:42 2018

@author: 10144678
"""
'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution(object):
    def replaceSpaceByAppend(self, s):
        """s使用append 事假复杂度为O(n),现行事假年内
        """
        string = list(s)
        string_replace = []
        for c in string:
            if c == ' ':
                string_replace.append('%')
                string_replace.append('2')
                string_replace.append('0')
            else:
                string_replace.append(c)
        return "".join(string_replace)

    def replaceSpace1(self, s):
        """使用新的字符串进行替换
        """
        if type(s) != str:
            return
        tmpstr = ""
        for c in s:
            if c == ' ':
                tmpstr += "%20"
            else:
                tmpstr += c
        return tmpstr
        
    def replaceSpace2(self, s):
        """在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
        """
        if type(s) != str:
            return
        return s.replace(' ', '%20')
    
    def replaceSpace3(self, s):
        if not isinstance(s, str) or len(s) < 1 or s == None:
            return ""
        
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1
        newStrlen = len(s)+spaceNum*2
        newStr = newStrlen * [None]
        indexOfOriginal, indexOfNew = len(s)-1, newStrlen-1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -=1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return "".join(newStr)
        
s = 'we are happy'

test = Solution()
print(test.replaceSpaceByAppend(s))
print(test.replaceSpace1(s))
print(test.replaceSpace2(s))
print(test.replaceSpace3(s))