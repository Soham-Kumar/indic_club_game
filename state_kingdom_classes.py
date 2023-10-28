import pandas as pd

# Read data excel sheet
file_path = "indic_club_stats.xlsx"
df = pd.read_excel(file_path)


# Defining classes
class States:
    def __init__(
        self,
        name,
        strategy,
        army,
        resource,
        navy,
        resource_on_loot,
        resource_on_invasion,
    ):
        self.name = name
        self.strategy = strategy
        self.army = army
        self.resource = resource
        self.navy = navy
        self.resource_on_loot = resource_on_loot
        self.resource_on_invasion = resource_on_invasion


class Kingdom:
    def __init__(
        self,
        name,
        king,
        strategy,
        army,
        resource,
        navy,
        invasion_damage_on_army_of_defender,
        invasion_damage_on_army_of_attacker,
        loot_damage_on_army_of_defender,
        loot_damage_on_army_of_attacker,
        resource_on_loot,
        resource_on_invasion,
        conquered_states,
    ):
        self.name = name
        self.king = king
        self.strategy = strategy
        self.army = army
        self.resource = resource
        self.navy = navy
        # self.invasion_damage_on_army_of_defender = damage_on_army_of_defender
        # self.invasion_damage_on_army_of_attacker = damage_on_army_of_attacker
        # self.loot_damage_on_army_of_defender = loot_damage_on_army_of_defender
        # self.loot_damage_on_army_of_attacker = loot_damage_on_army_of_attacker
        self.resource_on_loot = resource_on_loot
        self.resource_on_invasion = resource_on_invasion
        self.conquered_states = []


no_of_kingdoms = 7
no_of_states = 23

# List of kingdoms and states
kingdoms = []
states = []


# Initialise kingdoms and states
for i in range(no_of_kingdoms):
    kingdom = Kingdom(
        df["Kingdom"][i],
        df["King"][i],
        df["Strategy"][i],
        df["Army"][i],
        df["Resource"][i],
        df["Navy"][i],
        0,
        0,
        0,
        0,
        df["Resource on loot"][i],
        df["Resource on invasion"][i],
        [],
    )
    kingdoms.append(kingdom)

for i in range(no_of_states):
    state = States(
        df["Kingdom"][i + 8],
        df["Strategy"][i + 8],
        df["Army"][i + 8],
        df["Resource"][i + 8],
        df["Navy"][i + 8],
        df["Resource on loot"][i + 8],
        df["Resource on invasion"][i + 8],
    )

    states.append(state)


# Extract name of kingdoms and states
kingdom_names = []
state_names = []
for kingdom in kingdoms:
    kingdom_names.append(kingdom.name)
for state in states:
    state_names.append(state.name)


kingdoms_and_states = []  # List of all kingdom and state objects
kingdoms_and_states = kingdoms + states

kingdom_and_state_names = (
    kingdom_names + state_names
)  # List of all kingdom and state names
