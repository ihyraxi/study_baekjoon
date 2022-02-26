'''
 메모리: 30860 KB, 시간: 304 ms
 2022.02.26
 by Alub
'''
n, k = map(int, input().split())
c = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    c.append(int(input()))
for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])
