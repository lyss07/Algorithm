n=int(input())

nums=list(int(input()) for _ in range(n))

k=1
m=0
stack=[]
result=[]

for i in range(1,n+1):
    if nums[i-1]>=k:
        while nums[i-1]>=k:
            stack.append(k) #뺄 숫자가 나올때까지 숫자 넣기
            k+=1
            result.append("+")
        stack.pop() #숫자 빼기
        result.append("-")
    else: #nums[i-1]<k
        if not stack or stack[-1]>nums[i-1]:  # 스택이 비었거나 pop할 값이 num보다 크면 불가능
            print("NO")
            m=1
            break
        stack.pop()
        result.append("-")

if m==0:
    for a in result:
        print(a)