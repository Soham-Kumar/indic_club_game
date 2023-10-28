import PySimpleGUI as sg
import state_kingdom_classes
import LID
import current_stats

number_of_players = 0
current_player = 1


def update_player(current_player):
    if current_player <= number_of_players:
        return current_player + 1
    else:
        return 1


def no_of_people():
    global number_of_players
    layout_no_of_players = [
        [sg.Text("Enter the number of players between 3 to 7: ")],
        [sg.InputText()],
        [sg.Button("Start Game")],
    ]
    window = sg.Window("Input Window", layout_no_of_players)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Start Game" or "\r":
            if int(values[0]) < 3 or int(values[0]) > 7:
                sg.popup("Please enter a number between 3 to 7")
                no_of_people()
            else:
                number_of_players = int(values[0])
                main_loop()
        window.close()


def main_loop():
    global current_player
    current_stats.display_current_stats()
    layout = [[sg.Text(f"Current Player: {current_player}")], [sg.Button("Play")]]
    window = sg.Window("Player Update Example", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Play":
            LID.action(state_kingdom_classes.kingdoms_and_states[current_player - 1])
            current_player = update_player(current_player)

        window.close()
    main_loop()


no_of_people()
