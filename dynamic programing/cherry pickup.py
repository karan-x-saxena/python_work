def cherrypicup_recersion(i,j1,j2,mat,n,m):
    if j1 < 0 or j1 >= m+1 or j2 < 0 or j2 >= m+1:
        return -1000000
    if i == n:
        if j1 == j2:
            return mat[i][j1]
        else:
            return mat[i][j1]+mat[i][j2]
    maxi = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if j1 == j2:
                a = cherrypicup_recersion(i+1,j1+k,j2+l,mat,n,m) + mat[i][j1]
            else:
                a = cherrypicup_recersion(i+1,j1+k,j2+l,mat,n,m) + mat[i][j1] + mat[i][j2]
            maxi = max(maxi,a)
    return maxi

arr = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
n = len(arr)-1
m = len(arr[0])-1
print(cherrypicup_recersion(0,0,m,arr,n,m))

def cherrypicup_memoization(i,j1,j2,mat,n,m,dp):
    if j1 < 0 or j1 >= m+1 or j2 < 0 or j2 >= m+1:
        return -1000000
    if dp[i][j1][j2] != -1: return dp[i][j1][j2]
    if i == n:
        if j1 == j2:
            return mat[i][j1]
        else:
            return mat[i][j1]+mat[i][j2]
    maxi = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if j1 == j2:
                a = cherrypicup_memoization(i+1,j1+k,j2+l,mat,n,m,dp) + mat[i][j1]
            else:
                a = cherrypicup_memoization(i+1,j1+k,j2+l,mat,n,m,dp) + mat[i][j1] + mat[i][j2]
            maxi = max(maxi,a)
            dp[i][j1][j2] = maxi
    return dp[i][j1][j2]

dp = [[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]]
print(cherrypicup_memoization(0,0,m,arr,n,m,dp))
print(dp)

def cherrypickup_tabulization(mat,n,m,dp):
    for j1 in range(len(mat[0])):
        for j2 in range(len(mat[0])):
            if j1 == j2: dp[n][j1][j2] = mat[n][j1]
            else:
                dp[n][j1][j2] = mat[n][j1] + mat[n][j2]

    for i in reversed(range(0,n-2)):
        for j1 in range(m):
            for j2 in range(n):
                maxi = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if j1+k >= 0 or j1+k < m+1 or j2+l >= 0 or j2+l < m+1:
                            a = -1000000
                        else:
                            if j1 == j2:
                                a = dp[i + 1][j1 + k][j2 + l] + mat[i][j1]
                            else:
                                a = dp[i + 1][j1 + k][j2 + l] + mat[i][j1] + mat[i][j2]
                        maxi = max(maxi, a)
                        dp[i][j1][j2] = maxi
    return dp[0][0][m-1]

dp1 = [[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]]
print(cherrypickup_tabulization(arr,n,m,dp1))