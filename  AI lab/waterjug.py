def display_state(jug_a, jug_b):
    print(f"\nCurrent State => Jug A: {jug_a}L | Jug B: {jug_b}L")

def water_jug_game():
    capacity_a = 4
    capacity_b = 3
    goal = 2
    jug_a = 0
    jug_b = 0

    print("🌊 Water Jug Problem Game")
    print(f"Goal: Measure exactly {goal} liters.")
    print("Jug A capacity: 4L | Jug B capacity: 3L")

    while True:
        display_state(jug_a, jug_b)

        print("\nChoose your move:")
        print("1. Fill Jug A")
        print("2. Fill Jug B")
        print("3. Empty Jug A")
        print("4. Empty Jug B")
        print("5. Pour Jug A -> Jug B")
        print("6. Pour Jug B -> Jug A")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            jug_a = capacity_a
        elif choice == '2':
            jug_b = capacity_b
        elif choice == '3':
            jug_a = 0
        elif choice == '4':
            jug_b = 0
        elif choice == '5':
            transfer = min(jug_a, capacity_b - jug_b)
            jug_a -= transfer
            jug_b += transfer
        elif choice == '6':
            transfer = min(jug_b, capacity_a - jug_a)
            jug_b -= transfer
            jug_a += transfer
        elif choice == '7':
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if jug_a == goal or jug_b == goal:
            display_state(jug_a, jug_b)
            print("🎉 Congratulations! You've measured exactly 2 liters.")
            break
water_jug_game()
