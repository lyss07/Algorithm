N,M=map(int,input().split())

A=[list(map(int,input().split())) for _ in range(N)]
S=[[0]*(N+1) for _ in range(N+1)]
result=[]

for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j]=S[i][j-1]+S[i-1][j]+A[i-1][j-1]-S[i-1][j-1]

for i in range(M):
    X1,Y1,X2,Y2=map(int,input().split())
    result.append(S[X2][Y2]-S[X1-1][Y2]-S[X2][Y1-1]+S[X1-1][Y1-1])

for num in result:
    print(num)