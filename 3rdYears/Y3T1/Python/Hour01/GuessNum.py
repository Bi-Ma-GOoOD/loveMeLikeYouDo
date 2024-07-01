import random

i = 0
#Random number
rand_int = random.randint(0, 100)
#Flag to stop while-loop
check = True
#Guess number from input
while i < 10 and check != False:
    print("Round", i+1)
    guess_num = int(input("Enter number to guess : "))
    if guess_num < rand_int : 
        print("\tTry higher number.")
    elif guess_num > rand_int : 
        print("\tTry lower number.")
    else : 
        print("\tFinally!! You got it.")
        check = False
    i+=1
#print random number
print("Random number is:", rand_int)
