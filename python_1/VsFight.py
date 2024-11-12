import random
#Human Vs AI Tournament Of Warriors 

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def attack_character(self, other):
        other.health -= self.attack
        print(f"{self.name} attacks {other.name} for {self.attack} damage!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} health!")

class Game:
    def __init__(self):
        self.characters = [
            Character("Goku", 100, 25), Character("Naruto", 80, 30), Character("Mario", 90, 20),
            Character("Link", 85, 22), Character("Sonic", 75, 35), Character("Luffy", 95, 27),
            Character("Kirby", 80, 25), Character("Pikachu", 70, 20), Character("Deku", 85, 28),
            Character("Saitama", 110, 40), Character("Vegeta", 95, 30), Character("Zoro", 85, 29),
            Character("Alucard", 90, 32), Character("Sephiroth", 100, 35), Character("Cloud", 90, 30),
            Character("Shrek", 100, 20), Character("Darth Vader", 95, 34), Character("Superman", 120, 40),
            Character("Wonder Woman", 95, 28), Character("Batman", 85, 25), Character("Spiderman", 85, 26),
            Character("Iron Man", 90, 29), Character("Captain America", 100, 25), Character("Thor", 110, 33),
            Character("Hulk", 120, 45), Character("Ryu", 90, 30), Character("Ken", 90, 30),
            Character("Chun-Li", 80, 27), Character("Mewtwo", 90, 31), Character("Ash Ketchum", 70, 20),
            Character("Froppy", 75, 22), Character("Kakashi", 85, 28), Character("Itachi", 80, 26),
            Character("Baku", 85, 29), Character("Lelouch", 70, 15), Character("Edward Elric", 80, 24),
            Character("Ryuko", 75, 23), Character("Yusuke", 90, 27), Character("Dio", 95, 35),
            Character("Kirito", 85, 29), Character("Asuka", 70, 20), Character("Shinji", 75, 21),
            Character("Sailor Moon", 80, 22), Character("Ichigo", 90, 30), Character("Natsu", 85, 28),
            Character("Guts", 100, 30), Character("Alphonse", 90, 24), Character("Hawkeye", 80, 25),
            Character("Scar", 90, 28), Character("Gon", 75, 22), Character("Killua", 85, 27),
            Character("Levi", 90, 29), Character("Mikasa", 85, 28), Character("Erza", 80, 25),
            Character("Rin", 70, 20), Character("Saber", 85, 26), Character("Todoroki", 80, 24),
            Character("Rem", 75, 22), Character("Emilia", 70, 21), Character("Kaguya", 85, 27),
            Character("Hinata", 75, 23), Character("Neji", 80, 26), Character("Rock Lee", 90, 29),
            Character("Shikamaru", 80, 24), Character("Gaara", 90, 30), Character("Jiraiya", 85, 28),
            Character("Orochimaru", 90, 30), Character("Aang", 85, 27), Character("Zuko", 80, 25),
            Character("Katara", 75, 23), Character("Sokka", 70, 20), Character("Toph", 80, 22),
            Character("Loki", 85, 29), Character("Thanos", 100, 35), Character("Deadpool", 90, 28),
            Character("Wolverine", 100, 30), Character("Green Lantern", 90, 25), Character("Flash", 85, 27),
            Character("Aquaman", 90, 28), Character("Gambit", 80, 24), Character("Storm", 75, 22),
            Character("Mystique", 70, 20), Character("Psylocke", 80, 25), Character("Rogue", 90, 30),
            Character("Black Panther", 85, 29), Character("Gamora", 80, 26), Character("Rocket Raccoon", 70, 20),
            Character("Groot", 100, 10), Character("Venom", 95, 34), Character("Carnage", 90, 32),
            Character("Silver Surfer", 100, 35), Character("Doctor Strange", 85, 28), Character("Moon Knight", 90, 29),
            Character("Vision", 95, 31), Character("Scarlet Witch", 90, 30), Character("Black Widow", 80, 26),
            Character("Agent Carter", 75, 22), Character("Blade", 85, 29), Character("Ghost Rider", 90, 30),
            Character("Doctor Fate", 95, 34), Character("Zatanna", 80, 25), Character("Green Arrow", 85, 27),
            Character("Hawkeye", 80, 24), Character("Starfire", 90, 30), Character("Beast Boy", 75, 22),
            Character("Raven", 85, 26), Character("Cyborg", 90, 29), Character("Nightwing", 85, 28),
            Character("Red Hood", 80, 25), Character("Batgirl", 75, 23), Character("Morrigan", 85, 27),
            Character("Dante", 90, 30), Character("Ryu Hayabusa", 95, 33), Character("Geralt", 100, 32),
            Character("Kratos", 120, 40), Character("Cloud Strife", 90, 30), Character("Zelda", 80, 25),
            Character("Link", 85, 22), Character("Sora", 80, 26), Character("Mickey Mouse", 75, 20),
            Character("Donald Duck", 70, 20), Character("Goofy", 80, 22), Character("Doraemon", 75, 25),
            Character("Shinchan", 60, 10), Character("Tomo", 70, 20), Character("Ghibli Spirit", 80, 22),
            Character("Kiki", 75, 25), Character("Totoro", 100, 10), Character("Ashitaka", 85, 30),
            Character("Nausicaa", 80, 28), Character("Chihiro", 70, 20), Character("No-Face", 100, 5),
            Character("Spirited Away Spirit", 85, 25), #Charcters 
        ]

        self.wins = {"player": 0, "computer": 0}
        self.items = {
            "eraser": 1,
            "revival": 1,
            "healing_potion": 2,
            "attack_boost": 1,
            "defense_shield": 1,
            "speed_boost": 1,
            "double_damage": 1,
            "shield_bash": 1,
            "critical_hit": 1,
            "health_potion": 2,
            "stamina_boost": 1,
            "magic_potion": 1,
            "invincibility": 1,
            "power_ring": 1,
            "energy_drink": 2,
            "strength_boost": 1,
            "defense_boost": 1,
            "dodge_charm": 1,
            "healing_elixir": 1,
            "poison_resistance": 1,
            "speedy_feet": 1,
            "recovery_bandage": 2,
            "strength_shard": 1,
            "energy_shard": 1,
            "mind_shard": 1,
            "vision_shard": 1,
            "sight_potion": 1,
            "fire_blast": 1,
            "ice_blast": 1,
            "thunder_blast": 1,
            "wind_blast": 1,
            "earth_blast": 1,
            "water_blast": 1,
            "light_blast": 1,
            "dark_blast": 1,
            "status_ailment": 1,
            "elemental_rune": 1,
            "ultimate_rune": 1,
            "quick_heal": 2,
            "power_armor": 1,
            "stealth_cloak": 1,
            "battle_horn": 1,
            "luck_token": 1,
            "wisdom_token": 1,
            "endurance_token": 1,
            "bravery_token": 1,
            "guardian_angel": 1,
        }
        #Power Ups items 
        self.available_items = list(self.items.keys())

    def choose_character(self):
        print("Choose your character:")
        for i, char in enumerate(self.characters):
            print(f"{i + 1}: {char.name}")
        choice = int(input("Enter the number of your choice: ")) - 1
        return self.characters[choice]

    def random_character(self):
        return random.choice(self.characters)

    def use_item(self, character):
        print("Items available:")
        for item, count in self.items.items():
            if count > 0:
                print(f"{item} (x{count})")

        item_choice = input("Do you want to use an item? (yes/no): ").strip().lower()
        if item_choice == "yes":
            item_name = input("Enter the name of the item: ").strip().lower()
            if item_name in self.items and self.items[item_name] > 0:
                if item_name == "eraser":
                    print(f"{character.name} has been erased!")
                    return False  # Character is erased, can't fight
                elif item_name == "revival":
                    character.heal(30)
                    self.items["revival"] -= 1
                    print(f"{character.name} has been revived!")
                elif item_name == "healing_potion":
                    character.heal(20)
                    self.items["healing_potion"] -= 1
                elif item_name == "attack_boost":
                    character.attack += 10
                    self.items["attack_boost"] -= 1
                    print(f"{character.name} gains an attack boost! New attack: {character.attack}")
                elif item_name == "defense_shield":
                    character.health += 10
                    self.items["defense_shield"] -= 1
                    print(f"{character.name} gains a defense shield! New health: {character.health}")
                elif item_name == "speed_boost":
                    character.attack += 5  # Temporary speed effect
                    self.items["speed_boost"] -= 1
                    print(f"{character.name} gains a speed boost! New attack: {character.attack}")
                # Add other item effects here
                else:
                    print(f"{item_name} has been used!")
                    self.items[item_name] -= 1
            else:
                print("Invalid or unavailable item.")
        return True  # item has or has not worked

    def reward_item(self):
        item = random.choice(self.available_items)
        self.items[item] += 1
        print(f"You received a random item: {item}!")

    def battle(self, player_char, computer_char):
        print(f"\nBattle starts: {player_char.name} vs {computer_char.name}!")
        while player_char.is_alive() and computer_char.is_alive():
            player_char.attack_character(computer_char)
            if computer_char.is_alive():
                computer_char.attack_character(player_char)
    #Item recived

        if player_char.is_alive():
            print(f"{player_char.name} wins!")
            self.wins["player"] += 1
            return player_char.name
        else:
            print(f"{computer_char.name} wins!")
            self.wins["computer"] += 1
            self.reward_item()  # battle/ end of battle
            return computer_char.name

    def display_score(self):
        print(f"Score: Player {self.wins['player']} - {self.wins['computer']} Computer")

    def play(self):
        while self.wins["player"] < 5 and self.wins["computer"] < 5:
            player_char = self.choose_character()
            if not self.use_item(player_char):
                print(f"{player_char.name} cannot fight!")
                continue
            computer_char = self.random_character()
            winner = self.battle(player_char, computer_char)
            self.display_score()

        overall_winner = "Player" if self.wins["player"] == 5 else "Computer"
        print(f"{overall_winner} wins the game!")
#winner has won 
if __name__ == "__main__":
    game = Game()
    game.play()
#end