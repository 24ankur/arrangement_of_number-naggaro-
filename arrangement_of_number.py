n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if arr[i]>0:
        arr[c]=arr[i]
        c=c+1

for i in range(c,n):
    arr[i]=0


print(*arr)