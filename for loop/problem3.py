######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

rows,columns=8,8
for row in range(1,rows+1):
    for colm in range(1,columns+1):
        if (row+colm) % 2 == 0:
            print("\u25A0",end=' ')
        else:
            print("B",end=' ')
    print()