# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:41:00 2023

@author: 90545
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=[]; i=0
        while i<len(word1) and i<len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i+=1
        while i<len(word1):
            result.append(word1[i])
            i+=1
        while i<len(word2):
            result.append(word2[i])
            i+=1
        
        return "".join(result)