while(True): 
    try:
        q=input()
    except:
        break    
    if "//" in q:
        x=q.split("//",1)
        if "->" in x[0]:
            x[0]=x[0].replace("->",".")
            print(x[0]+"//"+x[1])
        else:
            print(q)        
    if "//" not in q:
        if "->" in q:
            q=q.replace("->",".")
            print(q)
        else:
            print(q)    
                    
