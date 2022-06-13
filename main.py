import random

# Check what the user's selection corresponds to
def check_selection(letter):
    if letter == "R":
        return "Rock"
    elif letter == "P":
        return "Paper"
    elif letter == "S":
        return "Scissors"
    else:
        return "Try Again"

# rock beats scissors
# paper beats rock
# scissors beats paper
# If game is extended (for example, rock paper scissors lizard rock),
# and each choice beats more than one choice, 
# replace the values with a list of all possible values
# e.g. "rock": ["scissors", "lizards"]
choice_beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    # collect user input
    user_input = input("Rock Paper Scissors, let's go!!!! Make your choice, R for rock, P for Paper, S for scissors ")

    # list of possible choices
    possible_choices = ["R", "P", "S"]
    # computer's choice
    computer_choice = random.choice(possible_choices)

    # Get what the choices correspond to
    user_selection = check_selection(user_input.upper()).lower()
    computer_selection = check_selection(computer_choice.upper()).lower()

    # Run only if user's choice is valid, else, prompt user for new choice
    if user_selection != "Try Again":

        # if players tie, run the game again
        if user_selection == computer_selection:
            print(f"Both players selected {user_selection}, It's a tie!")
        else:
            print(f"Player ({user_selection}) : CPU({computer_selection})")
            
            # if computer's choice matches what user's choice can beat, user wins
            if computer_selection in choice_beats[user_selection]:
                print(f"{user_selection} beats {computer_selection}! Player wins!!!")
            else:
                print(f"{computer_selection} beats {user_selection}! Computer wins!!!")
            break
    
            


