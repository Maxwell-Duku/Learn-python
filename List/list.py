####################LISTS USING FOR LOOPS#################

colours = ["red", "blue", "green", "yellow", "puple"]
for colour in colours:
    print(colour)
    

numbers = [2,4,6,8,10]
for num in numbers:
    print(num * num)
    
    
    
    
    #############LISTS USING WHILE LOOP############
colours = ["purple", "white", "pink", "black"]
index = 0
while index < len(colours):
    print(f"{index}: {colours[index]}")
    index += 1
    
    
###################USING APPEND METHOD#######################
items = ["tomato", "egg", "onion", "salt"]
items.append("pepper")
print(items)

#####################USING THE EXTEND METHOD#####################
num = [1, 2, 3, 4, 5]
#print(num)
num.extend((6, 7, 8, 9, 10))
print(num)

##################USING THE INSERT METHOD####################
first_list = [1, 2, 3]
print(first_list)
first_list.insert(2, 'hi!')
print(first_list)
first_list.insert(-1, 'the end!')
print(first_list)


#######################USING THE CLEAR METHOD####################
shoppings = ["pizza", "biscuit", "bread", "ice cream"]
shoppings.clear()
print(shoppings)


