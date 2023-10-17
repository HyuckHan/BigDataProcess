def fib(n, memo):
    if memo[n] != 0 :
        return memo[n];
    if n < 3 :
        return 1
    else :
        memo[n] =  fib(n-1,memo)+fib(n-2,memo)
        return memo[n];


m = [0 for n in range(0,6)]
print(fib(5,m))

m = [0 for n in range(0,11)]
print(fib (10,m))

m = [0 for n in range(0,36)]
print(fib(35,m))
