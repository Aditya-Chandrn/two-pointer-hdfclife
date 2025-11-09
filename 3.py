t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    i, j = 0, n - 1
    f = 0
    while i < j:
        s = arr[i] + arr[j]
        if s == k:
            f = 1
            break
        elif s < k:
            i += 1
        else:
            j -= 1
    print("Yes" if f else "No")
