from game import Game

def get_user_menu_choice():
    """Show menu and return user choice (no loop here)."""
    print("\n=== Rock Paper Scissors Menu ===")
    print("1. Play a new game")
    print("2. Show scores")
    print("x. Exit")
    choice = input("Choose an option: ").lower()

    if choice in ["1", "2", "x"]:
        return choice
    else:
        print(" Invalid choice. Try again.")
        return None

def print_results(results):
    """Display final results nicely."""
    print("\n=== Game Summary ===")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing! Goodbye.")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice is None:
            continue

        if choice == "1": 
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":  # show scores
            print_results(results)

        elif choice == "x":  # exit
            print_results(results)
            break

if __name__ == "__main__":
    main()
