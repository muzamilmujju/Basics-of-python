def fact(n):
    fac=1
    for i in range(1,n+1):
        fac *=i
    return fac

print(fact(5))
print(fact(4))