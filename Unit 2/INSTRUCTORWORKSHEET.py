def vending_machine():
    # Vending machine menu stored as a dictionary
    menu = {
        "B3": "Nacho Chips",
        "G4": "BBQ Chips",
        "G7": "Plain Chips",
        "D3": "Water",
        "G5": "Cola Soda"
    }

    print("Welcome to the Vending Machine!")
    print("Enter a code (e.g., D3) or 'q' to quit.\n")

    # Start the loop
    while True:
        user_input = input("Enter vending machine code: ").upper()

        # Check for quit condition
        if user_input == "Q":
            print("Stopping vending machine. Goodbye!")
            break

        # Check if the code exists in the menu
        if user_input in menu:
            print(f"Dispensing: {menu[user_input]}\n")
        else:
            print("Invalid code. Please try again.")