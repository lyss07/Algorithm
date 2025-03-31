N,M=map(int,input().split())

nums=list(map(int,input().split()))
sumList=[0]*N
sumList[0]=nums[0]
remainder=dict()

cnt=0

for i in range(1,N):
    sumList[i]=sumList[i-1]+nums[i]

for i in range(N):
    if sumList[i]%M==0:
        cnt+=1
    
    remainder[sumList[i]%M]=remainder.get(sumList[i]%M,0)+1

for num in remainder.values():
    if num>1:
        cnt+=num*(num-1)//2

print(cnt)