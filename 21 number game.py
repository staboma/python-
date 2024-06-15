def player_turn(player, current_total):
    while True:
        try:
            choice = int(input(f"Player {player}, choose a number (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                return current_total + choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def game():
    current_total = 0
    player = 1

    while current_total < 21:
        current_total = player_turn(player, current_total)
        print(f"Current total is: {current_total}")

        if current_total >= 21:
            print(f"Player {player} loses!")
            break

        player = 1 if player == 2 else 2

if __name__ == "__main__":
    game()
