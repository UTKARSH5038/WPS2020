str1=input()
str2=input()
flag=0
if len(str1)==len(str2):
    for i in range(len(str1)):
        if str1[i]>str2[i]:
            print("NO")
            flag=1
            break
    if flag==0:
        print("YES")
else:
    print("NO")            
            