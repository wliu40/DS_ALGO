lambda functions
http://www.codeskulptor.org/#user43_4vGKFYRSHO_0.py
http://www.codeskulptor.org/#user43_FDuELux9kb_1.py


def reverseWords(s):
    s = s[::-1]
def reverseWords1(s):
    s.reverse()
def reverseWords2(s):
    s[:] = s[::-1]	
	
s = [1,2,3]
reverseWords(s)
print(s)

b = [4,5,6]
reverseWords1(b)
print(b)

b = [7,8,9]
reverseWords2(b)
print(b)

##set operation
>>> a = set([1,2,3])
>>> b = set([2,3,4])
>>> a&b
{2, 3}
>>> a-b
{1}
>>> a|b
{1, 2, 3, 4}
>>> a.union(b)
{1, 2, 3, 4}


https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

http://www.codeskulptor.org/#user43_WXFeOP4lup_0.py

##quick-union method
class UF:
    def __init__(self, lst, n):
        self.id = range(n)        
        self.cnt = n
        for p,q in lst:
            self.union(p,q)
    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p
    def union(self,p,q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        self.id[proot] = self.id[qroot]
        self.cnt -= 1
    def id(self):
        return self.id
    def cnt(self):
        return self.cnt

        
def main():
    a = [(4,3),(3,8),(6,5),(9,4),(2,1),(5,0),(7,2),(6,1)]
    uf = UF(a, 10)
    print uf.id
    print uf.cnt

    
main()    
    
        

##check whether there is a cycle in undirected graph
from collections import defaultdict

g = [(0,1),(1,2),(1,3)]
graph = defaultdict(list)
for u,v in g:
    graph[u].append(v)
    graph[v].append(u)
visited=[False]*len(graph)
hascycle = False
def dfs(u,v):
    #当前访问的是u，v是u的直接连接的Parent
    print v, 'is', u, 's parent'
    visited[u] = True
    for w in graph[u]:
        if not visited[w]: 
            dfs(w,u)
        else:#如果w已经被访问过了,则w定为u的parent(即v),否则定有环
            print w,v,'@'
            if w!=v:
                print w,v
                hascycle = True

dfs(0,0)


#list convert to string
list1 = ['1', '2', '3']
str1 = ''.join(list1)
print str1
print 
list2 = [1,2,3]
str2 = ''.join(str(e) for e in list2)
print str2
print 

#use zip
a = [1,2,3]
b = [4,5,6]
for el in zip(a,b):
    print el
print
c = [[6,7,8],[1,2,3],[4,5,7]]
for el in zip(*c):
    print el

#######################################	
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

x = [a,b,c]
print x
print '-----------------'    
for pair in zip(*x):
    print pair
print '-----------------'    
for pair in zip(x):
    print pair
    
    
output：~~~~~~~~~~~~~~~~~~~~~~~~~~
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
-----------------
(1, 4, 7)
(2, 5, 8)
(3, 6, 9)
-----------------
([1, 2, 3],)
([4, 5, 6],)
([7, 8, 9],)	
#%%
#########################################################
##Longest Consecutive Characters
s = 'aaabbcddeeeeefg'

def fun(s):
    max_cnt = 0
    max_char = None
    pre_char = None
    cnt = 0
    for c in s:
        if c == pre_char:
            cnt+=1
        else:
            cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_char = c
        pre_char = c
    print max_char, max_cnt
    
fun(s)

###########select elements randomly from a list######
import random
a = [1,2,3,4]
print [random.choice(a) for _ in range(2)]

#%%
############ coin change problem ##############
#用足够多的 1 分，2 分和 5 分硬币凑出 1 元钱，一共有多少种方法？
#give you a money value, how many ways of changing coins by using a denominator list l 
def coinchange(money, coins):
    if money < 0 or (money>0 and not coins):
        return 0
    if money == 0:
        return 1
    return coinchange(money-coins[0], coins) + coinchange(money, coins[1:])

print coinchange(4,[1,2])
#4=1+1+1+1; 4=1+1+2; 4=2+2, so, return 3 
#%%
###########iterative method############
n = 10
v = [1,2,5]
L = [0 for i in range(n+1)]
L[0]=1
for coin in v:
    for i in range(coin, n+1):
        L[i] += L[i-coin]
    print L
print L[-1]
##################
# following is woring......
n = 10
v = [1,2,5]
L = [0 for i in range(n+1)]
L[0]=1
for i in range(coin, n+1):
    for coin in v:
        L[i] += L[i-coin]
    print L
print L[-1]
##################

#%%
python
s = "cab"
s.find("a") = 1
s.find("c") = 0

print sorted(s) #['a', 'b', 'c']

print "".join(sorted(s))  #abc


BITree
##############################################################
#BIT tree (binary indexed tree)
arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

class BITree:
    def __init__(self,arr):
        self.tree = [0]*(len(arr)+1)
        self.array = [0] * len(arr) #保存了update之前的值
        self.construct(arr)
        print self.tree
        
        
    def construct(self,arr):
        for i, v in enumerate(arr):
            self.update(i, v)
            
    def update(self, idx, val):
        delta = val - self.array[idx]
        self.array[idx] = val#保存Update后的值（准备下次Update使用）
        idx += 1
        while idx < len(self.array):
            self.tree[idx] += delta
            idx += idx&(-idx)
            print self.tree #BITree的生长过程
    def getsum(self, idx):
        idx += 1
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx&(-idx)
        return sum
t = BITree(arr)
t.update(0,100) #要把0号位上的元素改为100（而不是加上100）

for i in range(len(arr)):
    print t.getsum(i),

#%%    