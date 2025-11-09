t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    arr.sort()
    left, right = 0, n - 1
    max_sum = -1

    while left < right:
        s = arr[left] + arr[right]
        if s < k:
            max_sum = max(max_sum, s)
            left += 1
        else:
            right -= 1

    print(max_sum)
