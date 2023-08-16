n = int(input("n: "))
k = int(input("k: "))
counter = 1
A = [_ for _ in range(n)]
B = [_ for _ in range(k)]

print(A,"\n")
print(B)
while (B[0] != n - k):
    B[-1] += 1
    counter += 1
    for i in range(k-1,-1,-1):
        if (B[i] > n-k+i):
            B[i-1] += 1
            for j in range(i,k):
                B[j] = B[j-1]+1
    for _ in range(B[0]):
        print("\t",end="")
    print(B)

print(counter)