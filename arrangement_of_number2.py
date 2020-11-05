n=int(input())
arr=list(map(int,input().split()))
s=""
S=""
for i in range(n):
    if arr[i]>0:
        s=s+" "+str(arr[i])
    else:
        S=S+" "+str(arr[i])

print(s+S)
