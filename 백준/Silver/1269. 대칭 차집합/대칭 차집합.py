numA,numB=map(int,input().split())

A=set(input().split())
B=set(input().split())

result=(A-B)|(B-A)

print(len(result))