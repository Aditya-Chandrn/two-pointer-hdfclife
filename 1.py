n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(n // 2):
    res.append(arr[i] + arr[-(i + 1)])
print(*res)
