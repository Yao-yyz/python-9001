# ==================== pet.py ====================
import datetime

class Pet:
    """
    Pet represents a virtual pet with hunger, happiness, and energy stats.
    It provides methods to feed, play, sleep, view status, and apply time decay.
    """
    species_options = ("Cat", "Dog", "Rabbit")  # Class variable list of supported species (immutable tuple)

    def __init__(self, name, species):
        """
        Initialize a new Pet instance.

        Parameters:
        - name (str): The name of the pet.
        - species (str): The species of the pet, must be in species_options.
        """
        self.name = name                # Pet's name
        self.species = species          # Pet's species
        # Stats range from 0 to 100:
        self.hunger = 50                # 0=starving, 100=full
        self.happiness = 50             # 0=sad, 100=very happy
        self.energy = 50                # 0=exhausted, 100=full energy
        self.history = []               # List[str]: records of recent actions

    def feed(self, amount=20):
        """
        Feed the pet to reduce hunger.

        - Increases hunger stat by 'amount', capped at 100.
        - Records the change in history.

        Returns:
        - tuple(old_hunger, new_hunger)
        """
        old = self.hunger
        # Increase hunger but do not exceed 100
        self.hunger = min(100, self.hunger + amount)
        # Log the feed event
        self.history.append(f"Fed: {old} → {self.hunger}")
        return old, self.hunger

    def play(self):
        """
        Play with the pet to increase happiness at the cost of energy.

        - Requires at least 10 energy to play.
        - Increases happiness by 15, decreases energy by 15.
        - Records success or failure in history.

        Returns:
        - bool: True if played, False if too tired.
        """
        if self.energy < 10:
            # Not enough energy to play
            self.history.append("Play failed: too tired")
            return False
        old_h, old_e = self.happiness, self.energy
        # Apply stat changes
        self.happiness = min(100, self.happiness + 15)
        self.energy = max(0, self.energy - 15)
        # Log the play event
        self.history.append(f"Played: H {old_h}→{self.happiness}, E {old_e}→{self.energy}")
        return True

    def sleep(self, hours=2):
        """
        Let the pet sleep to restore energy.

        - Restores energy at rate of 10 per hour, capped at 100.
        - Records the sleep event in history.

        Parameters:
        - hours (int): Number of hours to sleep.

        Returns:
        - tuple(old_energy, new_energy)
        """
        old = self.energy
        self.energy = min(100, self.energy + hours * 10)
        self.history.append(f"Slept {hours}h: E {old}→{self.energy}")
        return old, self.energy

    def status(self):
        """
        Get current stats of the pet.

        Returns:
        - dict: {'hunger': int, 'happiness': int, 'energy': int}
        """
        return {"hunger": self.hunger,
                "happiness": self.happiness,
                "energy": self.energy}

    def time_decay(self):
        """
        Apply time-based decay to stats each loop iteration.

        - Decreases hunger by 5, happiness by 2 (half decay), and energy by 5.
        - Logs the decay event in history.
        """
        decay = 5
        self.hunger = max(0, self.hunger - decay)
        self.happiness = max(0, self.happiness - decay // 2)
        self.energy = max(0, self.energy - decay)
        self.history.append("Time passed: -stats")
