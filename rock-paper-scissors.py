import random

def get_choice():
   player_choice = input("Enter a choice (rock, paper or scissors): " )
   options = ["rock", "paper", "scissors"]
   computer_choice = random.choice(options)
   choices = {"player" : player_choice, "computer" : computer_choice}
   return choices

def check_results(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
      return print("It's a tie, maybe.....MOCHI CALL THE LYCHEE")
    elif player == "rock" and computer == "scissors":
       return "Rock smashes scissors. Oh no, our table, its broken!"
    elif player == "paper" and computer == "rock":
       return "Paper suffacates rock. YOU KILLED MOCHI, HOW DARE YOU."
    elif player == "scissors" and computer == "paper":
       return "Scissors cut paper. NOOOOOOOOOOO!!! MOCHI!! wait what, that was Lychee(bruh^10000)."
    else:
      return "YOU DIED TO THE CATS OF RPS"       

choices = get_choice()
results = check_results(choices["player"], choices["computer"])
print(results)