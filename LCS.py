def LCS(x,y):
    m = len(x)
    n = len(y)
    A = [[0 for j in range(n)] for i in range(m)]
    B = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if x[i]==y[j]:
                A[i][j] = A[i-1][j-1] + 1
                B[i][j] = 1
            elif A[i-1][j]>=A[i][j-1]:
                A[i,j] = A[i-1][j]
                B[i,j] = 2
            elif A[i][j] == A[i][j-1]:
                B[i,j] = 3
    return (A,B)
if __name__=="__main__":
    x = "hahaha"
    y = "jajaha"
    print LCS