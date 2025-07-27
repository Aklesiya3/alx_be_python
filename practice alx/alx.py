#import random
#secret_number =random.randint(1,10)
#guess = int(input("guess the number : "))
#match guess:
    #case _ if guess==secret_number:
     #   print("yes you guessed right")
    #case _ if guess> secret_number:
    #    print("oops your guess is bit high")
    #case _ if guess<secret_number:
     #   print("oops your guess is bit low")
#play_again= input("do you want to play again?(yes/no):").lower()
#if play_again != "yes":
 #   print("thanks")

numbers=[1,5,3,9]
total=0
for number in numbers:
    total =total + number
print(total)

