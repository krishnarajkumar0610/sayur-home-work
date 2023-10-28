def rev(sen,n):
    if len(sen)==1:
        return sen[0]
    else:
         return sen[n]+" "+rev(sen[0:n],n-1)
         
         
        
sen = input("Enter the senetence : ")
sen =  sen.split(" ")

print(rev(sen,len(sen)-1))
