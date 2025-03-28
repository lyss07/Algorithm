num=int(input())
armor=int(input())
ing=list(map(int,input().split()))

ing.sort()

cnt=0
start,end=0,num-1
sumNum=ing[start]+ing[end]

while start<end:
    if sumNum==armor:
        cnt+=1
        start+=1
        sumNum=ing[start]+ing[end]
    elif sumNum>armor:
        end-=1
        sumNum=ing[start]+ing[end]
    else:
        start+=1
        sumNum=ing[start]+ing[end]

print(cnt)
