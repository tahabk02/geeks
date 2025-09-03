import random

class Game:
    def get_user_item(self):
        """Ask the user to select rock/paper/scissors with validation."""
        while True:
            user_input = input("Select (rock/paper/scissors): ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                return user_input
            print("Invalid choice, try again.")

    def get_computer_item(self):
        """Randomly select rock/paper/scissors for the computer."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Determine the game result (win/draw/loss)."""
        if user_item == computer_item:
            return "draw"

       
        if (
            (user_item == "rock" and computer_item == "scissors")
            or (user_item == "scissors" and computer_item == "paper")
            or (user_item == "paper" and computer_item == "rock")
        ):
            return "win"

        return "loss"

    def play(self):
        """Play one round and return result."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

       
        if result == "win":
            print(f"You selected {user_item}. The computer selected {computer_item}.  You win!")
        elif result == "loss":
            print(f"You selected {user_item}. The computer selected {computer_item}.  You lose!")
        else:
            print(f"You selected {user_item}. The computer selected {computer_item}.  It's a draw!")

        return result
