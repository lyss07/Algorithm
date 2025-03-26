import math

A,B,V=map(int,input().split())

cnt=math.ceil((V-B)/(A-B))

print(cnt)