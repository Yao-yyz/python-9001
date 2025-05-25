"""
The code is split into four modules by responsibility: 
pet.py defines the Pet class and all its behaviors, showcasing object-oriented design; 
data_manager.py handles loading and saving, demonstrating file I/O and exception handling; 
ui.py provides user-interface functions for menu display, input collection, and result presentation; 
main.py serves as the program entry point, orchestrating the main loop and coordinating the modules.
"""
# ==================== main.py ====================
import sys
from pet import Pet
from data_manager import load_pet, save_pet
from ui import display_menu, get_choice, show_status, show_history


def create_new_pet():
    """
    Guide user through creating a new Pet instance.

    Prompts for name and species selection.
    Returns:
    - Pet: newly created Pet object
    """
    name = input("Enter your pet's name: ")
    options = Pet.species_options
    print("Choose species:")
    for i, s in enumerate(options, 1):
        print(f"{i}. {s}")
    while True:
        choice = get_choice('>>> ')
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(options):
                return Pet(name, options[idx - 1])
        print("Invalid choice, enter a number.")


def main():
    """
    Program entry point and main event loop.

    - Loads existing pet from file or creates new one.
    - Displays a menu and processes user commands until exit.
    """
    # Determine save filename from command-line argument or default
    filename = sys.argv[1] if len(sys.argv) > 1 else 'pet_data.txt'

    # # Load or create pet  Wrong_cannot creat new pet.
    # pet = load_pet(filename) or create_new_pet()
    # print(f"🐾 Welcome: {pet.name} the {pet.species}")

    # Try loading save file
    old_pet = load_pet(filename)
    if old_pet:
        choice = input(f"Save file \"{filename}\" found. Load it? [Y/N]: ").strip().lower()
        if choice == 'y':
            pet = old_pet
            print(f"✔ Loaded: {pet.name} the {pet.species}")
        else:
            pet = create_new_pet()
    else:
        pet = create_new_pet()

    print(f"🐾 Welcome: {pet.name} the {pet.species}")

    # Main loop: decay stats, then handle user action
    while True:
        pet.time_decay()
        display_menu()
        cmd = get_choice()

        if cmd == '1':
            old, new = pet.feed()
            print(f"Hunger: {old} → {new}")
        elif cmd == '2':
            print("That was fun!" if pet.play() else f"{pet.name} is too tired.")
        elif cmd == '3':
            hrs = get_choice("Sleep hours? ")
            try:
                hrs = int(hrs)
            except ValueError:
                print("Invalid input, defaulting to 2 hours")
                hrs = 2
            old, new = pet.sleep(hrs)
            print(f"Energy: {old} → {new}")
        elif cmd == '4':
            show_status(pet.status())
        elif cmd == '5':
            show_history(pet.history)
        elif cmd == '6':
            save_pet(pet, filename)
            print("Goodbye! 👋")
            break
        else:
            print("Please select a valid option (1-6).")
            continue

        # Save after each valid action
        save_pet(pet, filename)


if __name__ == '__main__':
    main()
