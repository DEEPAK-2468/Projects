import random
name=input("Enter your name: ")
print("Welcome to the Word Guessing Game,", name + "!")
print("Good luck!")
words=['orange', 'banana', 'grape', 'kiwi', 'mango', 'peach', 'pear', 'plum', 'cherry', 'melon']
random_word=random.choice(words)
print("The word has", len(random_word), "letters.")
print("Guess the word within 12 attempts.")
for i in random_word:
    print("__", end="  ")
guess_word=""
for i in range(12):
    guess=input("\nEnter your guess: ")
    if guess in random_word:
        guess_word+=guess
    for ch in random_word:
        if ch in guess_word:
            print(ch,end='  ')
        else:
            print("__",end="  ")
    if len(list(set(guess_word)))==len(list(set(random_word))):
        print("\nCongratulations,", name + "! You guessed the word", random_word, "correctly!")
        break
else:
    print("\nSorry,", name + ". You've used all your attempts. The correct word was", random_word + ".")
        