import random
randnum=random.randint(1,10)

while True:
    guessno=int(input("enter a Number: "))
    if(guessno==randnum):
        print("You Won!!!")
        break
            
    elif(guessno>randnum):
        print("Too high!!")
    else :
        print("Too Low!!")
print("------Gameover--------")