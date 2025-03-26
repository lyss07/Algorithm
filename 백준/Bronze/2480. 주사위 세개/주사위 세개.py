dice=list(map(int,input().split()))
check=0
cnt=0

if dice[0]==dice[1]:
    cnt+=1
    m=2

if dice[1]==dice[2]:
    cnt+=1
    m=0

if dice[0]==dice[2]:
    cnt+=1
    m=1

if cnt==0:
    maxDice=max(dice)
    print(maxDice*100)
elif cnt==1:
    dice.pop(m)
    print(1000+dice[0]*100)
elif cnt==3:
    print(10000+dice[0]*1000)