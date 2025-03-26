num=int(input())
cnt=0
ground=[[0]*100 for _ in range(100)]

for _ in range(num):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            if ground[99-b-j][a+i]==0:
                cnt+=1
                ground[99-b-j][a+i]=1
            else:
                continue

print(cnt)