# ==================== data_manager.py ====================
from pet import Pet

# Number of fields before history in save file
SAVE_FIELDS = 5

def load_pet(filename):
    """
    Load a Pet object from a CSV-like text file.

    File format:
        name,species,hunger,happiness,energy,history1|history2|...

    Returns:
    - Pet object if load succeeds
    - None if file not found or format error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line = f.readline().strip()
        parts = line.split(',')
        # Validate minimum fields
        if len(parts) < SAVE_FIELDS:
            raise ValueError("Invalid save format")
        # Parse basic stats
        name, species = parts[0], parts[1]
        hunger, happiness, energy = map(int, parts[2:5])
        # Parse history if present
        history = parts[5].split('|') if len(parts) > 5 and parts[5] else []
        # Reconstruct Pet
        pet = Pet(name, species)
        pet.hunger, pet.happiness, pet.energy = hunger, happiness, energy
        pet.history = history
        return pet
    except FileNotFoundError:
        # No existing save file
        return None
    except Exception as e:
        print("Load error:", e)
        return None


def save_pet(pet, filename):
    """
    Save a Pet object to a text file in CSV-like format.

    Writes: name,species,hunger,happiness,energy,history1|history2|...
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            history_str = '|'.join(pet.history)
            line = f"{pet.name},{pet.species},{pet.hunger},{pet.happiness},{pet.energy},{history_str}"
            f.write(line)
    except Exception as e:
        print("Save error:", e)

