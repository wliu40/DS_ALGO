# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:35:52 2019

@author: CGYY2
"""
# 1. the tree stores the real value of low and high, and other third value for your goal
# for example, a sum or a cnt value, depends how to use the tree
# 2. only use the indexs to build the tree, so that is why we have to sort the array before building it,
# build the tree with the binaray, recursive call
# 3. generally, need a update and a query function
# 4. generally, the update function will update the third value
# 5. generally, the query function will query about the information of the third value by giving the low and high

class TreeNode(object):
    def __init__(self, lo, hi):
        self.lo = lo # this is the true value
        self.hi = hi
        self.left = None # left tree intialized to None
        self.right = None # same to right tree
        self.cnt = 0 # this is the additional third value, this value tracks how many elements exists btwn lo and hi.        
        self.sum = 0 # this value tracks the summation of the elements btwn lo and hi
    def __str__(self):
        return "[{}, {}]".format(self.lo, self.hi)
  
def build_tree(arr, left, right):
    """ this build funtion will build the seg-tree's skeleton, aka, the third value has not been updated yet"""
    root = TreeNode(arr[left], arr[right])
    if left == right:
        return root
    mid = (left+right)/2
    root.left = build_tree(arr, left, mid)
    root.right = build_tree(arr, mid+1, right)
    return root

def update_tree(root, val):
    """ use the update function to update the third value, ie. cnt or sum"""
    if not root:
        return
    if root.lo <= val <= root.hi:
        root.cnt += 1
        update_tree(root.left, val)
        update_tree(root.right, val)
        
def query(root, lo, hi):
    """" query the info about the third value """
    if lo <= root.lo and root.hi <= hi:
        return root.cnt
    if hi < root.lo and lo > root.hi:
        return 0
    return query(root.left, lo, hi) + query(root.right, lo, hi)

def update_tree_4sum(root, num, idx):
    if root.lo == root.hi:
        root.sum = num[idx]
        return idx
    mid = (root.lo + root.hi)/2
    if idx <= mid:
        update_tree_4sum(root.left, num, idx)
    else:
        update_tree_4sum(root.right, num, idx)

    root.sum = root.left.sum + root.right.sum
    return root.sum


def query_range_sum(root, lo, hi):
    if root.lo == lo and root.hi == hi:
        return root.sum
    mid = (root.lo + root.hi)/2
    #print lo, hi, mid
    if hi <= mid:
        return query_range_sum(root.left, lo, hi)
    elif lo >= mid+1:
        return query_range_sum(root.right, lo, hi)
    else:
        return query_range_sum(root.left, lo, mid) + query_range_sum(root.right, mid+1, hi)
   
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root
    inorder(root.right)
    
def level_order_traversal(root):
    if not root:
        return []
    que = [[0, root]]
    res = []
    while que:
        level, cur = que.pop(0)
        if len(res) <= level:
            res.append([])
        if cur:
            res[-1].append(str(cur)+" "+str(cur.cnt) + ' ' + str(cur.sum))
        else:
            res[-1].append("NULL")
        if cur:
            que.append([level+1, cur.left])
            que.append([level+1, cur.right])     
    return res


  #%%  
arr = [1,5,-1,4,6,3,10,7]

tree = build_tree(sorted(arr), 0, len(arr)-1)
inorder(tree)
level_order_traversal(tree)
for i in arr:
    update_tree(tree, i)
level_order_traversal(tree)
#%%

arr = [1,5,-1,4,6,3,10,7]
tree = build_tree(range(len(arr)), 0, len(arr)-1)
level_order_traversal(tree)
#%%
for i in range(len(arr)):
    update_tree_4sum(tree, arr, i)

level_order_traversal(tree)
print query_range_sum(tree, 1,3)
print query_range_sum(tree, 2,3)
#%%