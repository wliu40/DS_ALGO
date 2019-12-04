https://leetcode.com/problems/sum-of-two-integers/#/solutions MUST SEE................................................!
turn-off the right-most set bit? 
get the right-most set bit?
get the left-most set bit?
turn-on the right-most bit set?
is kth bit set?
set all bit to 1 ones?
get Complement?
flip all bits?


http://www.codeskulptor.org/#user43_zowXFFR7pG_0.py
---------------------------------------------------------------------
turn-off the right-most set bit? x&(x-1)
get the right-most set bit? x&(-x)
get the left-most set bit? 
x |= x>>1
x |= x>>2
x |= x>>4
x |= x>>8
x |= x>>16
x ^= x>>1
turn-on the kth bit set?
x |= 1<< k
is kth bit set?
bool flag = x & (1 << k)
set all bit to 1 ones?
x |= x>>1
x |= x>>2
x |= x>>4
x |= x>>8
x |= x>>16
get Complement?
y = x
y |= y>>1
y |= y>>2
y |= y>>4
y |= y>>8
y |= y>>16
x ^= y 
flip all bits?
~x
hash a string to a number?
string s = "abc"
int num = 0;
for(char c: s){
	num |= 1 << (c-'a'); //num = 0000 0111 <= s = 'abc'
}
hash a string with repeated chars to a number?
string s = "ACGTAGCT";
unsigned char convert[26];
convert[0] = 0; // 'A' - 'A'  00  //因为每个字母占2位
convert[2] = 1; // 'C' - 'A'  01
convert[6] = 2; // 'G' - 'A'  10
convert[19] = 3; // 'T' - 'A' 11
int num = 0;
for(int i = 0; i < s.size(); i++){
	num <<= 2;
	num |= convert[s[i] - 'a']; //00 01 10 11 00 10 01 11  <= 'A C G T A G C T'
}

*******************turn off/on or toggle the kth bit**********************
	// 1 << 3: 0000 0100
	// 1 << 4: 0000 1000
	int turnOffKthBit(int n, int k){
		return n & ~(1 << (k - 1));
	}
	int turnOnKthBit(int n, int k){
		return n | (1 << (k - 1));
	}
	int isKthBitset(int n, int k) {
		return n & (1 << (k - 1));
	}
	int toggleKthBit(int n, int k) { //flip the kth bit
		return n ^ (1 << (k - 1));
	}

#-------------------------------------------------------
def num2str(num):
    s = ""
    while num:
        s = str(num&1) + s
        num >>= 1
    return '0'*(32-len(s)) + s
    	
n = pow(2,10)
for i in range(5):
    n |= 1<<i
    print num2str(n)
	
00000000000000000000010000000001
00000000000000000000010000000011
00000000000000000000010000000111
00000000000000000000010000001111
00000000000000000000010000011111


n = 1024
for i in [1,2,4,8,16]:
    n |= n>>i
    print num2str(n)
    
	
00000000000000000000011000000000
00000000000000000000011110000000
00000000000000000000011111111000
00000000000000000000011111111111
00000000000000000000011111111111
*******************get the opposite num**********************
int SignReversal(int x)  
{  
    return ~x + 1;  //取反加1
}  
*******************get the absolute value**********************
int my_abs(int x)  
{  
    int i = x >> 31; // if a>0,i=0; if a<0,i=-1
    return ((x ^ i) - i);  
}
*******************turn off the right-most set bit**********************
https://www.quora.com/What-are-some-cool-bit-manipulation-tricks-hacks
https://www.hackerearth.com/practice/notes/bit-manipulation/

turn off the right-most 1 of n: n &= n-1;
*************************get right-most set bit**************************
***method 1***
x & -x;

***method 2***
x ^ (x & (x-1));
-1: 1111 1111 = ~(0)   1: 0000 0001
-2: 1111 1110 = ~(1)   2: 0000 0010
-3: 1111 1101 = ~(2)   3: 0000 0011
-4：1111 1100 = ~(3)   4: 0000 0100
negative and positive num:  ~10 = -11, or 10 = ~(-11)
e.g., 10: 0000 1010
	 -11: 1111 0101	 

// example for get rightmost set bit, 得到最右的1位，其余位设置为0
x:             01110000
~x:            10001111
-x or ~x + 1:  10010000
x & -x:        00010000

// example for turning off the right-most 1 bit （unset the rightmost set），将最右的1位设置为0
x:             01110000
x-1:           01101111
x & (x-1):     01100000
	 
X_xor_Y = x^y; the bit is 1 when x and y are different at that bit, 得到的1位说明x和y在那一位上不同。
get the right-most first different bit: int mask = X_xor_Y&(-X_xor_Y);
	10: 0000 1010
   -10: 1111 0110
 =>tmp: 0000 0010
**************************get left-most set bit****************************
***method 1***
	
	x |= x >> 16;	
	x |= x >> 8;
	x |= x >> 4;
	x |= x >> 2;
	x |= x >> 1;
	x ^= x >> 1;	
	/*e.g.,
	int x = 0x0A00;	
	x = 0000 1010 0000 0000 (x |= x >> 16)
	x = 0000 1010 0000 1010 (x |= x >> 8)
	x = 0000 1010 1010 1010 (x |= x >> 4)
	x = 0000 1010 1010 1010 (x |= x >> 2)
	x = 0000 1111 1111 1111 (x |= x >> 1)
	x = 0000 1000 0000 0000 (x ^= x >> 1)	
	*/
***method 2***
	int cnt=0;
	while (x > 1) {
		cnt++; 
		x = x >> 1;
	}
	x = x << cnt;

**********************136. Single Number**************************
Given an array of integers, every element appears twice except for one. Find that single one.
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int temp = 0;
        for (auto iter = nums.cbegin(); iter != nums.cend(); iter++){
            temp = temp^(*iter);
        }
        return temp;
    }
};
// x ^ x = 0;
// x^ 0 = x;
//x ^ y ^ x = y;
*******python code********
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)
************************371. Sum of Two Integers****************************
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
//http://stackoverflow.com/questions/9070937/adding-two-numbers-without-operator-clarification
//正常的计算过程应该是从右至左，逐位进行。在这过程中，前面产生的carry会逐渐“产生-消耗”并影响后续的计算
//而在这里，递归过程模拟了carry“产生-消耗”过程
class Solution {
public:
    int getSum(int a, int b) {
        if(b ==0 )
            return a;
        int sum = a^b; //计算除去carry数的和
        int carry = (a&b) << 1;//计算carry
        return getSum(sum,carry);
    }
    /*
        int getSum(int a, int b) {
        int sum = a^b;
        int carry = (a&b)<<1;
        while(carry){
            int tmp = sum;
            sum ^= carry;
            carry = (tmp&carry)<<1;
        }
        return sum;
    }
    */
};

/*
sum = a^b
0+0=0 
0+1=1 
1+0=1 
1+1=0 (and generates carry)
*********************
a = 5, b = 7
    a = 0 1 0 1
    b = 0 1 1 1
  a+b = 1 1 0 1
                      sum = a^b = 0 0 1 0
carry = (a&b)<<1 = (0 1 0 1)<<1 = 1 0 1 0
*/

**********************191. Number of 1 Bits******************************
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
class Solution {
public:
    int hammingWeight(uint32_t n) {    
        int res = 0;
        while(n){
            if(n&1) res++;
            n >>= 1;
        }
        return res;
    }
};

*********************169. Majority Element******************************
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
class Solution {
public:

    int majorityElement(vector<int>& nums) {
        int res = 0, mask = 1;
        for(int i = 0; i < 32; i++){
            int count = 0;
            for(int num : nums){
                if((mask & num) != 0)
                    count++;
                if(count > nums.size()/2){
                     res |= mask;
                     break;
                }
            }
            mask <<= 1; 
        }
        return res;
    }        
};
**************************338. Counting Bits**************************
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate 
the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].
class Solution {
public:
    vector<int> countBits(int num) {
        int offset = 1;
        vector<int> res;
        res.resize(num+1);
        for(int i = 1; i <= num; i++){
            if(i == offset*2)
                offset *= 2;
            res[i] = res[i - offset] + 1;
        }
        return res;
    }
};
***************************137. Single Number II*************************
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
*********method 1*******
class Solution {
public:
/*
    3,3,4,3
    0011
    0011
    0100
    0011
从1到32位，统计各bit上1出现的次数sum，然后sum%3得到那个孤立位（如果是1的话)
*/    
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int i = 0; i < 32; i++) {
            int sum = 0;
            for(int j = 0; j < nums.size(); j++) {
                if(((nums[j] >> i) & 1) == 1) {
                    sum++;
                }
            }
            sum %= 3;
            ans |= sum << i;
        }
        return ans;
    }
};
*********method 2*******
ones - At any point of time, this variable holds XOR of all the elements which have appeared "only" once.
twos - At any point of time, this variable holds XOR of all the elements which have appeared "only" twice.

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        //e.g., 3,3,2,3
        int ones = 0, twos = 0;
        int common_bit_mask;
        for(int x: nums){
            twos = twos | (ones&x);
            ones = ones^x;
            //把ones和twos共有的'1'位变为'0'
            common_bit_mask = ~(ones&twos);
            ones &= common_bit_mask;
            twos &= common_bit_mask;
        }
        return ones;
    }
};
***************************187. Repeated DNA Sequences*************************
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA,
it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
/*
http://blog.csdn.net/haiyi727/article/details/43752693
http://www.cnblogs.com/grandyang/p/4284205.html
http://www.cnblogs.com/hzhesi/p/4285793.html?utm_source=tuicool


////
http://stackoverflow.com/questions/21240081/how-to-get-higher-20-bits-from-64-bit-integer  //如果修改位
/////
http://blog.csdn.net/eaglex/article/details/6310727 常见的哈希函数
*/

class Solution {
public:    
    vector<string> findRepeatedDnaSequences(string s) {

        int hashTable[1024*1024] = {0};
        vector<string> ans;
        if(s.size() <= 10)
            return ans;
            
        unsigned char convert[26];
        convert[0] = 0; // 'A' - 'A'  00
        convert[2] = 1; // 'C' - 'A'  01
        convert[6] = 2; // 'G' - 'A'  10
        convert[19] = 3; // 'T' - 'A' 11        

        for(int i = 0; i < 10; i++){
            int cycles = (s.size()-i)/10;
            
            for(int j = 0; j < cycles; j++){
                int hashValue = 0;
                int start = i + j*10;
                for(int k = start; k < start+10; k++){
                    hashValue <<= 2;
                    hashValue |= convert[s[k] - 'A'];
                }
                if( hashTable[hashValue] == 1 )
                    ans.push_back( s.substr(start, 10) );
                hashTable[hashValue]++;
            }
        }        
        return ans;
    }
};
************************268. Missing Number****************************
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
/*
x^x = 0
x^0 = x
x^y^x = y
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            res ^= ((i+1)^ nums[i]);
        }
        return res;
    }
};
**************************260. Single Number III**************************
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int XxorY= 0;
        for(auto &i:nums){
            XxorY ^= i;
        }
        //以上等同于：
        //int XxorY = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
        int temp = XxorY&(-XxorY); //XxorY: 0010 1010, -XxorY = 1111 0110 ( -XxorY = ~(XxorY-1), e.g., -11 = ~(11-1) )
        //so, temp = 0000 0010, 也就是说X和Y在倒数第二位是不同的，一个为1, 另一个为0（但不知道哪个数倒数第二位为0，哪个数为1）
        vector<int> res(2,0);
        //因为对于nums里面的所有的数而言，倒数第二位不是0就是1，所以用&将nums里面的数分为两组，一组倒数第二位为0，另一组为1
        //这样自然就把X和Y分开了，X在一组，而Y在另外一组
        //接下来的问题就是，在一组数字里面，除了一个数只出现一次以外，剩下的数都成双出现，如何找出这个单独出现的数
        for(auto &i:nums)
        {
            if ((i&temp) == 0)
                res[0] ^= i;
            else
                res[1] ^= i;
        }
        return res;
    }
};
*************************231. Power of Two***************************
Given an integer, write a function to determine if it is a power of two.
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return (n>0)&&!(n&(n-1));
    }
};
*************************461. Hamming Distance***************************
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
class Solution {
public:
    int hammingDistance(int x, int y) {
        int mask = x^y;
        int res = 0;
        while(mask){
            if(mask &1)
                res++;
            mask >>=1;			
        }
        return res;
    }
};
class Solution {
public:
    int hammingDistance(int x, int y) {
        int dist = 0, n = x ^ y;
        while (n) {
            ++dist;
            n &= n - 1; //turn off the right-most '1'
        }
        return dist;
    }
};

**************************190. Reverse Bits**************************
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
//method 1
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        //convert int to binary string representation
    	bitset<32> mybit(n);
    	string s = mybit.to_string();
    	//reverse a string
        reverse(s.begin(), s.end());
        
        //convert a string to char*
        char* c = new char[s.length() + 1];
        strcpy(c, s.c_str());
        //convert a char* to int long
        int res = strtol(c, nullptr, 2);
    	return res;
    }
};
//method 2
class Solution {
public:
    uint32_t  reverseBits(uint32_t n) {
        uint32_t result= 0;
        for(int i=0; i<32; i++)
            result = (result<<1) + (n>>i &1);        
        return result;
    }
};
//method 3
/*
for 8 bit binary number abcdefgh, the process is as follow:
abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
*/
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;
    }
};
************************78. Subsets****************************
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
class Solution {
public:

    // [] -> [[]]
    // [1] -> [[], [1]]
    // [1,2] -> [[], [1], [2], [1,2]]
    // 如果输入的vector有n个不同元素, 则一共有2^n 个排列
    // 假设输入[1,2,3], 那么产生8个组合
    // [] 1 2 3
    //  8 4 2 1 ----4 bits
    //  1 0 0 0 ---- number 7, put []
    //  0 1 1 1 ---- number 6, put 1 2 3
    //  
    // [[]]
    // [[], [1]]
    // [[], [1], [2], [1,2]]
    vector<vector<int> > subsets(vector<int>& v)
    {
        vector<vector<int> > res = {{}};
        vector<int> sender;
	    for (int i = 1; i < pow(2, v.size()); i++){
		    int tmp = i; 
    		for(int j = 0; j < v.size(); j++){
    			if(tmp%2 == 1) 
    			    sender.push_back(v[v.size()-1-j]);//v[3-1-0] = v[2] = 3
    			tmp >>= 1; 
    		}
    		res.push_back(sender);
    		sender.clear();
	    }
	    return res;
    }


/*
    void helper(vector<int> nums, vector<vector<int> > &smaller){
    	if (nums.size() == 0)
    		return;
    		
    	int extra = nums.back();
    	nums.pop_back();
    	helper(nums, smaller);

    	vector<vector<int> > newV;
    	for(vector<int> i : smaller)
    	{
    		i.push_back(extra);
    		newV.push_back(i);
		}
    	for (vector<int> i : newV)
    		smaller.push_back(i);

	}
    vector<vector<int> > subsets(vector<int>& nums) {
        vector<vector<int> > v = {{}};
        sort(nums.begin(), nums.end());
        helper(nums, v) ;
        return v;
    }
*/    
};

***********************201. Bitwise AND of Numbers Range*****************************
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        //solution 1
/*      int val1(m), val2(n), cnt1(0), cnt2(0);
        while(val1 || val2){   
            if(val1) {
                val1 >>= 1; cnt1++;
            }
            if(val2){
                val2 >>= 1; cnt2++;
            }
        }
        if(cnt1 != cnt2) return 0; //如果m和n的最高非零位的位置不同，则最后结果为0
        int res = ~0;
        for (int i = m; i <= n; i++){
            res &= i;
        }
        return res;
        */ //solution2 /////////////////////////////////////////////////////////////////////////////////////////////
        //从m到n，如果某位bit曾经变化过，那么这位Bit在AND后将会变成0（只要有一个0存在，那么AND所有数的结果也是0）
        //因为n>=m, 所以n的最高非0位的位置高于m的最高非0位
        //假设    n : 00001xxxxxxx...
        //        m : 0000001xxxxx...
        //mask = n^m: 00001xxxxxxx...， 从m XOR n可知二者的最高的不同的位
        //mask变为  ：000011111111...,  by : mask|=(mask>>1),mask|=(mask>>2), mask|=(mask>>4),mask|=(mask>>8), mask|=(mask>>16);
        //再~操作变为:111100000000...   mask ~= mask;
        //mask&m    : 000000000000... 为最后结果
        //或者假设n : 0000111xxxxx...
        //        m : 0000110xxxxx...
        //mask = n^m: 0000001xxxxx...
        //接下来mask: 000000111111...
        //然后mask  : 111111000000...
        //mask&m(n) : 000011000000... 为最后结果
        /*
        int mask = m^n;
        mask|=(mask>>1),mask|=(mask>>2), mask|=(mask>>4),mask|=(mask>>8), mask|=(mask>>16);
        return (~mask) & m;
        */
        ////solution 3 /////////////////////////////////////////////////////////////
		//e.g., m = 0000 1111 1001 0110
		//		n = 0000 1111 1101 1101
		//现在就是要得到从右边开始，相同的那些1位
        int cnt = 0;
        while(m!=n){
            m>>=1;n>>=1;cnt++; //m和n同时向右移动1位,同时记录移动的位数，直到m==n为止
        }
        if(!m) return 0;//如果m==n==0，那么返回0（m和n的right-most的1的位置不同）
        return m<<cnt;//否则把cnt的变化移回去，就是原来m和n相同的高位部分
    }
};
***********************318. Maximum Product of Word Lengths*****************************
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
class Solution {
public:
    int maxProduct(vector<string>& words) {
        //pre-process the words, convert each word to a number
        vector<int> nums;
        for(string &s:words){
            int tmp = 0;
            for(char c: s){
                tmp |= 1 << (c-'a');
            }
            nums.push_back(tmp);
        }
        //check if (nums[i] & nums[j]) == 0, 注意括号！
        //update maxLength
        int maxLength = 0;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i+1; j < nums.size(); j++){
                if( (nums[i] & nums[j]) == 0 ){
                    int size = words[i].size() * words[j].size();
                    maxLength = max( size, maxLength);
                }
            }
        }
        return maxLength;
    }
};
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
****************************************************
class Solution {
public:

    int majorityElement(vector<int>& nums) {
        int res = 0, mask = 1;
        for(int i = 0; i < 32; i++){
            int count = 0;
            for(int num : nums){
                if((mask & num) != 0)
                    count++;
                if(count > nums.size()/2){
                     res |= mask;
                     break;
                }
            }
            mask <<= 1; 
        }
        return res;
    }
};

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0], cnt = 1;
        for(int i = 1; i < nums.size(); i++){
            if(cnt == 0){
                candidate = nums[i];
                cnt++;
                continue;
            }
            if(nums[i] == candidate)
                cnt++;
            else{
                cnt--;
			}
        }
        return candidate;
    }
};