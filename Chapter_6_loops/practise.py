# Program 1: Multiplication Table
a = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(a, "*", i, "=", a * i)


# Program 2: Sum of numbers from 1 to n
b = int(input("Enter a number to find sum from 1 to n: "))
total = 0
for i in range(1, b + 1):
    total += i
print("Sum is:", total)


# Program 3: Guess the secret number
secret_number = 7

while True:
    guess = int(input("Enter your guessed number: "))
    if guess == secret_number:
        print("You guessed right.")
        break
    else:
        print("Wrong guess, guess again.")
