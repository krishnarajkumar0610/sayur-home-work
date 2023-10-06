def printLetters(aString):
    first_a=aString.find('a')
    last_a=0
    if first_a>=0:
        last_a=aString.rfind('a')
        if last_a != last_a:
            print(aString[first_a+1:last_a])
        else:
            print("There is only onr 'a' ")
    else:
        print("There is no 'a' ")
        


sentence = input("Enter the sentence : ")
sentence=sentence.lower()
printLetters(sentence)