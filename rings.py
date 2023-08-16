#T = [[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[4,5,6,7,8,9],[5,6,7,8,9,0]]
T = [[0,1,2,3,4],[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
#T = [[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6]]
#T = [[1,21,13,4],[8,81,4,92],[-4,42,0,0],[4,-1,-53,8]]

n = len(T)
for i in range(n):
    print(T[i])

B=[]
for i in range(0,(n+1)//2):
    B.append(0)

for i in range(0,n):
    for y in range(0,n):
        if (i<n//2 and y<n//2):   
            B[i if i<y else y] += T[i][y]

        if (i<n//2 and y>=n//2):
            B[i if i<n-1-y else n-1-y] += T[i][y]

        if (i>=n//2 and y<n//2):
            B[n-1-i if n-1-i<y else y] += T[i][y]
        
        if (i>=n//2 and y>=n//2):
            B[n-1-i if n-1-i<n-1-y else n-1-y] += T[i][y]

print()
print(B)