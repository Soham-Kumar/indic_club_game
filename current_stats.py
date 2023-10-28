import PySimpleGUI as sg
import state_kingdom_classes


def display_current_stats():
    data = [
        [
            kingdom.name,
            kingdom.king,
            kingdom.strategy,
            kingdom.army,
            kingdom.resource,
            kingdom.navy,
            ", ".join([state.name for state in kingdom.conquered_states]),
        ]
        for kingdom in state_kingdom_classes.kingdoms
    ]

    layout = [
        [
            sg.Table(
                values=data,
                headings=[
                    "Name",
                    "King",
                    "Strategy",
                    "Army",
                    "Resource",
                    "Navy",
                    "Conquered States",
                ],
                auto_size_columns=True,
                display_row_numbers=False,
                justification="center",
                # auto_size_columns=True,
            )
        ],
        [sg.Button("Close")],
    ]

    # Create the window
    window = sg.Window("Current Stats", layout)

    # Read the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Close":
            break

    # Close the window
    window.close()
