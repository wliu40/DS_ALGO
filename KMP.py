# -*- coding: utf-8 -*-
"""
Created on Wed Oct 09 11:38:54 2019

@author: cgyy2
"""

# compute the longest prefix-suffix array
def get_LPS(s):
    arr = [0] * (len(s)+1)
    for j in range(1, len(s)):
#        print 'j=',j
        k = arr[j]
#        print 'set k to ', arr[j]
        while (k and s[j] != s[k]):
            k = arr[k]
            
        if s[j] == s[k]:
            arr[j+1] = k+1
        else:
            arr[j+1] = 0
#        print 'update arr[j+1] ', arr[j+1]
#        print
    return arr
#%%
s = 'aaabcaaabcdeaaa'

p = get_LPS(s)[1:]
#      a  a  a  b  c  a  a  a  b  c  d  e  a  a  a
# p = [0, 1, 2, 0, 0, 1, 2, 3, 4, 5, 0, 0, 1, 2, 3]

s = 'abcdeabc'

p = get_LPS(s)[1:]

#      a  b  c  d  e  a  b  c
# p = [0, 0, 0, 0, 0, 1, 2, 3]

#%%

def find_substrs(s1, s2):
    p = get_LPS(s2)[1:]
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        if j == len(s2):
            print 'found the substr at {}'.format(i-j)
            print s1[i-j:]
            j = p[j-1]
        elif i < len(s1) and s1[i] != s2[j]:
            if j != 0:
                j = p[j-1]
            else:
                i += 1
#%%
s1 = 'abcxabcdeabxabcdabcexabcdabcfg'                
s2 = "abcdabc"

find_substrs(s1, s2)
             