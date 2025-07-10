# 1 for snake
# -1 for water 
# 0 for gun
import random #import random module to generate random numbers 

computer = random.choice([-1, 0, 1])
print(computer)

# computer = -1
youstr = input("enter ur choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake",-1: "water",0: "gun"}
you = youDict[youstr] #store the values thats entered in you string

#now we hve only two numbers(variable) you and computer

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}") #it hav the capability ti reverse the dictionary

if(computer == you):
    print("ITS A DRAW")
    
else:
    if(computer == 1 and you == -1):
        print("you lose")
        
    elif(computer == 1 and you == 0):
        print("you win")
        
    elif(computer == -1 and you == 0):
        print("you lose")
        
    elif(computer == 0 and you == 1):
        print("you lose")
        
    elif(computer == -1 and you == 1):
        print("you win")
        
    elif(computer == 0 and you == -1):
        print("you win")
    

    else:
        print("smthn is wrong")

