n = int(input("enter the value of n:- "))

def facto(n):
    i=n
    fact=1
    while i>1:
        fact *=i
        i -=1
    return fact
print(facto(n))
      
