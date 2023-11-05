#state = ""
for num in range(1,21):
    #print(num)
    if num == 4 or num == 13:
        state = "unlucky"
   # print("x is unlucky")
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")    
        
            