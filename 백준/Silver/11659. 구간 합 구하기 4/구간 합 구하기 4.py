N,M=map(int,input().split())

nums=list(map(int,input().split()))
sumList=[0]*(N+1)

for i in range(1,N+1):
    sumList[i]=sumList[i-1]+nums[i-1]

result=[]

for k in range(M):
    i,j=map(int,input().split())
    result.append(sumList[j]-sumList[i-1])

for num in result:
    print(num)