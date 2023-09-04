lines = int(input("Enter number of lines :"))
number=1
while(number<=lines):
    if input("Enter space to print $ :") == " ":
        print(' '*(lines-number),end='')
        print(f"{'$ '*number}")
        number+=1
    else:
        break