def sum(values):
    if len(values)==1:
        return values[0]
    else:
         return values[0]+sum(values[1:])
         
         
        
numbers=[]
size = int(input("Enter the list size : "))

for index in range(size):
    val=int(input(f"Enter the {index+1} element : "))
    numbers.append(val)
print(sum(numbers))
