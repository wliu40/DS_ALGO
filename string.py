344. Reverse String
class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size()-1;
        while(i < j){
            swap(s[i++], s[j--]);
        }
        return s;
    }
};

class Solution(object):
    def reverseString(self, s):
        return s[::-1]
		# do you know differce of s[::-1] and s.reverse()
		
*****************************************************	
6. ZigZag Conversion
class Solution {
public:
    string convert(string s, int numRows) {
        /*
            P       A       H       N
              A   P   L   S   I   I   G
                Y       I       R
        index如下：    
            0       4       8       12
              1   3   5   7   9   11   13
                2       6       10
        */
        
        if(numRows == 1) return s;
        vector<string> rows(numRows); //创造三行string
        int direction = -1, row_num = 0;
        for(int i = 0; i < s.size(); i++){
            if( i%(numRows-1) == 0 )
                direction *= -1; //控制方向
            rows[row_num].push_back(s[i]);
            row_num += direction;
        }
        string res = "";
        for(auto &s: rows){ //三行string加入最后结果
            res += s;
        }
        return res;
    }
};

*****************************************************	
13. Roman to Integer
class Solution {
public:

    /*
    罗马数字共有7个，即Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）。
    按照下述的规则可以表示任意正整数。需要注意的是罗马数字中没有“0”，与进位制无关。
    重复数次：一个罗马数字重复几次，就表示这个数的几倍。
    右加左减：
    在较大的罗马数字的右边记上较小的罗马数字，表示大数字加小数字。
    在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字。
    */
    int romanToInt(string s) {
        unordered_map<char, int> T = { { 'I' , 1 },
                                   { 'V' , 5 },
                                   { 'X' , 10 },
                                   { 'L' , 50 },
                                   { 'C' , 100 },
                                   { 'D' , 500 },
                                   { 'M' , 1000 } };
                                       
       int sum = T[s.back()];
       //从最后一位开始，比较倒数第二位与倒数第一位的大小，小于则减去，大于则加上
       //依次向前比较相邻位，直到第一位
       for (int i = s.length() - 2; i >= 0; --i) {
           if (T[s[i]] < T[s[i + 1]]){
               sum -= T[s[i]];
           }
           else{
               sum += T[s[i]];
           }
       }
       return sum;
    }
};
*****************************************************	
151. Reverse Words in a String
Given s = "the sky is blue",
return "blue is sky the".
class Solution {
public:
    void reverseWords(string &s) {
        /*清洗s的两段，去掉空格*/
        int begin = s.find_first_not_of(' ');
        if (begin == string::npos){ //说明全是空格
            s = "";
            return;
        }
        //找到词尾的第一个非空格字符的位置
        int end = s.find_last_not_of(' ');
        
        string ans = "";
        int cur = end;
        while (cur >= begin)
        {
            //从end开始倒着找到第一个空格
            cur = s.find_last_of(' ', cur);
            ans += s.substr(cur + 1, end-cur);//取出substr
            ans += ' '; //加空格分开各个单词
            //忽略原字符串中的词间空格
            while (s[cur] == ' ')
                cur--;
            //更新end
            end = cur;
        }
        //erase the last ' '
        ans.pop_back();
        s = ans;
    }
};
class Solution(object):
    def reverseWords(self, s):
        str_list = s.strip().split(" ")
        str_list = filter(lambda x:x!='', str_list)
        res = " ".join(str_list[::-1])
        return res
      
*****************************************************	
3. Longest Substring Without Repeating Characters
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
            遍历string, 
            1.更新start
            2.更新charmap
            3.更新maxlength
        */
        //e.g., string s = "abcdac";
        //前四轮，charMap[a]=0, charMap[b]=1,charMap[c]=2,charMap[d]=3,
        //因为目前为止未曾出现重复元素，所以start还是-1， maxLength=3-(-1)=4
        //到第五轮，出现重复的a,charMap[a]=0>-1, start更新为0
        //同时更新charMap[a]=4,maxLength仍为4
        //第六轮，再次出现重复元素，start变为2, 但是这一次没有更新maxLength
        
         //build a charMap, map each char to -1 initially
        vector <int> charMap(256, -1);
        int maxLength = 0;
        int start = -1;
        for(int i = 0; i < s.size(); i++){
            //i是现在的指针的位置，如果你站在i的位置往回走，在碰到重复元素之前最多能走多少步？i-start
            //If we found a repeated char, then, update start
            start = max(charMap[s[i]], start);
            //map each char to the current index
            charMap[s[i]] = i;
            //update max length
            maxLength = max(i-start, maxLength); 
        }
        return maxLength;
    }        
};
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charMap = [-1]*256
        maxLength, start = 0, -1
        for i in range(len(s)):
            start = max(charMap[ord(s[i])], start)
            charMap[ ord(s[i]) ] = i
            maxLength = max(maxLength, i-start)
        return maxLength
		
a = "abcdABCD"
print [ord(i) for i in a]	#[97, 98, 99, 100, 65, 66, 67, 68]
*****************************************************	
5. Longest Palindromic Substring
class Solution {
public:
    string longestPalindrome(string s) {
        
        int maxlength = 0;
        string res = "";
        for(int i = 0; i < s.size(); i++){
            //假如...cabac...奇对称
            //........i.....
            int j = i, k = i;
            while(j>=0 && k <s.size() && s[j]==s[k]) { j--;k++;}
            //假如...cabbac...偶对称
            //........i.....
            int jj = i, kk=i+1;
            while(jj>=0 && kk<s.size() && s[jj] == s[kk]) {jj--;kk++;}
            //比较哪种方法得到的回文字符串更长
            if(kk-jj > k-j && kk-jj-1 > maxlength){
                maxlength = kk-jj-1;
                res = s.substr(jj+1, maxlength);
            }
            else if(kk-jj < k-j && k-j-1 > maxlength){
                maxlength = k-j-1;
                res = s.substr(j+1, maxlength);
            }
        }
        return res;
    }
};
*****************************************************	
38. Count and Say
class Solution {
public:
    string countAndSayHelper(string s){
        string result = "";
        int i = 0, j = 0;
        while (i < s.length()){
            while (j < s.length() && s[j] == s[i])
                j++;
            result += to_string(j - i) + s[i];
            i = j;
        }
        return result;
    }

    string countAndSay(int n){
        string result = "1";
        for (int i = 0; i < n - 1; i++) {
            result = countAndSayHelper(result);
            //cout << result << endl;
        }
        return result;
    }
};
*****************************************************	
class Solution {
public:
    bool isValid(string s) {
        stack<char> sk;
        
        for (char c: s){
		    if (sk.empty() && (c == ')' || c == '}' || c == ']'))
			    return false;			   
            if (c == '(' || c == '{' || c == '[')
                sk.push(c);
            
            else if (c == ')' && sk.top() == '(')           
                sk.pop();        
            
            else if (c == ']' && sk.top() == '[')
                sk.pop();
            
            else if (c== '}' && sk.top() == '{')
                sk.pop();
            
            else
                return false;
        }
        return sk.empty();
    }
};
*****************************************************	
14. Longest Common Prefix
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0)
            return "";
        
        int index = 0;
        while (1) {
            char c = strs[0][index];
            for (string &s : strs) {
                if(index == s.size())
                    return s;
                if (s[index] != c )
                    return s.substr(0, index);
            }
            index++;
        }        
        return "";        
    }
};
*****************************************************	
10. Regular Expression Matching
class Solution(object):
    def isMatch(self, s, p):
        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        ''' table 'aab', 'c*a*b' 注意table多出一行一列，即p[i]对应的是table[i+1][j+1]
           '' a a b    
         '' 1 0 0 0 分别是空对空, a, aa, aab
         c  0 0 0 0 分别是c对空，a, aa, aab, p[i]!=*,如上对角为假，本列元素必为假;如上对角为真，当p[i]==s[i]或者p[i]=='.'，为真
         *  1 0 0 0 分别是c*对空, a, aa, aa, p[i]=='*',则本列上一行或者上两行为真，则下一行的本列为真
         a  0 1 0 0 分别是c*a对空,a, aa, aab
         *  1 1 1 0
         b  0 0 0 1
        
        '''
        table[0][0] = True
        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous.
        #'':'a*', return True,'':'a*a*' return True, '':'a*a*a' return False
        #'':'c*' return True, '':'cc*' return False
        for i in range(1, len(p) ):#初始化第一列
            table[i+1][0] = table[i-1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] != "*": #匹配前一个字符0次或无限次或者消除前面一个字符
                    # Update the table by referring the diagonal element.
                    if table[i][j] == False:#如果前面不匹配，则无论当前如何，一定不匹配
                        table[i+1][j+1] = False
                    elif p[i] == s[j] or p[i] == '.': #如果table[i][j]为真，则当前字符相同或者当前为'.'
                        table[i+1][j+1] = True
                    #table[i+1][j+1] = table[i][j] and (p[i] == s[j] or p[i] == '.')
                else:
                    #'*'的作用1)消去前面的字符；2)无作用,如'a*b'匹配'ab'
                    table[i+1][j+1] = table[i-1][j+1] or table[i][j+1]
                    #'*'的作用3)可以充当前面字符无限多次，‘propagation’
                    if p[i-1] == s[j] or p[i-1] == '.':
                        table[i+1][j+1] |= table[i+1][j] #如： 'aaaaaab' 和'a*b'匹配或者'.*b匹配'
        return table[-1][-1]
*****************************************************	
49. Group Anagrams
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for(int i = 0; i < strs.size(); i++){
          
            string tmp=strs[i];
            sort(strs[i].begin(), strs[i].end());
            if(mp.find(strs[i]) != mp.end())
                mp[strs[i]].push_back(tmp);
            else
                mp[strs[i]] = vector<string>{tmp};
        }
        vector<vector<string>> res;
        for(auto it = mp.begin(); it != mp.end(); it++){
            res.push_back(it->second);
        }
        return res;
        
    }
};
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        for s in strs:
            tmp = "".join(sorted(s))
            dic[tmp].append(s)
        return dic.values()
*****************************************************	
17. Letter Combinations of a Phone Number
class Solution {
public:   
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return vector<string>{};
        string charmap[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res {""};
        for(int i = 0; i < digits.size(); i++){
            vector<string> tmp;
            string s = charmap[digits[i]-'0'];
            for(string &str : res){
                for(char c : s){
                    tmp.push_back(str+c);
                }
            }
            res = tmp;
        }
        return res;
    }
};

*****************************************************	
67. Add Binary
class Solution {
public:
    string addBinary(string a, string b) 
    {
        int lena = a.size()-1, lenb = b.size()-1, tmpa, tmpb;
        string res = "";
        int carry = 0;
        while(lena>=0 || lenb>=0){
            tmpa = tmpb = 0;
            if(lena >=0){
                tmpa=a[lena--]-'0';
            }
            if(lenb>=0)
                tmpb = b[lenb--]-'0';
            res = to_string((tmpa+tmpb+carry)%2)+res;
            carry = (tmpa+tmpb+carry)/2;            
        }
        if(carry){
            res = to_string(carry)+res;
        }
        return res;
    }
};

class Solution(object):
    def addBinary(self, a, b):
        numa = int(a,2)
        numb = int(b,2)
        return str(bin(numa+numb))[2:]
        
*****************************************************	
22. Generate Parentheses
class Solution {
public:
    void backtrack(vector<string> &res, string s, int open, int close, int max){
        if(s.size() == max*2){
            res.push_back(s);
            return;
        }
        if(open < max)
            backtrack(res, s+"(", open+1, close, max);
        if(close < open)
            backtrack(res, s+")", open, close+1, max);
        
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string s = "";
        backtrack(res, s, 0, 0, n);
        return res;
    }
};
*****************************************************	
8. String to Integer (atoi)
class Solution {
public:
    int myAtoi(string str) {
        if(str.empty())
            return 0;
        long result = 0;
        int indicator = 1;
        int i = str.find_first_not_of(' ');
        if(str[i] == '-' || str[i] == '+')
            indicator = (str[i++] == '-')? -1 : 1;
        while('0' <= str[i] && str[i] <= '9')
        {
            result = result*10 + (str[i++]-'0');
            if(result*indicator >= INT_MAX) return INT_MAX;
            if(result*indicator <= INT_MIN) return INT_MIN;
        }        
        return result*indicator;
    }
};

*****************************************************	
72. Edit Distance
class Solution {
public:
    int findMin(int a, int b, int c)
    {
        int temp = (a <= b)? a:b;
        return (temp <= c)? temp:c;
    }
    int minDistance(string word1, string word2) 
    {
        //polynomial, exponential
        //    p o l y n o ..
        //  0 1 2 3 4 5 6 ..
        // e1 1 2 3 4 5 6 ..
        // x2 2 2 3 4 5 6 ..
        // p3 2 3 3 4 5 6 ..
        // o4 3 2 3 4 5 5 ..
        // .. . . . . . . ..
        int row = word1.size() + 1;
        int col = word2.size() + 1;
        
        //构建一个二维matrix,注意行数，列数
        int **matrix = new int*[row];
        for (int i = 0 ; i < row; i++)
        {
            matrix[i] = new int[col];
        }
        //第一行填0,1,2,3,4...
        for (int i = 0; i < row; i++)
        {
            matrix[i][0] = i;
        }
        //第一列填0,1,2,3,4...
        for (int j = 0; j < col; j++)
        {
            matrix[0][j] = j;
        }
        //动态求解 matrix[i,j] = min（左,右,上）+diff(matrix[i], matrix[j])
        //matrix[i] == matrix[j]=>diff = 0, otherwise, diff = 1;
        int diff = 0;
        for (int i = 1; i < row; i++)
        {
            for (int j = 1; j < col; j++)
            {
                diff = (word1[i-1] == word2[j-1])? 0:1;
                matrix[i][j] = findMin(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + diff);
            }
        }
        return matrix[row-1][col-1];
    }
};
*****************************************************	
345. Reverse Vowels of a String
class Solution {
public:
    string reverseVowels(string s) {
        int head = 0, tail = s.size()-1;
        while(1){
            head = s.find_first_of("aeiouAEIOU", head);
            tail = s.find_last_of("aeiouAEIOU", tail);
           // cout << head << tail << endl;
            if(head >=tail) break;
            swap(s[head++], s[tail--]);
        }
        return s;
    }
};
*****************************************************	
28. Implement strStr()
class Solution {
public:

    int strStr(string haystack, string needle) {
        if(haystack.empty()){
            if(needle.empty()) return 0;
            return -1;
        }
        if(haystack.size() < needle.size() ) return -1;
        for(int i = 0; i <= haystack.size()-needle.size(); i++ ){
            //cout << "@" << endl;
            int j = 0;
            while(i+j < haystack.size() && haystack[i+j] == needle[j]){
                j++;
            }
            if(j == needle.size())
                return i;
        }
        return -1;
    }
};
*****************************************************	
115. Distinct Subsequences
class Solution {
public:

    //DP
    /*
      S 0123....j
    T +----------+
      |1111111111|
    0 |0         |
    1 |0         |
    2 |0         |
    . |0         |
    . |0         |
    i |0         |
    对于matrix[i][j]而言，如果t[i] == s[j], 则matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1]
                          如果t[i] != s[j]，则matrix[i][j] = matrix[i][j-1]
      e.g.,                    
        S: [acdabefbc] and T: [ab]
            a c d a b e f b c
          1 1 1 1 1 1 1 1 1 1
        a 0 1 1 1 2 2 2 2 2 2
        b 0 0 0 0 0 2 2 2 4 4

    */
    int numDistinct(string s, string t) {
        //初始化matrix
        int rowCount = t.size()+1, colCount = s.size()+1;
        vector<vector<int>> matrix (rowCount, vector<int>(colCount, 0));
        
        fill(matrix[0].begin(), matrix[0].end(), 1);

        //Danamic programming
        for(int i = 1; i < rowCount; i++ ){
            for(int j = 1; j < colCount; j++){
                if(t[i-1] == s[j-1])
                    matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1];
                else
                    matrix[i][j] = matrix[i][j-1];
            }
        }
        return matrix.back().back();        
    }
};
*****************************************************	
273. Integer to English Words
class Solution {
public:
    string belowTen[10] = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    string belowTwenty[10] =  {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    string belowHundred[10] = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        return helper(num); 
    }
    
private:    
    string helper(int num) {
        //按照从小到大的次序排列if/else
        string result;
        if (num < 10) result = belowTen[num];
        else if (num < 20) result = belowTwenty[num -10];
        else if (num < 100) result = belowHundred[num/10] + " " + helper(num % 10);
        else if (num < 1000) result = helper(num/100) + " Hundred " +  helper(num % 100);
        else if (num < 1000000) result = helper(num/1000) + " Thousand " +  helper(num % 1000);
        else if (num < 1000000000) result = helper(num/1000000) + " Million " +  helper(num % 1000000);
        else result = helper(num/1000000000) + " Billion " + helper(num % 1000000000);
        if(result.back() == ' ')
            result.pop_back();
        return result;
    }
};
*****************************************************	
336. Palindrome Pairs
class Solution {
public:
    /*
    Case1: If s1 is a blank string, then for any string that is palindrome s2, s1+s2 and s2+s1 are palindrome.
    Case 2: If s2 is the reversing string of s1, then s1+s2 and s2+s1 are palindrome.
    for 'abc', if there also a 'cba' exist, then we find a pair
    Case 3: If s1[0:cut] is palindrome and there exists s2 is the reversing string of s1[cut+1:] , then s2+s1 is palindrome.
    for 'abac' if there is a 'c' exist, then 'c' + 'abac' is palindrome
    for 'caba' if there is a 'c', then 'caba'+'c' is palindrome
    
    for '/abc'  we search 'cba'
    for 'a/bc'  we search 'cb'
    for 'ab/c'  we donot need search, since 'ab' is not palindrome
    
    for '/abbac' we search 'cabba'
    for 'a/bbac' we search 'cabb'
    for 'ab/bac' we donot search, since 'ab' is not palindrome
    for 'abb/ac' we donot search
    for 'abba/c' we search 'c' for left side, we search 'abba' for right side
    
    for 'babcec' we have to search 'cecbab', 'cecba','cec','bab' and 'ecbab'
    */
    vector<vector<int>> palindromePairs(vector<string>& words) {
        unordered_map<string, int> mp;
        vector<vector<int>> res;
        for(int i = 0; i < words.size(); i++){
            mp[words[i]] = i;
        }
        vector<int> palindroms; //all the palindrom words, such as "aba", "a", "abba", etc
        bool has_space = false;
        int space_pos = 0;
        if(mp.find("") != mp.end()){
            has_space = true;
            space_pos = mp[""];
        }
            
        for(int i = 0; i < words.size(); i++){
            for(int j = 0; j < words[i].size(); j++){
                string left = words[i].substr(0, j);
                string right = words[i].substr(j);
                if(is_palm(left)){
                    reverse(right.begin(), right.end());
                    auto it = mp.find(right);
                    if( it != mp.end() && it->second != i){
                        res.push_back(vector<int>{it->second, i});
                    }
                }
                if(is_palm(right)){
                    if(has_space && j == 0){
                        palindroms.push_back(i);
                    }
                    reverse(left.begin(), left.end());
                    auto it = mp.find( left);
                    if( it != mp.end() && it->second != i){
                        res.push_back(vector<int>{i, it->second});
                    }
                }
                
            }
        }
        if(has_space){
            for(int i:palindroms){
                res.push_back(vector<int>{space_pos, i});
            }
        }
        
        return res;
         
    }
    bool is_palm(string &s){
        int i = 0, j = s.size()-1;
        while(i < j){
            if(s[i++] != s[j--])
                return false;
        }
        return true;
    }
};

class Solution(object):
    def palindromePairs(self, words):
        dic = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in xrange(len(word)):
                prefix, postfix = word[:j], word[j:]
                if prefix == prefix[::-1]:
                    target = postfix[::-1]
                    if target in dic and dic[target] != i:
                        res += [[dic[target], i]]
                if postfix == postfix[::-1]:
                    if j == 0 and "" in dic:
                        res += [[dic[""], i]]
                    target = prefix[::-1]
                    if target in dic and dic[target] != i:
                        res += [[i, dic[target]]]
        return res 
        
    def is_palm(self, s): #pythonic way of checking palindrome
        return s == s[::-1]

            
*****************************************************	
43. Multiply Strings
class Solution {
public:
    string multiply(string num1, string num2) {
        
        string sum(num1.size() + num2.size(), '0');
        //跟两个string相加的方法差不多，
        //原来是num = (num1+num2+carry)%10, 现在这个只是增加了一个原来的sum[i+j+1]位
        // int tmp = (sum[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry;
        for (int i = num1.size() - 1; i >= 0; --i) {
            int carry = 0;
            for (int j = num2.size() - 1; 0 <= j; --j) {
                int tmp = (sum[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry;
                sum[i + j + 1] = tmp % 10 + '0';
                carry = tmp / 10;
            }
            sum[i] += carry;            
        }
        
        size_t startpos = sum.find_first_not_of("0");
        if (string::npos != startpos) 
            return sum.substr(startpos);
        
        return "0";
    }
    
};

*****************************************************	
383. Ransom Note
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int charmap[26] = {0};
        for(char c : magazine){
            charmap[c-'a']++;
        }
        for(char c: ransomNote){
            charmap[c-'a']--;
            if(charmap[c-'a'] < 0)
                return false;
        }
        return true;
    }
};
*****************************************************	
165. Compare Version Numbers
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int num1, num2;
        char *pos1, *pos2;
        const char *s1 = version1.c_str();
        const char *s2 = version2.c_str();
        
        while(s1 - version1.c_str() < version1.size()  ||  s2 - version2.c_str() < version2.size()){
            if(s1 - version1.c_str() < version1.size()){ // the same as if( *s1 )
                num1 = strtol(s1, &pos1, 10); //pos1是'.'的位置，或者是最后一个字符的位置
                s1 = pos1+1;
            }
            else            
                num1 = 0; //如果一个数已经结束了，而另一个数还没有结束，那么结束的数用0代替，比如：1.0和1.0.0.0是相等的版本            
            
            if(s2 - version2.c_str() < version2.size()){
                num2 = strtol(s2, &pos2, 10);
                s2 = pos2+1;
            }
            else           
                num2 = 0;            
            
            if(num1 > num2) //如果num1大于num2，提前结束
                return 1;
            else if (num1 < num2)
                return -1;
        }
        return 0;
    }
    
};
*****************************************************	
125. Valid Palindrome
class Solution {
public:
    bool isPalindrome(string s) {
         
        int cnt1 = 0;
        int cnt2 = s.size()-1;
        while(cnt1 < cnt2)
        {
            //skip none-alphanumerical chars
            while (cnt1 < s.size() && !isalnum(s[cnt1]) )
                cnt1++;
            //skip none-alphanumerical chars
            while (cnt2 >=0 && !isalnum(s[cnt2]) )
                cnt2--;
            //when they meet, end the loop
            if (cnt1 >= cnt2)
                break;
            //if they donot meet yet, check their value, remember tolower or toupper before comparison
            if ( tolower(s[cnt1]) != tolower(s[cnt2]) )
                return false;
            //increase and decrease the index
            cnt1++;
            cnt2--;
        }
        return true;
    }
};

*****************************************************	
214. Shortest Palindrome
class Solution {
public:
    /****用KMP算法****/
    //关于KMP:http://blog.csdn.net/v_july_v/article/details/7041827
    //              s = "a b a"
    //KMP next[]表为   0 0 0 1        
    //              s = "a b c d e a b c" 
    //KMP next[]表为   0 0 0 0 0 0 1 2 3
    
    //              s = "a b a d e a b a"
    //KMP next[]表为   0 0 0 1 0 0 1 2 3
    
    //              s = "a b c d e c b a"
    //KMP next[]表为   0 0 0 0 0 0 0 0 1         
    //  假设s = "a b c b a d e"
    //现在构造ss = s+'*'+reverse(s)
    //     ss = "a b c b a d e * e d a b c b a"
    //next[]表 0 0 0 0 1 2 0 0 0 0 0 1 2 3 4 5
    //则ss的前缀回文字符串的长度为5, ss.substr(0,5) = "abcba"
    //相应的，加上"edabcba"的substr(0,7-5) = "ed" 即可
    
    //给一个string s, 返回s的KMP next[]表
    void get_next(vector<int> &next, const string &s){
        for(int j = 1; j < s.size(); j++){
            int k = next[j];
            while(k && s[j] != s[k])
                k = next[k];
            next[j+1] = (s[j] == s[k])? k+1 : 0;
        }
    }
    string shortestPalindrome(string s){
        //构建辅助字符串ss
        string rev_s = s;
        reverse(rev_s.begin(), rev_s.end());
        string ss = s + "*" + rev_s;
        //计算ss的next表
        vector<int> next(ss.size()+1, 0);
        get_next(next, ss);
        //得到原来s中的前缀回文的长度=next.back()
        return rev_s.substr(0, s.size()-next.back()) + s;
         
    }
};
*****************************************************	
65. Valid Number
class Solution {
public:
    bool isNumber(string s) {
        
        string s1="+-.e";//only those chars (except digits) will be allowed
       
        //stripping the leading and trailing spaces ...
        int begin = s.find_first_not_of(" ");
        if (begin == string::npos)
            return false;//no content
        int end = s.find_last_not_of(" ");
        s = s.substr(begin, end-begin+1);
       
        bool pointSeen = false;
        bool eSeen = false;
        bool numberSeen = false;
        
   
        if (s.back() == 'e'||s.back() == '+' || s.back() == '-') return false;
        for(int i=0; i<s.length(); i++) {
            if('0' <= s.at(i) && s.at(i) <= '9') //seen number already
                numberSeen = true;
            
            else if(s.at(i) == '.') {
                if(eSeen || pointSeen) return false; //'.' should not be ahead of 'e'
                pointSeen = true;
            } 
            else if(s.at(i) == 'e') {
                if(eSeen || !numberSeen) return false; //'e' should not appear before number
                eSeen = true;
            } 
            else if(s.at(i) == '-' || s.at(i) == '+') {
                if(i != 0 && s.at(i-1) != 'e') return false;//if '+' or '-' not zero index, and 'e' not in s[i-1]
            } 
            else return false;// other chars will lead to false
        }
        return numberSeen;
	}
};
*****************************************************	
58. Length of Last Word
class Solution {
public:
    int lengthOfLastWord(string s) {
        int end = s.find_last_not_of(" ");
        if(end == string::npos) return 0;
        int start = s.find_last_of(" ", end);
        return end-start;
    }
};
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	

*****************************************************	