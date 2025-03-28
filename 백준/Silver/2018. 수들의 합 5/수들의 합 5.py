N=int(input())
n=1
cnt=0
start,end=1,1

while end<=N:
    if n==N:
        cnt+=1
        end+=1
        n+=end
    elif n<N:
        end+=1
        n+=end
    else:
        n-=start
        start+=1 #n>N
        
print(cnt)