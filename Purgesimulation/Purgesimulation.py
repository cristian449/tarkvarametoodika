import random

class Player:
    def __init__(self, health, food, energy, time_left):  
        self.health = health
        self.food = food
        self.energy = energy
        self.time_left = time_left


    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 10
            print("You have eaten to restore energy. Your energy is now:", self.energy)
        else:
            print("You have no food to eat to gain energy.")



    def status(self):
        print(f"Health: {self.health}, Food: {self.food}, Energy: {self.energy}, Time Left: {self.time_left}")



    def end_turn(self):
        if self.time_left > 0:
            self.time_left -= 1
            print(f"Time left has decreased. Time Left: {self.time_left}")
        else:
            print("Time is up, Game over.")





    def event(self):
        events = [
            {"name": "Attack", "health_change": -20, "message": "You were attacked by people luckily you escaped. Lost 20 health."},
            {"name": "Illness", "health_change": -10, "message": "You hadth gotten sick. Lost 10 health."},
            {"name": "Good Weather", "energy_change": +10, "message": "Good weather has made you feel energized."},
            {"name": "Bad Weather", "energy_change": -10, "message": "Bad weather drained your energy. Gained 10 energy."},
            {"name": "Horrible Weather", "energy_change": -20, "message": "Horrible weather drained your energy. Lost 20 energy."},
            {"name": "Found Food", "food_change": 2, "message": "You found food. Gained 2 food."},
            {"name": "Found Food", "food_change": 1, "message": "You found food. Gained 1 food."},
            {"name": "Found Food", "food_change": 3, "message": "You found food. Gained 3 food."},
            {"name": "Found Food", "food_change": 4, "message": "You found food. Gained 4 food."},
            {"name": "Found Food", "food_change": 5, "message": "You found food. Gained 5 food."},
            {"name": "Lost Food", "food_change": -1, "message": "You were robbed. Lost 1 food."},
            {"name": "Lost Food", "food_change": -2, "message": "You were robbed. Lost 2 food."},
            {"name": "Lost Food", "food_change": -3, "message": "You were robbed. Lost 3 food."},
            {"name": "Lost Food", "food_change": -4, "message": "You were robbed. Lost 4 food."},
            {"name": "Neutral Weather", "message": "Neutral Weather, Nothing Changed."},
            {"name": "Obstacles", "energy_change": -5, "message": "Obstacles in your way have drained your energy. Lost 5 energy."},
            {"name": "Medicine", "health_change": +15, "message": "You found medicine and restored health. Gained 15 health."},
            {"name": "Trader", "food_change": +3, "message": "You found a friendly trader and bought food. Gained 3 food."},
            {"name": "Thirst", "energy_change": -10, "message": "You are thirsty nad there are not water sources and lost energy. Lost 10 energy."},
            {"name": "Injury", "health_change": -15, "message": "You cut yourself while attempting to find food. Lost 15 health."},
            {"name": "Water", "energy_change": +15, "message": "You found clean water and restored energy. Gained 15 energy."},
            {"name": "SupplyCache", "energy_change": +15, "health_change": +25, "message": "You found a supply cache and gained 15 energy and 25 health."},
            {"name": "Purgers", "health_change": -30, "message": "You were attacked by Purgers. Lost 30 health."},
        ]
        event = random.choice(events)

        if "health_change" in event:
            self.health += event["health_change"]
            self.health = max(0, self.health)  
        if "energy_change" in event:
            self.energy += event["energy_change"]
            self.energy = max(0, self.energy) 
        if "food_change" in event:
            self.food += event["food_change"]
            self.food = max(0, self.food) 

        print(event["message"])
        self.status()


    def gather(self):
        if self.energy > 0:
            food_gathered = random.randint(1, 5)  
            if self.energy >= food_gathered: 
                self.food += food_gathered
                self.energy -= 5
                print(f"You gathered {food_gathered} food but lost {self.energy} energy.")
            else:
                print("Not enough energy to gather the desired amount of food.")
        else:
            print("You have no energy left to gather resources.")




    def take_turn(self):
        if not hasattr(self, 'available_actions'):
            self.available_actions = ["1", "2", "3", "4"]

        print("\nChoose an action please:")
        if "1" in self.available_actions:
            print("1. Rest Restore energy by consuming food")
        if "2" in self.available_actions:
            print("2. Move forward Decrease time left")
        if "3" in self.available_actions:
            print("3. Take a risk Random event")
        if "4" in self.available_actions:
            print("4. Gather resources")

        choice = input("Choose what you wish to do: ")

        if choice in self.available_actions:
            if choice == "1":
                self.rest()
                self.available_actions.remove("1")
            elif choice == "2":
                self.end_turn()
                self.available_actions = ["1", "2", "3", "4"]
            elif choice == "3":
                self.event()
                self.available_actions.remove("3")
            elif choice == "4":
                self.gather()
                self.available_actions.remove("4")
        else:
            print("Invalid choice. Please choose a number from 1 to4.")
            self.take_turn()

    def game_over(self):
        if self.health <= 0:
            print("Game over! You have no health left.")
            return True
        elif self.time_left <= 0:
            print("Game over! Time is up.")
            return True
        return False






if __name__ == "__main__":
    player = Player(health=80, food=1, energy=50, time_left=20)
    while not player.game_over():
        player.status()
        player.take_turn()

    print("Game over!")
