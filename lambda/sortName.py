# Write a Python program to sort a list of tuples using Lambda.
# [("apple", 50),("orange", 15) ,("mango", 30)]
# lambda functios - sort by name, sort by cost

fruits =[ 
          ("apple",50),
          ("orangte",15),
          ("mango",30)
        ]

# created a list and inside the list we created tuples

sorted_names = sorted(fruits, key = lambda x:x[0])   # sorting the names by alphabetical order alone

sorted_price = sorted(fruits, key = lambda x:x[1])  # sorting the price by integer order alone

print(f"sorted_names : {sorted_names}")  #printint the names and price in alphabetical order
 
print(f"sorted prices : {sorted_price}")    #printint the names and prince in integer order