def subsetsum_target_recursion(i,target,arr):
   if target == 0:
       return True
   if i == 0:
       if arr[0] == target:
           return True
       else:
           return False
   notTake = subsetsum_target_recursion(i-1,target,arr)
   Take = False
   if arr[i] >= target:
       Take = subsetsum_target_recursion(i-1,target-arr[i],arr)
   if notTake is True or Take is True: return True
   return False

arr = [3, 2, 1]
print(subsetsum_target_recursion(len(arr)-1,2,arr))

def subsetsum_target_memoization(i,target,arr,dp):
   if target == 0:
       return True
   if i == 0:
       if arr[0] == target:
           return True
       else:
           return False
   if dp[i][target] != -1: return dp[i][target]
   notTake = subsetsum_target_memoization(i-1,target,arr,dp)
   Take = False
   if arr[i] >= target:
       Take = subsetsum_target_memoization(i-1,target-arr[i],arr,dp)
   dp[i][target] = False
   if notTake is True or Take is True:
       dp[i][target] = True
   return dp[i][target]

target  = 2
dp = [[-1]* (len(arr)+1) for _ in range(target+1)]
print(subsetsum_target_memoization(len(arr)-1,target,arr,dp))