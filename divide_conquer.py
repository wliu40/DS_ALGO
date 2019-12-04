# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:30:44 2019

@author: cgyy2
"""

# binary search

def bisearch(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)/2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return -1

print bisearch([0,1,5,6], 5) #2
print bisearch([0,1,5,6], 6) #3
print bisearch([-1,0,5,6,10,15,19], 1) #-1
print bisearch([-1,0,5,6,10,15,19], 19) #6

def bisearch_recursive(arr, target):        
    def helper(arr, l, r, target):
        if l > r:
            return -1
        mid = (l+r)/2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return helper(arr, mid+1, r, target)
        else:
            return helper(arr, l, mid-1, target)
    return helper(arr, 0, len(arr)-1, target)

print bisearch_recursive([0,1,5,6], 5) #2
print bisearch_recursive([0,1,5,6], 6) #3
print bisearch_recursive([-1,0,5,6,10,15,19], 1) #-1
print bisearch_recursive([-1,0,5,6,10,15,19], 19) #6
#%%

def find_first_missing_element(arr):
    def helper(arr, l, r):
        if l > r:
            return l
        mid = l + (r-l)/2
        if arr[mid] == mid:
            return helper(arr, mid+1, r)
        else:
            return helper(arr, l, mid-1)
    return helper(arr, 0, len(arr)-1)

print find_first_missing_element([0,1,2,4,7]) #3
print find_first_missing_element([0,1,2,3,4]) #5
print find_first_missing_element([1,2]) #0
#%%
# how to do circular indexing
arr = [1,2,3,4,5,6]
for i in range(len(arr)):
    pre = (i-1+len(arr)) % len(arr)
    post = (i+1+len(arr)) % len(arr)
    print pre, i, post

#5 0 1
#0 1 2
#1 2 3
#2 3 4
#3 4 5
#4 5 0
#%%
def find_smallest_number_in_rotated_array(arr):
    n = len(arr)-1
    l, r = 0, n
    while l <= r:
        if arr[l] <= arr[r]:
            return arr[l]
        mid =  l +(r-l)/2
        prev = (mid-1+n)%n
        post = (mid+1)%n
        if arr[mid] <= arr[prev] and arr[mid] <= arr[post]:
            return arr[mid]
        elif arr[mid] <= arr[r]:
            r = mid-1
        elif arr[mid] >= arr[l]:
            l = mid+1
    return -1
print find_smallest_number_in_rotated_array([7,8,9,0,2,3,4,5]) #0
print find_smallest_number_in_rotated_array([4,8,9,0]) #0
print find_smallest_number_in_rotated_array([0,4,8,9]) #0

#%%

def find_insert_position(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r-l)/2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l
print find_insert_position([0,1,5], 3) #2
print find_insert_position([0,1,5], -1) #0
print find_insert_position([0,1,5], 8) #3
print find_insert_position([0,1,5, 7], 6) #3
#%%

def search_in_rotated_array(nums, target):
    if not nums:
        return -1
    
    def bisearch(arr, l, r, target):
        while l <= r:
            mid = l+(r-l)/2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return -1
    
    if nums[0] < nums[-1]:
        return bisearch(nums, 0, len(nums)-1, target)
    
    l, r = 0, len(nums)-1            
    # if l == r-1, it is time to break the loop
    while l < r-1:
        mid = l+(r-l)/2
        if nums[l] < nums[mid]:
            l = mid
        else:
            r = mid
            
    if target >= nums[0]:
        return bisearch(nums, 0, l, target)
    else:
        return bisearch(nums, r, len(nums)-1, target)
    return -1
#%%

def find_peak_number(arr):
    l, r = 0, len(arr)-1
    while l < r:
        mid = l + (r-l)/2
        if arr[mid] < arr[mid+1]:
            l = mid+1
        else:
            r = mid
    return arr[l]

print find_peak_number([1,2,3,1])
print find_peak_number([1,2,1,3,5,6,4])
#%%
Find First and Last Position of Element in Sorted Array
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.empty() || target > nums.back()) return {-1,-1};
        int i = bs(nums, target);
        if(nums[i] != target) return {-1,-1};
        int j = bs(nums, target+1);        
        return {i, j-1};
    }
    int bs(vector<int> &nums, int target){
        int i = 0, j = nums.size();
        while(i < j){
            int mid = i + (j-i)/2;
            if(nums[mid] < target)
                i = mid+1;
            else
                j = mid;            
        }
        return i;
    }
};
#%%
"""
[5,7,9,11,15], return 13
[1,3,5,7,11], return 9
[,2,4,6] return 8?

""" 
class Search
{
	// Function to find missing term in a sequence
	public static int missingTerm(int[] A)
	{
		// search space is A[left..right]
		int left = 0, right = A.length - 1;

		// calculate common difference between successive elements
		int diff = (A[A.length - 1] - A[0]) / A.length;

		// run till search space is exhausted
		while (left <= right)
		{
			// find middle index
			int mid = right - (right - left) / 2;

			// check difference of mid element with its right neighbor
			if (mid + 1 < A.length && A[mid + 1] - A[mid] != diff) {
				return A[mid + 1] - diff;
			}

			// check difference of mid element with its left neighbor
			if (mid - 1 >= 0 && A[mid] - A[mid - 1] != diff) {
				return A[mid - 1] + diff;
			}

			// if missing element lies on left sub-array, then we reduce
			// our search space to right sub-array A[left..mid-1]
			if (A[mid] - A[0] != (mid - 0) * diff) {
				right = mid - 1;
			}

			// if missing element lies on right sub-array, then reduce
			// our search space to right sub-array A[mid+1..right]
			else {
				left = mid + 1;
			}
		}
		return -1;
	}

	public static void main(String[] args)
	{
		int[] A = { 5, 7, 9, 11, 15 };

		System.out.println("Missing element is " + missingTerm(A));
	}
}
