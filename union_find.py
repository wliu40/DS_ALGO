# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:25:33 2019

@author: cgyy2
"""


class UF(object):
    def __init__(self, N):
        self.parent = {i:i for i in range(N)}
        self.size = {i:1 for i in range(N)}
        self.count = N
#        
#    def find(self, val):
#        if self.parent[val] != val:
#            self.parent[val] = self.find(self.parent[val])
#        return self.parent[val]

    def find(self, val):
        while val != self.parent[val]:
            val = self.parent[self.parent[val]]
        return val
    
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
#        if px != py:
#            self.parent[px] = py
        
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1
#%%
uf = UF(10)

uf.union(1,2)
uf.union(2,3)
uf.union(1,4)
uf.union(2,5)
uf.union(0,4)

uf.union(6,7)
uf.union(7,8)
#%%
uf.count

for i in range(10):
    print uf.find(i)
    
    



#%%
dic = {}
dic['a'] = ['b', 'c']
dic['b'] = ['e', 'd']
dic['e'] = ['d']

dic['c'] = ['d']


start = 'a'
end = 'd'
tmp = ['']
def foo(dic, start, end, tmp):
    if start == end:
        print tmp
        return
    for i in dic[start]:
        tmp.append(i)
        foo(dic, i, end, tmp)
        tmp.pop()
        
foo(dic, start, end, ['a'])

#%%
import hashlib
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

