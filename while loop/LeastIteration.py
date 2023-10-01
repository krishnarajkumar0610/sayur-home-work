size = int(input("Enter the size of your lsit :"))
numbers=[]
number_counts=[]
print("Enter the elements : ")

for i in range(size):
    numbers.append(int(input()))
    
for number in numbers:
    count=0
    while number !=1 :
        if number %2 == 0:
            number=(number//2)
        else:
            number=(3*number)+1
        count+=1
    number_counts.append(count)


print(f"Minimum count : {min(number_counts)}")
print(f"Numbers count : {number_counts}")




# def check(numbers,value):
#     if value in numbers:
#         return True
#     return False

# for i in range(size):
#     value=int(input())
#     if not check(unique_numbers,value):
#         numbers.append(value)
#         unique_numbers.append(value)   
#     else:
#         print("Enter other number it is already in the list : ")
#         value=int(input())
#         numbers.append(value)
# for index in range(0,len(numbers)):
#     count=1
#     value = numbers[index]
#     while value!=1:
#         if value%2==0:
#             value = value//2        
#         else:
#             value = (3*value)+1
#         count+=1
#     frequency_numbers.append(count)    
    
# print(f"Minimum count in the index is : {min(frequency_numbers)}")