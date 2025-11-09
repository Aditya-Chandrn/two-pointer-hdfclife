n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
for i in range(n):
    res.append(arr1[i] + arr2[-(i + 1)])
print(*res)