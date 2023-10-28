def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  

n=int(input("Enter the nth number to get fibonacci series : "))
if n<0:
    print("Enter number which is >=0")
else:
    print(f"Fibonacci numbers for {n} :",end=' ')  
    for i in range(n+1):  
        print(fibo(i),end=' ')


# 1st number is 0, 2nd number is 1, 3rd is add previ number-1 and previ number-2    