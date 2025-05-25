# ==================== ui.py ====================

def display_menu():
    """
    Print the main action menu to the console.
    """
    print("""
1. Feed
2. Play
3. Sleep
4. Show Status
5. Show Recent History
6. Exit
""")


def get_choice(prompt='Your choice: '):
    """
    Prompt the user for input and strip whitespace.

    Returns:
    - str: the user's raw input
    """
    return input(prompt).strip()


def show_status(stats):
    """
    Display the pet's current stats neatly.

    Parameters:
    - stats (dict): output from Pet.status()
    """
    for key, value in stats.items():
        print(f"{key.title():<9}: {value}/100")


def show_history(history, count=5):
    """
    Display the most recent history entries.

    Parameters:
    - history (list of str): pet.history list
    - count (int): how many recent entries to show
    """
    recent = history[-count:]
    if recent:
        print("Recent activities:")
        for entry in recent:
            print(f" - {entry}")
    else:
        print("No history yet.")
