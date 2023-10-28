def rev(sen,n):
    if len(sen)==1:     # when list has only one word then return it
        return sen[0]
    else:
         return sen[n]+" "+rev(sen[0:n],n-1)    # adding the last word from the list and adding with return value when the function called
         
sen = input("Enter the senetence : ")   # asking the inpur
print(f"Before Revered : {sen}")

sen =  sen.split(" ")   # spliting it into list
print(f"Revered String : {rev(sen,len(sen)-1)}")  # calling the function
