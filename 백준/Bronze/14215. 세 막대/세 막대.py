a,b,c=map(int,input().split())

sticks=[a,b,c]
maxLen=max(sticks)

sticks.remove(maxLen)

while(maxLen>=sum(sticks)):
    maxLen-=1

print(sum(sticks)+maxLen)