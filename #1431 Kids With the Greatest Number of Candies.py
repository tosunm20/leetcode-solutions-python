# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:45:24 2023

@author: 90545
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        myRes = []
        i=0
        maxCandies=max(candies)
        while i<len(candies):
            num = candies[i] + extraCandies
            if num>=maxCandies:
                myRes.append(True)
            elif num<candies:
                myRes.append(False)
            i+=1

        return myRes