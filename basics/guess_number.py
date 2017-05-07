# guess a number with 10 tries
import random
start = 1
end = 100
num_of_tries = 10
secret = random.randint(start, end)

print(secret)

for tries in range(1, num_of_tries + 1):
    print("Guess a number between " + str(start) + " and " + str(end))
    number = input()

    try:
        number = int(number)
        if number < secret:
            print("Too low")
        elif number > secret:
            print("Too high")
        else:
            secret = None
            break
    except ValueError:
        print("Invalid input")

if secret == None:
    print("You win the game!")
else:
    print("Better luck next time :p")
