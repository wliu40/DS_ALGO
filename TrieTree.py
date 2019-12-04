# -*- coding: utf-8 -*-
"""
Created on Wed Oct 09 11:53:12 2019

@author: cgyy2
"""

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isend=False
        
class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        cur.isend = True
        
    def is_prefix(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
       
    def search_word(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.isend
    
#%%
words = ['abc', 'abcd', 'aed', 'a', 'xy', 'xyz']

tt = TrieTree()

for w in words:
    tt.insert(w)
    
tt.is_prefix("ab")
tt.is_prefix("abd")
tt.search_word("xyz")
tt.search_word("xy")



    