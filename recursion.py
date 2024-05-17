#Recursion : function calls itself.

def recu(n):
    if(n==10): #condition to stop recursion 
        return
    print(n)
    recu(n+1) #called it selfhere

recu(1)