print("*********************************")
print("Welcome to the Guess Game!")
print("*********************************")

secret_number: int = 42

guess_str = input("Type your number: ")

print("You Type: ", guess_str)

guess = int(guess_str)

if(secret_number == guess):
    print("You Won")
else:
    print("You lose")

print("END OF GAME")
