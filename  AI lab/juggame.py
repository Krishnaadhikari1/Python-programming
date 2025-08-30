def print_jars(jars):
    print("\nCurrent Jars:")
    for i, count in enumerate(jars, start=1):
        print(f"Jar {i}: {'●' * count} ({count})")
    print()

def get_move(player, jars):
    while True:
        try:
            jar = int(input(f"Player {player}, choose a jar (1-3): "))
            if jar not in [1, 2, 3]:
                print("Invalid jar number. Choose 1, 2, or 3.")
                continue
            if jars[jar - 1] == 0:
                print("That jar is empty. Choose another.")
                continue
            count = int(input(f"Player {player}, how many to remove from Jar {jar}? "))
            if not (1 <= count <= jars[jar - 1]):
                print(f"Choose between 1 and {jars[jar - 1]}.")
                continue
            return jar - 1, count
        except ValueError:
            print("Please enter valid integers.")

def is_game_over(jars):
    return sum(jars) == 1

def three_jar_game():
    jars = [3, 5, 7]
    current_player = 1

    print("Welcome to the 3 Jar Game!")
    print("Rules:\n1. Take turns removing 1 or more items from one jar.")
    print("2. The player forced to take the LAST item loses.\n")

    while True:
        print_jars(jars)

        if is_game_over(jars):
            print("Only one item remains!")
            print_jars(jars)
            print(f"Player {current_player} is forced to take the last item.")
            print(f"Player {3 - current_player} wins!")
            break

        jar_index, remove_count = get_move(current_player, jars)
        jars[jar_index] -= remove_count
        current_player = 3 - current_player  # Switch players

# Run the game
three_jar_game()
