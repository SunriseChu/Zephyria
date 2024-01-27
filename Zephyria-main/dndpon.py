# Import the os module to clear the console
import os

# Function to clear the console screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary to store class stats
class_stats = {
    "Fighter": {"strength": 2, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 1},
    "Barbarian": {"strength": 2, "dexterity": 0, "constitution": 2, "intelligence": 0, "wisdom": 0, "charisma": 0},
    "Monk": {"strength": 0, "dexterity": 2, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 0},
    "Paladin": {"strength": 2, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 1},
    "Ranger": {"strength": 0, "dexterity": 2, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 0},
    "Cleric": {"strength": 0, "dexterity": 0, "constitution": 2, "intelligence": 0, "wisdom": 0, "charisma": 1},
    "Druid": {"strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 2, "charisma": 0},
    "Rogue": {"strength": 0, "dexterity": 2, "constitution": 0, "intelligence": 1, "wisdom": 0, "charisma": 0},
    "Sorcerer": {"strength": 0, "dexterity": 0, "constitution": 1, "intelligence": 2, "wisdom": 0, "charisma": 1},
    "Bard": {"strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 3},
    "Warlock": {"strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 3},
    "Wizard": {"strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 3, "wisdom": 0, "charisma": 0},
}

# Dictionary to store race stats
race_stats = {
    "Dragonborn": {"health_bonus": 3, "force_damage": 5, "magic_damage": 2, "defense": 15},
    "Dwarf": {"health_bonus": 3, "force_damage": 8, "magic_damage": 1, "defense": 13},
    "Elf": {"health_bonus": 2, "force_damage": 6, "magic_damage": 3, "defense": 14},
    "Gnome": {"health_bonus": 3, "force_damage": 4, "magic_damage": 4, "defense": 14},
    "Halfling": {"health_bonus": 2, "force_damage": 3, "magic_damage": 5, "defense": 14},
    "Half-Elf": {"health_bonus": 2, "force_damage": 3, "magic_damage": 6, "defense": 13},
    "Half-Orc": {"health_bonus": 2, "force_damage": 4, "magic_damage": 4, "defense": 14},
    "Human": {"health_bonus": 3, "force_damage": 3, "magic_damage": 5, "defense": 14},
    "Tiefling": {"health_bonus": 2, "force_damage": 2, "magic_damage": 7, "defense": 11},
    "Drow": {"health_bonus": 1, "force_damage": 3, "magic_damage": 5, "defense": 12},
    "Gith": {"health_bonus": 1, "force_damage": 5, "magic_damage": 6, "defense": 11},
    "Goblin": {"health_bonus": 1, "force_damage": 2, "magic_damage": 8, "defense": 10},
}

# Welcome message and narrative
print("Welcome to the Adventure Game!")
print("\nYou wake up in the middle of nowhere, surrounded by mist and uncertainty. As you glance at yourself, you try to remember anything about who you are.")

# Prompt for adventurer's name
name = input("\nYou scratch your head trying to remember your name... There is only one name that comes to mind...")

# Capitalize the first letter of the name and convert the rest to lowercase
name = name.capitalize()

# Prompt for adventurer's race
print("\nYou glance at yourself, looking over your hands, hurt. As you walk up to a puddle of water nearby, you realize you are a...")
for i, race in enumerate(race_stats.keys(), start=1):
    print(f"{i}. {race}")

race_choice = input("Enter the number corresponding to your desired race: ")
race_keys = list(race_stats.keys())
race = race_keys[int(race_choice) - 1]

# Prompt for adventurer's class
print("\nFeeling overwhelmed by pain and uncertainty, you look over yourself again, trying to find your sword or your inner magic power...")
for i, char_class in enumerate(class_stats.keys(), start=1):
    print(f"{i}. {char_class}")

class_choice = input("Enter the number corresponding to your desired class: ")
class_keys = list(class_stats.keys())
char_class = class_keys[int(class_choice) - 1]

# Combine class and race stats
combined_stats = {
    "force_damage": race_stats[race]["force_damage"],
    "magic_damage": race_stats[race]["magic_damage"],
    "defense": race_stats[race]["defense"],
    "strength": class_stats[char_class]["strength"],
    "dexterity": class_stats[char_class]["dexterity"],
    "constitution": class_stats[char_class]["constitution"],
    "intelligence": class_stats[char_class]["intelligence"],
    "wisdom": class_stats[char_class]["wisdom"],
    "charisma": class_stats[char_class]["charisma"],
}

# Prompt for adventurer's level
level_str = input("\nYou try to remember again if you were proficient at anything... ")

# Convert level from string to integer
level = int(level_str)

# Calculate health with race bonus
health = level + 6 + race_stats[race]["health_bonus"]

# Create description
description = f"{name} the {race} {char_class}"

# Clear the console
clear_console()

# Display character information
print("\nCharacter Information:")
print(f"\n{name} is a {race} {char_class} with level {level}.")
print(f"Health: {health}")
print(f"Force Damage: {combined_stats['force_damage']}")
print(f"Magic Damage: {combined_stats['magic_damage']}")
print(f"Defense: {combined_stats['defense']}")
for attribute, value in class_stats[char_class].items():
    print(f"{attribute.capitalize()}: {value}")
print(f"\nDescription: {description}")
