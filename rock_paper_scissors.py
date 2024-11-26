import random  # Import the random module

print("Welcome to Rock, Paper, and Scissors!")

choices = ["rock", "paper", "scissors"]  # List of possible choices

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # User's choice
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue  # Skip to the next iteration of the loop

    # Computer's choice
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1  # Increment user score
    else:
        print("You lose!")
        computer_score += 1  # Increment computer score

    # Display the current score
    print(f"Score: You {user_score} - {computer_score} Computer")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        print(f"Final Score: You {user_score} - {computer_score} Computer")
        break
