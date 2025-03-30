from collections import deque

N,L=map(int,input().split())

A=list(map(int,input().split()))

dq=deque()
result=[]

for i in range(N):
    while dq and dq[-1]>A[i]:
        dq.pop()
    dq.append(A[i])
    if i>=L and dq[0]==A[i-L]:
        dq.popleft()
    print(dq[0],end=' ')