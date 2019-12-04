#%%





#%%
************************ 94. Binary Tree Inorder Traversal ********************
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> sk;
        TreeNode *tmp = root;
        while(tmp || !sk.empty()){
            while(tmp){
                sk.push(tmp); //在压入的时候就访问，是先序遍历
                tmp = tmp->left;
            }
            tmp = sk.top();            
            res.push_back(tmp->val);//在弹出的时候访问，是中序遍历
            sk.pop();
            tmp = tmp->right;
        }        
        return res;        
    }
};
// 递归方法
class Solution {
public:
    vector<int> vec;
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL)
            ;
        else
        {
            inorderTraversal(root->left);
            vec.push_back(root->val);
            inorderTraversal(root->right);
        }
        return vec;
    }
};


********************* 96. Unique Binary Search Trees *******************
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
class Solution {
public:

    int numTrees(int n) {
        vector<int> ans(n+1); // DP, prepare vector to store the results from 1 to n
        //初始化base case
        ans[0] = 1;
        //i代表节点的个数，使用动态规划，依次求出当节点数是1，2, 3...一直到n的解，这些解依次储存到ans[1], ans[2]...到ans[n-1]
        //动态规划： 大问题的解建立在小问题的解的基础上： 例如当求解ans[4]时，会用到已经求得的ans[0], ans[1], ans[2], ans[3]的值. 
        for (int i = 1; i <= n; i++)
        {
            //e.g., 假设 i == 4; 则节点1,2,3,4都可能是root, 所以要用Loop把所有的这些可能的子树都加起来
            //假设1是root,则1的左边子树只能为空(只有1种这样的子树)，右边子树是一个三个节点的子树（有ans[3]这么多种不同的子树）
            //所以对于1是root的情况，共有ans[0]*ans[3]这么多种不同的子树。
            //又比如，假设3是root，则3的左子树有ans[3-1]种可能，右子树有ans[4-3]种可能。共有ans[2]*ans[1]多种不同的子树
            for (int root = 1; root <= i; root++)
                ans[i] += ans[root-1]*ans[i-root];
        }
        return ans[n]; //返回节点数为n的解
    }
};
*********************** 95. Unique Binary Search Trees II ******************
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
class Solution {
public:
    vector<TreeNode*> generateTreesUtil(int start, int end) {
    	vector<TreeNode*> res;
    	// 当start == end的时候，只生成一个根节点的树
    	// 当start > end的时候，结束递归， 需要返回一个[[]]
    	if (start > end) {
    		res.push_back(nullptr); // empty tree
    		return res;
    	}
		
    	// first, for simple case, GT(1,1) will generate a tree like NULL<-TreeNode(1)->NULL;
        // e.g., GT(1, 3)
        // i = 1: leftTrees = GT(1, 0); rightTrees = GT(2,3); so, GT(1,0)<-TreeNode(1)->GT(2, 3)
        //        leftTrees = [[]]; rightTrees = GT(2, 3): 
        //                          i = 2: leftTrees = GT(2,1); rightTrees = GT(3,3); so,NULL<-TreeNode(2)->TreeNode(3);
        //                          i = 3: leftTrees = GT(2,2); rightTrees = GT(4,3); so,TreeNode(2)<-TreeNode(3)->NULL;
        //                          so, GT(2,3) = [[2,null,3],[2,3,null]]
        // i = 2: leftTrees = GT(1,1); rightTrees = GT(3,3), so, GT(1,1)<-TreeNode(2)->GT(3,3)
        // i = 3: leftTrees = GT(1,2); rightTrees = GT(4,3); so GT(1,2)<-TreeNode(3)->GT(4,3)
        //        rightTrees = [[]]; leftTrees = GT(1,2)
        //                           i = 1: leftTrees = GT(1,0); rightTrees = GT(2,2);so, NULL<-TreeNode(1)->TreeNode(2)
        //                           i = 2; leftTrees = GT(1,1); rightTrees = GT(3,2);so, TreeNode(1)<-TreeNode(2)->NULL;
        //                           so, GT(1,2) = [[1,null,2],[2,1,null]]
		
    	for (int i = start; i <= end; ++i) {
    		vector<TreeNode*> leftSubtrees = generateTreesUtil(start, i - 1);
    		vector<TreeNode*> rightSubtrees = generateTreesUtil(i + 1, end);
			
        // 两个for循环嵌套：
        // e.g., [1,2,3,4,5]; i = 3; 此时，root是TreeNode(3), GT(1,2)<-TreeNode(3)->GT(4,5)
        // GT(1,2) = [[1,null,2], [2,1,null]] <-TreeNode(3) ->[[4,null,5], [5,4,null]]
        // 明显的，共有2*2 = 4种可能的组合
		
    		for (TreeNode *left : leftSubtrees) {
    			for (TreeNode *right : rightSubtrees) {
    				TreeNode* root = new TreeNode(i);
    				root->left = left;
    				root->right = right;
    				res.push_back(root);
    			}
    		}
    	}
    	return res;
    }
    
    vector<TreeNode*> generateTrees(int n) {
        if(!n) return vector<TreeNode*>{};
        return generateTreesUtil(1, n);
    }
};
************************ 98. Validate Binary Search Tree ******************
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

class Solution {
public:
bool isValidBST(TreeNode* root) {
    return isValidBST(root, NULL, NULL);
}

bool isValidBST(TreeNode* root, TreeNode* minNode, TreeNode* maxNode) {
    if(!root) return true;
    if(minNode && root->val <= minNode->val) return false; 
    if(maxNode && root->val >= maxNode->val) return false;
    return isValidBST(root->left, minNode, root) && isValidBST(root->right, root, maxNode);
}
};
*****************************  100. Same Tree  **************************
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if ( p == NULL && q == NULL)
            return true;
        if ( p == NULL && q != NULL)
            return false;
        if ( p != NULL && q == NULL)
            return false;
        else if (p->val != q->val)
            return false;
        else
        {
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
        
    }
};
*************************** 101. Symmetric Tree ***********************************
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

class Solution {
public:
    bool isSymmetric(TreeNode *L, TreeNode *R)
    {
        if(!R && !L)
            return true;
        if (L && !R || !L && R || L->val != R->val)
            return false;
        return isSymmetric(L->left, R->right) && isSymmetric(L->right, R->left);
    }
    
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        return isSymmetric(root->left, root->right);
    }
};

**************************** 102. Binary Tree Level Order Traversal ***********************
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector< vector<int> >result;
        stack<pair<TreeNode*, int>> sk;
        sk.push(make_pair(root, 0));
        TreeNode *tmp;
        int level;
        while(!sk.empty()){
            tmp = sk.top().first;
            level = sk.top().second;
            sk.pop();
            if(tmp){
                if (result.size() <= level){ //如果进入下一层，则加入一个新的vector
                    result.push_back(vector<int> {});//树有几层，就会加入几个vector
                }              
                result[level].push_back(tmp->val); //在result[level]上加入新的node
                if(tmp->right) sk.push(make_pair(tmp->right, level+1));
                if(tmp->left) sk.push(make_pair(tmp->left,level+1));
            }
        }        
        return result;
    }
};
************************103. Binary Tree Zigzag Level Order Traversal*************************
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int> > res;
        if(!root) return res;
        stack<pair<TreeNode*, int>> sk;
        sk.push(make_pair(root,0));
        TreeNode* tmp;
        int level = 0;
        while(!sk.empty()){
            tmp = sk.top().first;
            level = sk.top().second;
            sk.pop();
            if(tmp){
                if(res.size() <= level)
                    res.push_back(vector<int>{});
                if(level % 2)
                    res[level].push_back(tmp->val);//插到尾部
                else
                    res[level].insert(res[level].begin(), tmp->val);//每次插到第一个位置
                sk.push(make_pair(tmp->left, level+1));
                sk.push(make_pair(tmp->right, level+1));
            }
        }
        return res;
    }
};   
***************************104. Maximum Depth of Binary Tree***********************************
Given a binary tree, find its maximum depth.
class Solution {
public:
    int maxDepth(TreeNode* root) 
    {
        int left_height, right_height,max_height;
        if (root == NULL)
            return 0;        
        else{
            left_height = maxDepth(root->left);
            right_height = maxDepth(root->right);
            max_height = (left_height > right_height)? left_height: right_height;
            max_height++;
            return max_height;
        }       
    }
};

****************************************************************************
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.
class Solution {
public:
    TreeNode* buildTreeUtil(vector<int> &preorder, int i, int j, vector<int> &inorder, int ii, int jj){
        if(i >= j|| ii >=jj)
            return NULL;
        
        int root_val = preorder[i];
        auto iter = find(inorder.begin()+ii, inorder.begin()+jj, root_val);
        int dist = iter - inorder.begin() - ii;
        //cout << dist << endl;
        TreeNode* root = new TreeNode(root_val);
        root->left = buildTreeUtil(preorder, i+1, i+dist+1, inorder, ii, ii+dist);
        root->right = buildTreeUtil(preorder, i+dist+1, j, inorder, ii+dist+1, jj);
        return root;      
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
       return buildTreeUtil(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }
};
*************************106. Construct Binary Tree from Inorder and Postorder Traversal*************************
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
class Solution {
public:
TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
        return helper(inorder, 0, inorder.size(), postorder, 0, postorder.size());
    }
private:
    //
    //[8,4,9,2,5,10,1,6,3,7,12]
    //[8,9,4,10,5,2,6,12,7,3,1]
    
    //helper(inorder, 0, 9, postorder, 0, 9);
    //inorder:    [8, 4, 9, 2, 5, 1, 6, 3, 7]
    //postorder:  [8, 9, 4, 5, 2, 6, 7, 3, 1]
    // index       0  1  2  3  4  5  6  7  8 
    //1.root_val = 1;
    //2.在inorder里找到1的iterator, inorder[5] = 1, 计算距离dis = 5;
    //3.创建TreeNode(1)
    //4.    TreeNode(1) ->left = helper(inorder, 0, 5, postorder, 0, 5);
    //                         这时inorder =    [8, 4, 9, 2, 5] 1 6 3 7
    //                             postorder =  [8, 9, 4, 5, 2] 6 7 3 1
    //                                index =    0  1  2  3  4  5 6 7 8 
    //                      1.      root_val = 2
    //                      2.      在inorder里找到2的Iterator, inorder[3] = 2, 计算距离dis = 3
    //                      3.      创建TreeNode(2)
    //                      4.      TreeNode(2)->left = helper(inorder, 0, 3, postorder, 0, 3)
    //                                            inoder =    [8, 4, 9] 2 5 1 6 3 7
    //                                            postorder = [8, 9, 4] 5 2 6 7 3 1
    //                                            index =      0  1  2  3 4 5 6 7 8 
    //                                              1.   root_val = 4
    //                                              2.   inoder[1] = 4, dis = 1
    //                                              3.   TreeNode(4)
    //                                              4.   TreeNode(4)->left = helper(inorder, 0, 1, postorder, 0, 1)
    //                                                                inorder =   [8] 4 9 2 5 1 6 3 7
    //                                                                postorder = [8] 9 4 5 2 6 7 3 1
    //                                                                  index =    0  1 2 3 4 5 6 7 8
    //                                                          1.    找到inorder[0] = 8, dis = 0
    //                                                          2.    创建TreeNode(8)
    //                                                          3.    TreeNode(8) ->left = NULL return!!
    //                                              1.  TreeNode(4)->right = helper(inorder, 2, 3, postorder, 1, 1)
    //
    //5.    TreeMpde(1)->right = helper(inorder, 6, 9, postorder, 5, 8); 
    //                         这时inorder =     8, 4, 9, 2, 5  1 [6 3  7]
    //                             postorder =   8, 9, 4, 5, 2 [6  7 3] 1
    //                                index =    0  1  2  3  4  5  6 7  8
    //...................................................................................
    //                                                     index        0  1  2  3  4  5  6  7  8 
    //            return = helper(inorder, 0, 9, postorder, 0, 9);     [8  4  9  2  5  1  6  3  7]
    //                                                                 [8  9  4  5  2  6  7  3  1]
    //TreeNode(1) ->left = helper(inorder, 0, 5, postorder, 0, 5);     [8  4  9  2  5] 1  6  3  7 
    //                                                                 [8  9  4  5  2] 6  7  3  1
    //TreeMpde(1)->right = helper(inorder, 6, 9, postorder, 5, 8);      8  4  9  2  5  1 [6  3  7]
    //                                                                  8  9  4  5  2 [6  7  3] 1
    //基本思路, inorder和postorder给出了两个数列（数的不同遍历表示）, i,j 和ii, jj 分别给出了数列的两个窗口
    //在每次递归中，由postorder[jj-1]，即postorder窗口的最后一个值root_val，定义出一个新的子树树根，
    //然后在inorder中寻找到root_val的位置，然后以位置为界，把inorder/postorder画出两个窗口（如上面例子所示）
    //在接下来的递归中，重复上述过程。
    //                  
    //    
    //用i, j 表示该轮递归，作用在inorder的范围，即是inorder[i, j], 最外层递归自然是inorder[0, inorder.size()]
	
    TreeNode* helper(vector<int>& inorder, int i, int j, vector<int>& postorder, int ii, int jj)
    {
        // 每次取postorder的最后一个值root_val，将其作为树的根节点
        // 然后从inroder中找到mid，将其分割成为两部分，左边作为mid的左子树，右边作为mid的右子树
        // tree:     8 4 10 3 6 9 11
        // Inorder   [3 4 6] 8 [9 10 11]
        // postorder [3 6 4]   [9 11 10] 8

        if(i >= j || ii >= jj)
            return NULL;
        
        int root_val = postorder[jj-1];//在jj-1的位置上即是下一个根节点，在最外层递归，就是postorder的最后一个元素
        
        auto f = find(inorder.begin() + i,inorder.begin() + j,root_val);//在i和j的范围内寻找root_val, 返回一个iterator
        
        int dis = f - inorder.begin() - i; //dis是找到的iter与位置索引i的距离， inorder[i+dis] == root_val
        
        TreeNode* root = new TreeNode(root_val);
        /*
        cout << "root_val = " << root_val << " = ";
        cout << "inorder[" << i+dis << "]; ";
        cout << "inorder：[ ";
        for(int k = i; k < i+dis; k++){
            cout << inorder[k] << " ";
        }
        cout << "] + " << "[ ";
        for(int k = i+dis+1; k < j; k++){
            cout << inorder[k] << " ";
        }
        cout << "]; postorder：[ ";
        for(int kk = ii; kk < ii+dis; kk++){
            cout << postorder[kk] << " ";
        }
        cout << "] + [ ";
        for(int kk = ii+dis; kk < jj-1; kk++){
            cout << postorder[kk] << " ";
        }
        cout << "];" << i <<" " << i+dis << " " << j << " " << ii << " " << ii+dis << " " << jj-1 <<endl;
        */
        root -> left = helper(inorder,  i,       i+dis, postorder, ii,     ii+dis);
        root -> right = helper(inorder, i+dis+1, j,     postorder, ii+dis, jj-1 );
        return root;        
    }
};
**********************107. Binary Tree Level Order Traversal II*************
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        stack<pair<TreeNode*, int>> sk;
        sk.push(make_pair(root, 0));
        TreeNode *tmp;
        int level = 1;
        vector<vector<int>> res;
        while(!sk.empty()){
            tmp = sk.top().first;
            level = sk.top().second;
            sk.pop();
            if(tmp){
                if(res.size() <= level)
                    res.insert(res.begin(), vector<int>{});
                res[res.size()-level-1].push_back(tmp->val);
                sk.push(make_pair(tmp->right, level+1));
                sk.push(make_pair(tmp->left, level+1));
            }
        }
        return res;
    }
};
**********************108. Convert Sorted Array to Binary Search Tree******************
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
class Solution {
public:
    TreeNode* convert(vector<int> &nums, int L, int R)
    {
        if (L > R)
        return NULL;
        else{
            int mid = (L+R)/2;
            TreeNode * _root = new TreeNode(nums[mid]);
            _root->left = convert(nums, L, mid-1);
            _root->right = convert(nums, mid+1, R);
            return _root;
        }        
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return  convert(nums, 0, nums.size() - 1);     
    }
};
*****************************110. Balanced Binary Tree***************************
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
class Solution {
public:
    int isBalanced(TreeNode *_root, bool &flag){
        if ( !_root || !flag)
            return 0;
        int LH, RH;
        if (_root){
            LH = isBalanced( _root->left, flag);
            RH = isBalanced(_root->right, flag);
            if (abs(LH-RH) > 1)
                flag = false;
            return max(LH, RH) + 1;
        }
    }
    bool isBalanced(TreeNode* root) {
        bool flag = true;
        isBalanced(root, flag);
        return flag;
    }
};
***************************111. Minimum Depth of Binary Tree***********************
Given a binary tree, find its minimum depth.
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        int res = INT_MAX;
        helper(root, 0, res);
        return res;
    }
    void helper(TreeNode* root, int cur, int& res){
        if(!root) return;
        cur++;
        if(!root->left && !root->right){
            res = min(res, cur);
            return;
        }
        
        helper(root->left, cur, res);
        helper(root->right, cur, res);
    }
};
**********************************112. Path Sum**********************************
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root)
            return false;
        if (!root->left && !root->right){
            if(sum == root->val)
                return true;
            return false;
        }
        return hasPathSum(root->left, sum-root->val) || hasPathSum(root->right, sum-root->val);
    }
};
**********************************113. Path Sum II**********************************
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
class Solution {
public:
    void pathSum(vector<vector<int>> &result, vector<int> &v,int sum, TreeNode *_root)
    {
        if (!_root)
            return;
            
        //update the temp value for each node and push_back the value to v
        sum -= _root->val;
        v.push_back(_root->val);
    
        //recursively go to the left and right child
        pathSum(result, v, sum, _root->left);
        pathSum(result, v, sum, _root->right);
        
        //if this route meets the requirements, push v to the 2-D vector result
        //also remember to update temp value and v
        if (!_root->left && !_root->right && sum==0)
        {
            result.push_back(v);
        }
        //update temp and v each recursion
        sum += _root->val;
        v.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> result;
        vector<int> v;
        pathSum(result, v, sum, root);
        return result;
    }
};

************************114. Flatten Binary Tree to Linked List**************************
Given a binary tree, flatten it to a linked list in-place.
For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
class Solution {
public:
    
    TreeNode *prev;
    void flatten(TreeNode* root) {
        /*
        //recursive method:
        if(!root) return;
        
        flatten(root->right);
        flatten(root->left);
       
        root->right = prev;
        root->left = NULL;
        prev = root;
        */
        //iterative method:
        /*
             1            1            1
            / \          / \            \
           2   5        2   5            2
          / \   \      / \   \          / \
         3   4   6    3   4   6        3   4
                           \                \
                            5                5
                             \                \
                              6                6
         */ 
        while(root)
        {
            if(root->left)
            {
                // 先找到根结点的左树的最右的节点， 然后用该节点右树指向根结点的右树
                if(root->right)
                {
                    TreeNode* tmp = root->left;
                    while(tmp->right) 
                        tmp = tmp->right;
                    tmp->right = root->right;
                }
                //替换右树为左树，左树清空
                root->right = root->left;
                root->left = NULL;
            }
            //更新root为现在的右节点（原来的左节点）
            root = root->right;
        }
    }
};
******************************116. Populating Next Right Pointers in Each Node*************************
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
	
class Solution {
public:
    void connect(TreeLinkNode *root) {
        TreeLinkNode *parent(root), *levelHead(root), *tmp;
        
        while(parent && parent->left){
            tmp = parent->left->next = parent->right;
            if(parent->next){
                parent = parent->next;
                tmp->next = parent->left;
            }
            else{
                parent = levelHead = levelHead->left;
            }
        }
    }
};	
	
**************************117. Populating Next Right Pointers in Each Node II************************
What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
class Solution {
public:
    void connect(TreeLinkNode *root) {
        TreeLinkNode *parent(root), *tail(NULL), *head(NULL);
        //parent是上层的当前节点
        //head是下层的首个节点，tail是下层的当前尾节点
        //parent逐渐向后移动，在此过程中，将parent下一层的节点“串”起来
        while(parent)
        {
            //因为不知道parent是否有子节点，有几个子节点，所以每次询问parent->left, parent->right
            if (parent->left)
            //如果tail已经是非NULL,说明已经找到了head和tail, 只需移动tail, 并且让tail->next = 当前找到的上层的子节点
                if (tail)
                    tail = tail->next = parent->left;//由后向前赋值
                else
                    head = tail = parent->left;
            if (parent->right)
                if (tail) 
                    tail = tail->next = parent->right;
                else 
                    head = tail = parent->right;
                
            if(parent->next)
                parent = parent->next;
            else
            {
                parent = head;//parent移动到下一层
                head = tail = NULL;
            }
        }
    }
};
	

****************************129. Sum Root to Leaf Numbers************************
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
class Solution {
public:
    void sumNumbers(TreeNode *_root, int &ans, int sum)
    {
        sum += _root->val;
		//if this is a leaf node, add the val of this leaf node;
        // and return to upper recursive level		
        if (!_root->left && !_root->right){        

            ans += sum;
            return;
        }
        else{
            sum *= 10;
            //recursively visit its left and right child
            if (_root->left)
                sumNumbers(_root->left, ans, sum);                
            if (_root->right)
                sumNumbers(_root->right, ans, sum);
        }
    }
    int sumNumbers(TreeNode* root) {
        if (!root)
			return 0;        
        int ans = 0;
        sumNumbers(root, ans, 0);
        return ans;
    }
};

***************************144. Binary Tree Preorder Traversal****************************
class Solution {
public:
    vector<int> vec; // need to put this vec outside of the recursive function
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == NULL) // do nothing
            ;
        else
        {
            vec.push_back(root->val);
            preorderTraversal(root->left);
            preorderTraversal(root->right);
        }
        return vec;
    }
};
*****************************145. Binary Tree Postorder Traversal*****************************
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> v;
        if (!root)
            return v;

        stack<TreeNode*> sk;
        sk.push(root);
        TreeNode* tmp;
        while(!sk.empty())
        {
            tmp = sk.top();        
            v.insert(v.begin(), tmp->val);
            sk.pop();
            if (tmp->left)
                sk.push(tmp->left);
            if(tmp->right)
                sk.push(tmp->right);
        }        
        return v;
    }
};

*******************************173. Binary Search Tree Iterator*****************************
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        pushLeftNodes(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return ( !vec.empty() );
    }
	
    /** @return the next smallest number */
    int next() {
        int tempVal = vec.back()->val;
        TreeNode* tempNode = vec.back();
        vec.pop_back();
        pushLeftNodes(tempNode->right);
        return tempVal;
        
    }
    /*give you a _root, push_back all the left children line to vec*/
    void pushLeftNodes(TreeNode* _root)
    {
        TreeNode *tempNode = _root;
        while(tempNode)
        {
            vec.push_back(tempNode);
            tempNode = tempNode->left;
        }
    }
    
private:
    vector<TreeNode*> vec;
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
*****************************199. Binary Tree Right Side View******************************
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(!root) return res;
        stack<pair<TreeNode*, int>> sk;
        TreeNode* tmp;
        int level = 0;
        sk.push(make_pair(root, 0));
        while(!sk.empty()){
            tmp = sk.top().first;
            level = sk.top().second;
            sk.pop();
            if(tmp){
                if(res.size() <= level)
                    res.push_back(tmp->val);
                res[level] = tmp->val;
                sk.push(make_pair(tmp->right, level+1));
                sk.push(make_pair(tmp->left, level+1));
            }
        }
        return res;
    }
};


*****************************222. Count Complete Tree Nodes*********************************
Given a complete binary tree, count the number of nodes.
class Solution {
public:
    // 如果是一棵完美二叉树（），树高是n，则返回节点数：2^n-1；假设只有一个根结点，则2^1-1=1
    // 如果是不完美的二叉树，则根节点+递归计算左子树+递归计算右子树
    int countNodes(TreeNode* root) {
        if(!root) return 0;
        int left_height(0), right_height(0);
        TreeNode *left(root), *right(root);
        while(left){
            left = left->left;
            left_height++;
        }
        while(right){
            right = right->right;
            right_height++;
        }
        if (left_height == right_height)
            return (1<<left_height) - 1;
        return 1+countNodes(root->left) + countNodes(root->right);
        //加1是因为要加上根节点，然后去递归计算左右子树的节点数
        
    }
};
*****************************226. Invert Binary Tree***********************************
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
class Solution {
public:
    void swapNode(TreeNode*& _root) //指针的引用
    {
        TreeNode* temp;
        temp = _root->left;
        _root->left = _root->right;
        _root->right = temp;
    }
    void invertRecursive(TreeNode *_root)
    {
        if (_root == NULL)
            return;
        swapNode(_root);
        invertRecursive(_root->left);
        invertRecursive(_root->right);
    }
    TreeNode* invertTree(TreeNode* root) {
        invertRecursive(root);
        return root;
    }
};

*****************************230. Kth Smallest Element in a BST******************************
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Show Hint 
class Solution {
public:
    void inorderTrav(TreeNode* _root, int &k, vector<int> &v)
    {
        if (v.size() == k)
            return;
        if (_root)
        {
            inorderTrav(_root->left, k, v);
            v.push_back(_root->val);
            //cout << _root->val << endl;
            inorderTrav(_root->right, k, v);
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<int> v;
        inorderTrav(root, k, v);
        return v[k-1];
    }
};

**************************235. Lowest Common Ancestor of a Binary Search Tree*********************
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that 
has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant 
of itself according to the LCA definition.
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (p->val < root->val && q->val < root->val)
        lowestCommonAncestor(root->left, p, q);
    else if (p->val > root->val && q->val > root->val)
        lowestCommonAncestor(root->right, p, q);
    else
        return root;
    }
};

***************************236. Lowest Common Ancestor of a Binary Tree****************************
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has 
both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant 
of itself according to the LCA definition.
class Solution {
public:
    void find(TreeNode *root, TreeNode *des, vector<TreeNode*> &v)
    {
        //如果空，则返回
        if (!root)  return;
        //如果非空，则沿途压入vector  
        v.push_back(root);
        //如果找到了，则返回
        if ( root == des ) return;
        //递归查找左树和右树
        find(root->left, des, v);
        find(root->right, des, v);
        //如果vector的最后一个元素不是我们需要的，弹出
        if ( v.back() != des )  
            v.pop_back();
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
       //vector v1记录了从根节点到p的路径
        vector<TreeNode*> v1;
        find(root, p, v1);
        //vector v2记录了从根节点到q的路径
        vector<TreeNode*> v2;
        find(root, q, v2);
        
        //找出v1和v2第一个不同的元素
        int i;
        for (i = 0; i < v1.size() && i < v2.size(); i++)
        {
            if (v1[i] != v2[i])
                return v1[i-1];
        }
        //如果一个vector穷尽了，依然都相同，则返回较短vector的最后那个元素
        return v1.size() < v2.size() ? v1.back():v2.back();
    }
};
******************************257. Binary Tree Paths***********************************
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
class Solution {
public:
    void helperFun(TreeNode *_root, vector<string> &res, string temp){
        if (!_root)
            return;
        if (temp.size() != 0)
            temp += "->";
        temp += to_string(_root->val);
        if (!_root->left && !_root->right)
        {
            res.push_back(temp);
            return;
        }
        helperFun(_root->left, res, temp);
        helperFun(_root->right, res, temp);
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
            
        string temp = "";
        helperFun(root, res, temp);

        return res;
    }
};
******************************404. Sum of Left Leaves********************************
Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
class Solution {
public:
    int sum = 0;
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root)
            return 0;
        
        // 判断一个节点是否是左叶节点，如果是，加到sum里    
        if(root->left && !root->left->left && !root->left->right){
            sum += root->left->val;
        }
        sumOfLeftLeaves(root->left);
        sumOfLeftLeaves(root->right);
        return sum;
    }
};
******************************437. Path Sum III************************************
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

class Solution {
public:

    int res = 0, cnt = 0;
    // function can return all possible sum from the root to all its children.
    // e.g., tree[1,2,3,4], will return sum(1->2)=3, sum(1->2->4)=7, sum(1->3)=4
    int helper(TreeNode* root, int sum) {
        if(!root)
            return 0;
        res += root->val;
        if(res == sum)
            cnt++;
        
        helper(root->left, sum);
        helper(root->right, sum);
        res-=root->val;
        return res;
    }
    int pathSum(TreeNode* root, int sum) {
        if (!root)
            return 0;
        helper(root, sum);
        pathSum(root->left, sum);
        pathSum(root->right, sum);
        return cnt;
    }
};

***************************450. Delete Node in a BST***************************
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
	
class Solution {
public:
    //return the min node in a subtree, root != NULL
    TreeNode* getmin(TreeNode *root){
        if(root->left == nullptr)
            return root;
        return getmin(root->left);
    }
    //delete the min node in a subtree recursively
    TreeNode *delMin(TreeNode *root){
        if(root->left == nullptr)
            return root->right;
        root->left = delMin(root->left);
        return root;
    }
    //get the min iteratively given the root of a subtree
    TreeNode *getmin1(TreeNode *root){
        TreeNode* tmp = root;
        while(tmp->left){
            tmp = tmp->left;
        }
        return tmp;
    }
    //delete the min iteratively given the root a subtree
    TreeNode* delMin1(TreeNode *root){
        TreeNode *dummy = new TreeNode(0);
        dummy->left = root;
        TreeNode *pre(dummy), *cur(root);
        while(cur->left){
            pre = cur;
            cur = cur->left;
        }
        pre->left = cur->right;
        return dummy->left;
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root == NULL)
            return NULL;
        if(key < root->val) root->left = deleteNode(root->left, key);
        else if(key > root->val) root->right = deleteNode(root->right, key);
        else{
            if(root->right == nullptr)
                return root->left;
            if(root->left == nullptr)
                return root->right;
            TreeNode *tmp = root;//暂存要删除的点为tmp
            root = getmin1(tmp->right);//找到以tmp的右子树的最小节点（其实就是tmp的中序遍历的后继节点）
            root->right = delMin1(tmp->right);//重新定义root的右子树为删除掉min的新子树
            root->left = tmp->left;//重新定义root的左子树
        }
        return root; //返回该root为根的子树到上一层递归
    }
};
******************************501. Find Mode in Binary Search Tree*******************
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
class Solution {
public:
    void findModeRecur(TreeNode* root,  unordered_map<int, int> &mp, int &count){
        if(!root) return;
        mp[root->val]++;
        if(mp[root->val] > count)
            count = mp[root->val];
        findModeRecur(root->left, mp, count);
        findModeRecur(root->right, mp, count);
    }
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> mp;
        int count = 0;
        findModeRecur(root, mp, count);
        vector<int> res;
        for(auto it = mp.begin(); it!=mp.end(); it++){
            if(it->second == count){
                res.push_back(it->first);
            }
        }
        return res;     
    }
};
****************************508. Most Frequent Subtree Sum*********************
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of 
all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? 
If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
class Solution {
public:
    int fun(TreeNode *root, unordered_map<int,int> &mp, int &max){
        if(!root) return 0;
        int sum = root->val;
        sum += fun(root->left, mp, max);
        sum += fun(root->right, mp, max);
        mp[sum]++;
        if(mp[sum] > max)
            max = mp[sum];
        return sum;
    }
    vector<int> findFrequentTreeSum(TreeNode* root) {
        unordered_map<int, int> mp;
        int max = 0;
        fun(root, mp, max);
        vector<int> res;
        
        
        for (auto it = mp.begin(); it != mp.end(); it++){
            if(it->second == max)
                res.push_back(it->first);
        }
        return res;
    }
};
**********************513. Find Bottom Left Tree Value*************************
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        queue<pair<TreeNode*, int>> que;
        que.push(make_pair(root, 0));
        TreeNode *tmp;
        int level = 0;
        int res = root->val;
        int cnt = 1;
        while(!que.empty()){
            tmp = que.front().first;
            level = que.front().second;
            que.pop();
            if(tmp){
                if(cnt <= level){//如果进入了新的level,那么就更新res, 这个就是最左边的node，同时cnt++, 这样同一层的其他的数字就不会再加进来
                    res = tmp->val;
                    cnt++;
                }
                que.push(make_pair(tmp->left, level+1));
                que.push(make_pair(tmp->right, level+1));
            }
        }
        return res;
    }
};
************************515. Find Largest Value in Each Tree Row*********************
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int> res;       
        stack<pair<TreeNode*, int>>sk;
        TreeNode* tmp = root;
        int level = 0;
        sk.push(make_pair(root, 0));
        while(!sk.empty()){
            tmp = sk.top().first;
            level = sk.top().second;
            sk.pop();
            if(tmp){
                if(res.size() <= level){
                    res.push_back(INT_MIN);
                }
                if(res[level]< tmp->val){
                    res[level] = tmp->val;
                }
                sk.push(make_pair(tmp->left, level+1));
                sk.push(make_pair(tmp->right, level+1));
            }
        }
        return res;
    }
};
******************************538. Convert BST to Greater Tree***************************
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
class Solution {
public:
    
    TreeNode *helper(TreeNode *root, int &sum){
        if(!root) return NULL;
        
        helper(root->right, sum);
        
        root->val += sum;
        sum=root->val;

        helper(root->left, sum);
        return root;
    }
    
    TreeNode* convertBST(TreeNode* root) {
        int res = 0;
        return helper(root, res);
    }
};

*****************************543. Diameter of Binary Tree********************************
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
class Solution {
public:

    int diameter(TreeNode* root, int &res){
        if(!root)
            return 0;
        int left = diameter(root->left, res);
        int right = diameter(root->right, res);
        int max = left>right?left+1:right+1;
        if(left+right>res)
            res = left+right;
        return max;
    }
    int diameterOfBinaryTree(TreeNode* root) {        
         int res = 0;
         diameter(root,res);
         return res;
    }
};
****************************************************************************
def check_if_level_order_traversal_can_be_BST(arr):
    from collections import deque
    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    que = deque([[float('-inf'), arr[0], float('inf')]])
    i = 1
    while i < len(arr) and len(que):
        low, val, high = que.popleft()
        if low < arr[i] and arr[i] < val:
            que.append([low, arr[i], val])
            print que[-1][1], ' can be left node of the node', val
            i += 1

        if val < arr[i] and arr[i] < high:
            que.append([val, arr[i], high])
            print que[-1][1], ' can be right node of the node', val
            i += 1
    if i == len(arr):
        print 'YES'
        return
    print 'NO'

arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
check_if_level_order_traversal_can_be_BST(arr)


