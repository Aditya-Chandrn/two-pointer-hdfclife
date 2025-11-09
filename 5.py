t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    seen = set()
    found = False
    for num in arr:
        if (k - num) in seen:
            found = True
            break
        seen.add(num)
    print(1 if found else -1)
