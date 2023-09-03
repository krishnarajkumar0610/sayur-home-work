############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like
#init variables

movies = input("What movies you like ? ") # asking movie names from frie
friend1_movie_list=movies.split(',')        # stores as list because we using split method
commonMoviewCount = 0
common_movie_list=[]
print(friend1_movie_list)

while (True) :   # alwasys running when we need to stop we use break
    #ask the second friend for one movie at a time
    movie = input ("Enter the movie name Friend 2 :")    # asking the movie name to friend again and again
    
    for film in(friend1_movie_list):     # this loop is for checking the movie name in friend 1 movie list
        if film in movie:
            #if present, 
            print(f"You both like {movie}")  # printing the movie name both friend1 and friend2 liked
            commonMoviewCount+=1    # counting movie count by +1
            common_movie_list.append(movie)
            break   # breaking the for loop 

    if(commonMoviewCount >= 3):# when common movie count is greaterthan equal to 3 then breaking the while loop to stop asking movie name
        break
    else:
        print ("Try again") # this is when common movie count is lessthan 3
        
print(f"The common movies are : {common_movie_list}")  # printing the common movie name list both friend1 and friend2 has both liked