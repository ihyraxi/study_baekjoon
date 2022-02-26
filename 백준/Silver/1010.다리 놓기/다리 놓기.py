def f(a):#factorial
    if(a>1):
        return a * f(a-1)
    else:
        return 1
def bridge(n, m):#nCr
    return f(n) / (f(m) * f(n-m))
T = int(input())
results = []
for _ in range(T):
    N, M = map(int, input().split())
    results.append(int(bridge(M, N)))
for result in results:
    print(result)
