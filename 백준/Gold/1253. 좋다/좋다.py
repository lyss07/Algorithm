N=int(input())

nums=list(map(int,input().split()))

nums.sort()

cnt=0

for k in range(N):
    i=0
    j=N-1
    while i<j:
        num=nums[i]+nums[j]
        if num==nums[k]:
            if i!=k and j!=k:
                cnt+=1
                break
            elif i==k:
                i+=1
            elif j==k:
                j-=1
        elif num<nums[k]:
            i+=1
        else:
            j-=1

print(cnt)