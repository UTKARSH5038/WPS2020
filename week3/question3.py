flag=0
q=int(input())
for _ in range (q):
    flag=0    
    list1=input()
    list2=input()
    c=ord((list2[0]))-ord((list1[0]))
    for i in range(1,len(list1)):
        w=(ord(list2[i])-ord(list1[i]))
        if w<0:
            w=26-abs(w)
        if w!=c and w!=26-abs(c):
            flag=1
    if flag==1:
        print('-1')
    else:
        if c>=0:
            print(c)
        else :
            print(26-abs(c)) 
                  