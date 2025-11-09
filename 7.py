t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    weights = list(map(int, input().split()))
    
    weights.sort()
    i, j = 0, n - 1
    boats = 0

    while i <= j:
        if weights[i] + weights[j] <= k:
            i += 1  
        j -= 1      
        boats += 1  
    
    print(boats)
