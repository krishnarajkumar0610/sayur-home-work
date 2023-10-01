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
print(f"Number is reached 1 after these number of iterations :{calculate(n)}")