s=0
nos,noq=map(int,input().split())
clist=list(input())
slist=list(input())
mlist=list(input().split())
for i in range(len(clist)):
    if clist[i]==slist[i]:
        s=s+int(mlist[i])
print(nos*s)