import PySimpleGUI as sg
import state_kingdom_classes

# import action_functions

# conquered_states = []

# def list_of_conquered_states():
#     for kingdom in state_kingdom_classes.kingdoms:
#         for i in kingdom.conquered_states:
#            conquered_states.append(i)


def loot(
    attacker: state_kingdom_classes.Kingdom, defender: state_kingdom_classes.Kingdom
):
    for k in state_kingdom_classes.kingdoms_and_states:
        if k.name == defender:
            defender = k
        if k.name == attacker:
            attacker = k
    if (
        attacker.army
        - (0.3 * defender.army * defender.strategy * 100)
        / (attacker.army * attacker.strategy)
        > 0
    ):
        defender.army = defender.army - (0.3 * defender.army)
        defender.resource = defender.resource - (0.5 * defender.resource)
        attacker.army = attacker.army - (
            0.3 * defender.army * defender.strategy * 100
        ) / (attacker.army * attacker.strategy)
        attacker.resource = attacker.resource + (0.5 * defender.resource)
    else:
        sg.popup("Illegal Battle")
        action(attacker)
        # loot(attacker, defender)


def invade(
    attacker: state_kingdom_classes.Kingdom, defender: state_kingdom_classes.Kingdom
):
    for k in state_kingdom_classes.kingdoms_and_states:
        if k.name == defender:
            defender = k
        if k.name == attacker:
            attacker = k
    if (
        attacker.army
        - (defender.army * defender.strategy * 100)
        / (attacker.army * attacker.strategy)
        > 0
    ):
        defender.army = defender.army - (defender.army * defender.strategy * 100) / (
            attacker.army * attacker.strategy
        )
        defender.resource = defender.resource - (defender.resource * 0.8)
        attacker.army = attacker.army - (defender.army * defender.strategy * 100) / (
            attacker.army * attacker.strategy
        )
        attacker.resource = attacker.resource + (defender.resource * 0.8)
        attacker.conquered_states.append(defender)
    else:
        sg.popup("Illegal Battle")
        action(attacker)


def navy_invasion(
    attacker: state_kingdom_classes.Kingdom, defender: state_kingdom_classes.Kingdom
):
    for k in state_kingdom_classes.kingdoms_and_states:
        if k.name == defender:
            defender = k
        if k.name == attacker:
            attacker = k
    if (attacker.navy > 0) & (defender.navy > 0):
        if (
            attacker.navy
            - (defender.navy * defender.strategy * 100)
            / (attacker.navy * attacker.strategy)
            > 0
        ):
            defender.navy = defender.navy - (
                defender.navy * defender.strategy * 100
            ) / (attacker.navy * attacker.strategy)
            defender.resource = defender.resource - (defender.resource * 0.8)

            attacker.navy = attacker.navy - (
                defender.navy * defender.strategy * 100
            ) / (attacker.navy * attacker.strategy)
            attacker.resource = attacker.resource + (defender.resource * 0.8)
            attacker.conquered_states.append(defender.name)

        else:
            sg.popup("Illegal Battle")
            action(attacker)
            # navy_invasion(attacker, defender)
    else:
        sg.popup("Illegal Battle")
        action(attacker)


def diplomacy(
    kingdom_1: state_kingdom_classes.Kingdom, kingdom_2: state_kingdom_classes.Kingdom
):
    for k in state_kingdom_classes.kingdoms_and_states:
        if k.name == kingdom_1:
            kingdom_1 = k
        if k.name == kingdom_2:
            kingdom_2 = k
    new_kingdom = state_kingdom_classes.Kingdom()
    new_kingdom.name = kingdom_1.name + " " + kingdom_2.name + " " + "Alliance"
    new_kingdom.army = kingdom_1.army + kingdom_2.army
    new_kingdom.resource = kingdom_1.resource + kingdom_2.resource
    new_kingdom.strategy = (kingdom_1.strategy + kingdom_2.strategy) / 2
    new_kingdom.navy = kingdom_1.navy + kingdom_2.navy
    new_kingdom.conquered_states = (
        kingdom_1.conquered_states + kingdom_2.conquered_states
    )
    state_kingdom_classes.kingdoms_and_states.append(new_kingdom)
    state_kingdom_classes.kingdom_and_state_names.append(new_kingdom.name)

    state_kingdom_classes.kingdom_and_state.pop(kingdom_1)
    state_kingdom_classes.kingdom_and_state.pop(kingdom_2)
    state_kingdom_classes.kingdom_and_state_names.pop(kingdom_1.name)
    state_kingdom_classes.kingdom_and_state_names.pop(kingdom_2.name)


def break_diplomacy(
    kingdom_1: state_kingdom_classes.Kingdom, kingdom_2: state_kingdom_classes.Kingdom
):
    if kingdom_1.name + " " + kingdom_2.name + " " + "Alliance" in (
        state_kingdom_classes.kingdom_and_state_names
    ):
        state_kingdom_classes.kingdoms_and_states.append(kingdom_1)
        state_kingdom_classes.kingdoms_and_states.append(kingdom_2)
        state_kingdom_classes.kingdom_and_state_names.append(kingdom_1.name)
        state_kingdom_classes.kingdom_and_state_names.append(kingdom_2.name)

        state_kingdom_classes.kingdoms_and_states = [
            instance
            for instance in state_kingdom_classes.kingdoms_and_states
            if instance.name != kingdom_1.name + " " + kingdom_2.name + " " + "Alliance"
        ]
        state_kingdom_classes.kingdom_and_state_names = [
            instance
            for instance in state_kingdom_classes.kingdom_and_state_names
            if instance != kingdom_1.name + " " + kingdom_2.name + " " + "Alliance"
        ]
    else:
        sg.popup("No alliance exists between the two kingdoms")
        action(kingdom_1)


def resource_to_army(kingdom, amount):
    conversion_rate = 2
    if kingdom.resource >= amount:
        kingdom.resource = kingdom.resource - amount
        kingdom.army = kingdom.army + (amount / conversion_rate)
    else:
        sg.popup("Not enough resources")
        action(kingdom)


def action(attacker):
    data = []
    for index, kingdom_var in enumerate(state_kingdom_classes.kingdoms_and_states):
        if kingdom_var != attacker:
            kingdom_var.invasion_damage_on_army_of_attacker = int(
                (kingdom_var.army * kingdom_var.strategy * 100)
                / (attacker.army * attacker.strategy)
            )
            kingdom_var.loot_damage_on_army_of_attacker = int(
                (kingdom_var.army * kingdom_var.strategy * 100)
                / (attacker.army * attacker.strategy)
            )

            data.append(
                [
                    index,
                    kingdom_var.name,
                    kingdom_var.army,
                    kingdom_var.resource,
                    kingdom_var.resource_on_loot,
                    kingdom_var.loot_damage_on_army_of_attacker,
                    kingdom_var.resource_on_invasion,
                    kingdom_var.invasion_damage_on_army_of_attacker,
                ]
            )

    layout_lid = [
        [
            sg.Table(
                values=data,
                headings=[
                    "S.No",
                    "Kingdom/State",
                    "Army",
                    "Resources",
                    "Loot Resources gained",
                    "Loot Damage",
                    "Invasion Resources gained",
                    "Invasion Damage",
                ],
                auto_size_columns=True,
                display_row_numbers=False,
                justification="center",
            )
        ],
        [sg.Text("Select the state you want to loot/invade:")],
        [
            sg.Listbox(
                values=state_kingdom_classes.kingdom_and_state_names, size=(35, 6)
            )
        ],
        [
            sg.Button("Loot"),
            sg.Button("Invade"),
            sg.Button("Naval Invasion"),
            sg.Button("Diplomacy"),
            sg.Button("Break Diplomacy"),
            sg.Button("Convert resources to army"),
        ],
    ]
    window = sg.Window("Loot Window", layout_lid)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Loot":
            defender = values[1][0]
            loot(attacker, defender)
        elif event == "Invade":
            defender = values[1][0]
            invade(attacker, defender)

        elif event == "Diplomacy":
            defender = values[1][0]
            diplomacy(attacker, defender)
        elif event == "Break Diplomacy":
            defender = values[1][0]
            break_diplomacy(attacker, defender)
        elif event == "Naval Invasion":
            defender = values[1][0]
            navy_invasion(attacker, defender)
        elif event == "Convert resources to army":
            amount = int(sg.popup_get_text("Enter the amount of resources to convert"))
            resource_to_army(attacker, amount)

        window.close()
