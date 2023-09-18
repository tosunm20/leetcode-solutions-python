# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:46:15 2023

@author: 90545
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2 + str1): return ""
        else: return ( str1[:gcd( len(str1), len(str2) )] )