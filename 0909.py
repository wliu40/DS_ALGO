# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 15:00:55 2019

@author: cgyy2
"""


def foo(res, n):
    if not n:
        return ""

    if n % 2:
        s = "1"
    else:
        s = '0'
    res[0] += s
    return foo(res, n / 2)


def foo2(n):
    res = ""
    while n:
        res += str(n % 2)
        n /= 2
    return res


# %%
res = [""]
foo(res, 162212)
print '0b' + res[0][::-1]

print bin(162212)

print '0b' + foo2(162212)[::-1]


# https://www.geeksforgeeks.org/generating-all-possible-subsequences-using-recursion/
# https://www.geeksforgeeks.org/generating-subarrays-using-recursion/
# %%
def subsets(nums):
    ## recursive
    res = []

    def helper(tmp, nums, start):
        res.append(tmp[:])
        # print "range: {} to {}".format(start, len(nums))
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            # print "add {}".format(nums[i])
            print "calling helper({}, nums, {})".format(tmp, i + 1)
            helper(tmp, nums, i + 1)
            # print "pop {}".format(tmp[-1])
            tmp.pop(-1)

    helper([], nums, 0)
    return res


arr = [1, 2, 3]
print subsets(arr)

# %%
print subsets(arr)

"""

calling helper([1], nums, 1)
    calling helper([1, 2], nums, 2)
        calling helper([1, 2, 3], nums, 3)
    calling helper([1, 3], nums, 3)
calling helper([2], nums, 2)
    calling helper([2, 3], nums, 3)
calling helper([3], nums, 3)

[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

"""


# %%
def printSubsequences(subarr, arr):
    # Print the subsequence when reach  
    # the leaf of recursion tree 

    # Condition to avoid printing
    # empty subsequence
    # if len(subarr) != 0:
    print(subarr)

    for index in range(len(arr)):
        # Subsequence without including  
        # the element at current index 
        # print "call printSubsequences({}, arr, {})".format(subarr, index+1)
        # printSubsequences(subarr, arr[index+1:])

        # Subsequence including the element 
        # at current index 
        print "call printSubsequences({}, {})".format(subarr + [arr[index]], arr[index + 1:])
        printSubsequences(subarr + [arr[index]], arr[index + 1:])
    return


arr = [1, 2, 3]
printSubsequences([], arr)


# %% permutation I
# generate all the permutations of an array
# no duplicate element in this array
def permutations(arr):
    res = []

    def helper(tmp, start):
        if start == len(arr) - 1:
            res.append(tmp[:])
        for i in range(start, len(arr)):
            tmp[start], tmp[i] = tmp[i], tmp[start]
            helper(tmp, start + 1)
            tmp[start], tmp[i] = tmp[i], tmp[start]

    helper(arr, 0)
    return res


arr = [1, 2, 3]
print permutations(arr)


# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
# %% permutation II
# Input: [1,1,2]
# Output:
# [[1,1,2],[1,2,1],[2,1,1]]
def permutations_2(arr):
    res = []
    arr = sorted(arr)

    def helper(tmp, start):
        if start == len(arr) - 1:
            res.append(tmp[:])
        for i in range(start, len(arr)):
            if i != start and tmp[i] == tmp[start]:
                continue
            tmp[start], tmp[i] = tmp[i], tmp[start]
            helper(tmp, start + 1)
            tmp[start], tmp[i] = tmp[i], tmp[start]

    helper(arr, 0)
    return res


arr = [1, 2, 1, 1]
permutations_2(arr)


# %%Combination Sum
def combinationSum(candidates, target):
    res = []
    candidates = sorted(candidates)

    def helper(tmp, start, target):
        if target == 0:
            res.append(tmp[:])
            return
        for j in range(start, len(candidates)):
            if candidates[j] > target:
                break
            tmp.append(candidates[j])
            helper(tmp, j, target - candidates[j])
            tmp.pop(-1)

    tmp = []
    helper(tmp, 0, target)
    return res


# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
# ]

# %%
def combinationSum2(candidates, target):
    res = set()
    candidates.sort()

    def helper(candidates, tmp, start, target):
        if target == 0:
            res.add(tuple(sorted(tmp[:])))
        for i in range(start, len(candidates)):
            # if i != start and candidates[start] == candidates[i]:
            #     continue
            if candidates[i] > target:
                break
            tmp.append(candidates[i])
            helper(candidates, tmp, i + 1, target - candidates[i])
            tmp.pop(-1)

    helper(candidates, [], 0, target)
    return list(res)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print combinationSum2(candidates, target)


# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
# %%
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
def combinationSum3(k, n):
    res = []

    def helper(tmp, start, target):
        if len(tmp) == k and target == 0:
            res.append(tmp[:])
        for i in range(start, 10):
            tmp.append(i)
            helper(tmp, i + 1, target - i)
            tmp.pop(-1)

    helper([], 1, n)
    return res


# %%
# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
# Therefore the output is 7.
def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    nums.sort()
    for i in range(target + 1):
        for j in nums:
            if i - j < 0:
                break
            dp[i] += dp[i - j]

    return dp[-1]


# %%
def parenthesis_gen(n):
    res = []

    def helper(tmp):
        if len(tmp) == n:
            res.append(tmp[:])
            return
        helper(tmp + ")")
        helper(tmp + "(")

    helper("")
    return res


print parenthesis_gen(2)


# ['))', ')(', '()', '((']
# write a checker function to check if this is a valid parenthesis combination

# %%
def parenthesis_gen(n):
    res = []

    def helper(tmp, left_count, right_count):
        if len(tmp) == n * 2:
            res.append(tmp[:])
            return
        if left_count < n:
            helper(tmp + "(", left_count + 1, right_count)
        if right_count < left_count:
            helper(tmp + ")", left_count, right_count + 1)

    helper("", 0, 0)
    return res


print parenthesis_gen(2)  # ['(())', '()()']


# %%
# You have a set of tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make.
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
def numTilePossibilities(tiles):
    res = [0]

    def recursion(tiles, curr):
        print curr,
        visited = set()
        for i, n in enumerate(tiles):
            # rint 'i={}, n={}'.format(i, n)
            if n in visited:
                continue
            visited.add(n)
            res[0] += 1
            print "call recursion({}, {})".format(tiles[:i] + tiles[i + 1:], curr + n)
            recursion(tiles[:i] + tiles[i + 1:], curr + n)

    recursion(tiles, "")
    return res[0]


arr = 'ABC'
print numTilePossibilities(arr)
# A AB ABC AC ACB B BA BAC BC BCA C CA CAB CB CBA 15
arr = 'ABA'
print numTilePossibilities(arr)
# A AB ABA AA AAB B BA BAA 8
call
recursion(BA, A)
A
call
recursion(A, AB)
AB
call
recursion(, ABA)
ABA
call
recursion(B, AA)
AA
call
recursion(, AAB)
AAB
call
recursion(AA, B)
B
call
recursion(A, BA)
BA
call
recursion(, BAA)
BAA
8


# %%
def numTilePossibilities(tiles):
    def recursion(tiles, curr):
        print curr,
        visited = set()
        for i, n in enumerate(tiles):
            # rint 'i={}, n={}'.format(i, n)
            # if n in visited:
            #    continue
            # visited.add(n)
            # print "call recursion({}, {})".format(tiles[:i]+tiles[i+1:], curr+n)
            recursion(tiles[:i] + tiles[i + 1:], curr + n)

    recursion(tiles, "")


arr = 'ABA'
print numTilePossibilities(arr)

#  call recursion(BA, A)
# A call recursion(A, AB)
# AB call recursion(, ABA)
# ABA call recursion(B, AA)
# AA call recursion(, AAB)
# AAB call recursion(AA, B)
# B call recursion(A, BA)
# BA call recursion(, BAA)
# BAA call recursion(A, BA)
# BA call recursion(, BAA)
# BAA call recursion(AB, A)
# A call recursion(B, AA)
# AA call recursion(, AAB)
# AAB call recursion(A, AB)
# AB call recursion(, ABA)
# ABA None
