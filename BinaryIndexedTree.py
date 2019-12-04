''' Binary Indexed Tree '''
nums = [2,3,1,5,6,7,-1,4]
#binary indexed tree

#build a BIT from a number list
def build(nums):
    bitt = [0]*(len(nums)+1) # # of tree node is n+1
    for i in range(len(nums)):
        update(bitt, i+1, nums[i]) #BIT[0] is dummy node
    return bitt

#update the BIT[i] with val (BIT[i]+=val)        
def update(bitt, i, val):
    while i < len(bitt):
        bitt[i] += val
        i += i&(-i) #find the next node need to be added
        
# return sum(nums[:idx]        
def summ(nums, idx):
    bitt = build(nums)
    res = 0
    while idx:
        res += bitt[idx]
        idx -= idx&(-idx)
    return res
        
#%%  
bitt = build(nums)
print "binary indexed tree generated: "
print bitt
#%%
print "sums of nums by using a BIT"
for i in range(len(nums)+1):
    print summ(nums, i),

#%%
print 
res = [0]
for i in range(len(nums)):
    res.append(res[-1] + nums[i])
print "sums of nums by conventional method"
print res