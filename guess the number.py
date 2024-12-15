# TASK: number guess game
# 1. Lower bound = 1, upper bound = 100
# 2. Generate an integer between lower and upper bounds - N
# # 3. In a while loop:
## 3. Ask user for a guess between lower and upper bounds - G
## 4. Check if G is lower or upper from N
## 5. If U:
### 6. Print "Too high"
## 7. If L:
### 8. Print "Too low"
## 9. If C:
### 10. Congratulate the user and show the number of guesses user have made

# import random

# print("Guess the number!")

# invent_number=random.randrange(
#     start=1,
#     stop=100
# )
    

# print (invent_number)

import random

print("Guess the number!")

# Generate a random number between 1 and 100
invent_number = random.randrange(1, 100)

# Uncomment this line to debug or test by revealing the number
# print(f"The number to guess is: {invent_number}")

# Initialize attempt counter
attempts = 0

while True:
    try:
        # Get the user's guess
        user_guess = int(input("Enter your guess (1-100): "))
        attempts += 1  # Increment the attempt counter

        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.")
        elif user_guess < invent_number:
            print("Too low! Try again.")
        elif user_guess > invent_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number: {invent_number}")
            print(f"It took you {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a number.")
