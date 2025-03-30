S,P=map(int,input().split())
line=input()
cA,cC,cG,cT=map(int,input().split())
A,C,G,T=0,0,0,0
m=0
cnt=0

idx=0

for i in range(P):
    if line[i]=='A':
        A+=1
    elif line[i] == 'C':
        C += 1
    elif line[i] == 'G':
        G += 1
    elif line[i] == 'T':
        T += 1

if A>=cA and C>=cC and G>=cG and T>=cT:
    cnt+=1

for i in range(P,S):
    if line[i-P]=='A':
        A-=1
    elif line[i-P]=='C':
        C -= 1
    elif line[i-P]=='G':
        G -= 1
    elif line[i-P]=='T':
        T -= 1

    if line[i]=='A':
        A+=1
    elif line[i]=='C':
        C+=1
    elif line[i]=='G':
        G+=1
    elif line[i]=='T':
        T+=1

    if A>=cA and C>=cC and G>=cG and T>=cT:
        cnt+=1
        
print(cnt)