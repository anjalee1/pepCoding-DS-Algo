
n=int(input())
arr=[]
for i in range(n):
    string=input().split()
    b=[]
    for x in string:
        b.append(int(x))
    arr.append(b)
dp=[]
for i in range(n):
    a=[]
    for j in range(3):
        a.append(0)
    dp.append(a)
dp[0][0]=arr[0][0]
dp[0][1]=arr[0][1]
dp[0][2]=arr[0][2]
for i in range(1,n):
     dp[i][0]=arr[i][0]+min(dp[i-1][1],dp[i-1][2])
     dp[i][1]=arr[i][1]+min(dp[i-1][0],dp[i-1][2])
     dp[i][2]=arr[i][2]+min(dp[i-1][0],dp[i-1][1])
print(min(dp[n-1][0],min(dp[n-1][1],dp[n-1][2])))
