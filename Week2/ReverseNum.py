'''
Write a program if input if 89, output should be 98 (swap the digits)
'''
def reverse_the_number(number):
    '''
    rev=0
    rem=number%10
    rev=(rev*10)+rem
    number=number/10
    rev=(rev*10)+number
    return rev
    '''
    total=0
    while number!=0:
        rem=number%10
        total=(total*10)+rem
        number = number / 10
    return total
    
num = int(input("Enter any Number: "))   # Taking Input from
print(f"Reversed number :{reverse_the_number(num)}")