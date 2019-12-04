# -*- coding: utf-8 -*-
"""
Created on Mon Jan 07 16:14:32 2019

@author: cgyy2
"""

''' sorting methods'''
#%%
# bubble sort

#%%
# insert sort

#%%
def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater

arr = [2,1,0,5,10,2,-1,32]
print quicksort(arr) 
#%%
import operator
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)


arr = [2,1,0,5,10,2,-1,32]
print mergeSort(arr)

#%%

def heapify(arr, n, i): 
    print i, '#'
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        print '$$'
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        print '$$'
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n-1, -1, -1): 
        print arr, '@', i
        heapify(arr, n, i) 
    print arr, '------'
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
    return arr
        

arr = [2,1,0,5,10,2,-1,32]
print heapSort(arr)

#%%
def pigeonhole_sort(a):
    mi = min(a)
    size = max(a) - mi + 1
    holes = [0]*size
    for x in a:
        holes[x - mi] += 1
    i = 0
    for count in xrange(size):        
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + mi
            i += 1
    return a

arr = [2,1,0,5,10,2,-1,32]
print pigeonhole_sort(arr)      

#%%
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1



#%%
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1      