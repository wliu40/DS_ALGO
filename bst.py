#%%

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.hdist = 0
    def __str__(self):
        return str(self.val)
#%%        
class BST:
    def __init__(self):
        self.root = None
    def build_from_arr(self, arr):
        if not arr:
            self.root = None
        self.root = self.build_helper(arr, 0, len(arr)-1)
    def build_helper(self, arr, i, j):
        if i > j:
            return None
        mid = i + (j-i)/2
        root = Node(arr[mid])
        root.left = self.build_helper(arr, i, mid-1)
        root.right = self.build_helper(arr, mid+1, j)
        return root
    
    def bottom_view(self):
        res = self._bottom_view(self.root)
        return res
    def _bottom_view(self, root):
        res = dict()
        from Queue import Queue
        que = Queue()
        que.put(root)
        res[0] = root.val
        while que:
            tmp = que.get()
            if tmp:
                if tmp.left:
                    tmp.left.hdist = tmp.hdist-1
                    que.put(tmp.left)
                    res[tmp.hdist - 1] = tmp.left.val
                if tmp.right:
                    tmp.right.hdist = tmp.hdist+1
                    que.put(tmp.right)
                    res[tmp.hdist + 1] = tmp.right.val
        return res
                
    def add(self,val):
        if not self.root:
            self.root = Node(val)
            return
        tmp = self.root
        while True:
            if val < tmp.val:
                if tmp.left == None:
                    tmp.left = Node(val)
                    break
                else:
                    tmp = tmp.left
            else:
                if tmp.right == None:
                    tmp.right = Node(val)
                    break
                else:
                    tmp = tmp.right
                        
    def getMin(self):    	
        return self.min(self.root)
    def min(self, x):
        if x.left == None:
            return x
        return self.min(x.left)
    def getMax(self):
        return self.max(self.root)
    def max(self, x):
        if x.right == None:
            return x
        return self.max(x.right)
    
    
    def delMin(self):
        self.delMinRe(self.root)
    def delMinRe(self, root):
        if root.left == None:
            return root.right
        root.left = self.delMinRe(root.left)
        return root
    
    def delMax(self):
        self.delMaxRe(self.root)
    def delMaxRe(self, root):
        if root.right == None:
            return root.left
        root.right = self.delMaxRe(root.right)
        return root
    
    def delNode(self,val):
        return self.delNodeRec(self.root, val)
    def delNodeRec(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self.delNodeRec(node.left, val)
        elif val > node.val:
            node.right = self.delNodeRec(node.right, val)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            tmp = node
            node = self.min(tmp.right)
            node.right = self.delMinRe(tmp.right)
            node.left = tmp.left
        return node
        
    
    def delMinIter(self):
        if self.root == None:
            return
        dummy = Node(0)
        dummy.left = self.root
        pre = dummy
        cur = self.root
        while cur.left:
            pre = cur
            cur = cur.left
        pre.left = cur.right
        
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            print self.root.val
        else:            
            self.insert_recur(self.root,val)

    def insert_recur(self, root, val):
        if not root:
            root = Node(val)            
        else:
            if root.val > val:
                root.left = self.insert_recur(root.left, val)
            else:
                root.right = self.insert_recur(root.right, val)
        return root
    def levelOrderRecur(self):
        self.levelOrderHelper(self.root)       
    def levelOrderHelper(self, root):
        if not root:            
            return
        queue = [root]       
        while queue:
            tmp = queue.pop(0)
            if tmp:
                print tmp.val, " ",
                queue.append(tmp.left)
                queue.append(tmp.right)
#%%   
bst = BST()
for i in [4,1,2,3,6,0]:
    bst.insert(i)
bst.levelOrderRecur()
for i in [10,-1,5]:
    bst.add(i)
print 
bst.levelOrderRecur()

print bst.bottom_view()
#%%
print 
print bst.getMin()
print bst.getMax()
bst.delMin()
print 
bst.levelOrderRecur()
bst.delMax()
print 
bst.levelOrderRecur()
print 
bst.delMinIter()
bst.levelOrderRecur()
bst.delNode(2)
print 
bst.levelOrderRecur()