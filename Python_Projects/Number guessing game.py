import random
low_bound=int(input("Enter the lower bound of the range: "))
up_bound=int(input("Enter the upper bound of the range: "))
print("\tYou have only 7 attempts to guess the number!")
random_number=random.randint(low_bound,up_bound)
for i in range(7):
    user_guess=int(input("Enter your guess: "))
    if user_guess<random_number:
        print("Your guess is too low!")
    elif user_guess>random_number:
        print("Your guess is too high!")
    else:
        print("Congratulations! You guessed the number correctly in ",i+1," attempts.")
        break
else:
    print("Sorry, you've used all your attempts. The correct number was ", random_number)