print("welcome to the snake water gun game")
print('''Now chose which you want
1. S for Snake
2. W for Water
3. G for Gun ''')
user = input("")
import random
list = ["Snake" , "Water" , "Gun"]
computer = random.choice(list)
if user=="Snake":
  if computer=="Water":
    print("Snake vs Water" + "\nYou Won")
  elif computer=="Gun":  
    print("Snake vs Gun" + "\nYou lost")
  elif computer=="Snake":
    print("Snake vs Snake" + " Draw")  
elif user=="Water":
  if computer=="Snake":
    print("Water vs Snake" + "\nYou lost")
  elif computer=="Water":
    print("Water vs Water" + " Draw")
  elif computer=="Gun":
    print("Water vs Gun" + "\nYou Won")
elif user=="Gun":
  if computer=="Snake":
    print("Gun vs Snake" + "\nYou Won")
  elif computer=="Water":
    print("Gun vs Water" + "\nYou Won")
  elif computer=="Gun":
    print("Gun vs Gun" + " Draw")  
    
