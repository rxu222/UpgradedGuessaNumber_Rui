import random
from library import updateTopPlayers

# Build the function to start the game
def startGame():
    topPlayerFile = "topPlayers.txt"
    # Start an infinite loop for playing multiple games
    while True:
        # Ask the player for their name prior to playing the game
        playerName = input("Please input your name: ")

        # Initialize variables for tracking guesses and game state
        attempts = 0  # Counter for the number of attempts
        isGuessCorrect = False  # Flag to track if the guess is correct

        print(f"Hi {playerName}, welcome to the Number Guessing Game!")

        # Inner loop for a single game
        secretNumber = random.randint(1, 100)  # Set the secret number as a random integer between 1 and 100
        while isGuessCorrect is False:  # Inner loop for a single game
            try:
                userInput = input("Guess a number between 1 and 100 (or enter 'quit' to exit): ")
                if userInput == "quit":
                    print("Thank you for playing")
                    break  # Exit the function if the player chooses to quit

                # Skip the rest of the loop and ask for input again
                # if the player input a number out of range
                guess = int(userInput)
                if guess < 1 or guess > 100:
                    print("Please enter a number within the range of 1 to 100.")
                    continue

                attempts += 1  # Increment the attempt counter

                # Compare the guess and the secret number
                if guess < secretNumber:
                    print("Too low! Try again.")
                elif guess > secretNumber:
                    print("Too high! Try again.")
                else:
                    print(f"Good job! You guessed the number {secretNumber} correctly in {attempts} attempts.")

                    # Set flag to True when correct guess is made
                    isGuessCorrect = True

            # Catch invalid input
            except ValueError:
                print("Please enter a valid number.")

        # Make sure the result will not be ranked when the attempt = 0
        if attempts > 0:
            updateTopPlayers(playerName, attempts, topPlayerFile)
            print("Top players updated.")

        # Ask if the player wants to play the game again
        playAgain = input("Do you want to play again? (yes/no): ")
        if playAgain != "yes":
            print("Thank you for playing!")
            return  # Exit the function if the player doesn't choose the "yes"


# Call the function
startGame()
