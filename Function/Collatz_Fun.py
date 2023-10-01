def calculate(n):
    count=0
    while n!=1:
        if n%2==0:
            n = n//2        
        else:
            n = (3*n)+1
        count+=1   
    return count

n = int(input("Enter a Number : ")) # asking input 
count_num1=calculate(n)

n = int(input("Enter a Number : ")) # asking input 
count_num2=calculate(n)

if count_num1<count_num2:
    print(f"Count number1 is less count")
else:
    print(f"Count number2 is less count")