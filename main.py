import random

random_number = random.randint(1, 100);
attempts = 0;

print("Welcome to the Number Guessing Game");
print("I have selected a number between 1 and 100.");

while True:  
    
    user_guess = input("Guess the number from 1 to 100: ");
    
    
    if not user_guess.isdigit():
        print("Invalid input! Please enter a number.");
        continue
    
    user_guess = int(user_guess);
    
    
    if user_guess < 1 or user_guess > 100:
        print("Invalid number! Please guess a number between 1 and 100.");
        continue
    
    attempts += 1
    
    if user_guess < random_number:
        print("Too low, try again.");
    elif user_guess > random_number:
        print("Too high! Try again.");
    else: 
        print(f"Correct! You've guessed the number in {attempts} attempts.");
        break

