def tim_so_fibonacci(n):
    if n <= 2:
        return 1
    f1,f2= 1,1
    for i in range (3,n+1):
        f1,f2=f2,f1+f2
    return f2