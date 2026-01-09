def fak(n:int)->int:
    result=1
    if n!=0:
        for x in range(1,n+1):
            result *= x
    return result
print(fak(3))

def fak2(n:int)->int:  #rekurzivna
    if n==1:
        return 1
    else:
        return n*fak2(n-1)

def fib(n:int)->int:
    if n== 1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(3))