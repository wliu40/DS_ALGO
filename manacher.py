# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:13:10 2019

@author: cgyy2
"""



a = "abacabac"
"""

    a b a c a b a c
    0 1 0 3 0 2 0 0 

"""
def convert(s):
    res = ""
    for i in s:
        res += '#'
        res += i
    res += "#"
    return res


print convert(a)


def get_longest_palindrome(s):
    s = convert(s)
    p = [0] * len(s)
    print 'new string: ', s
    c = 0
    r = 0
    # c is the current longest palindrome' center index
    # r is the right boudnary index
    for i in range(1, len(s)-1):
        # the mirror index
        mirror = 2*c - i # c - (i-c)
        if r > i:
            p[i] = min(r-i, p[mirror])
        # update the current index
        while i+1+p[i] < len(s) and i-1-p[i] >= 0 and s[i+1+p[i]] == s[i-1-p[i]]:
            p[i] += 1
        # update the right boundary
        if i+p[i] > r:
            c = i
            r = i + p[i]
            
    return p
print get_longest_palindrome(a)

#%%