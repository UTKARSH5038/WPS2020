## DOUBT IN THIS QUESTION 

while(True):           
    q=input()
    if "//" in q:
        x=q.split("//")
        if ">" in x[0]:
            x[0]=x[0].replace(">",".")
            x[0]=x[0].replace("-","")
    print(x[0]+"//"+x[1])
    if "//" not in q:
        print(q)        