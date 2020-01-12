from gui.interface import run_interface
from game.game_board import GameBoard


class Options:
    player_count = 6
    cli_inputs = True
    use_gui = False
    player_names_random = True


def welcome_message():
    print("***** Welcome to LeWi! *****\n")
    print('If you are new to the game checkout the "readme".')
    print('Enter "h" for help.')


def display_help():
    print('"h"      displays this information')
    print('"n"      starts new game')
    print('"p"      changes how many player will play the game\n'
          '         (note that only 3-6 players are allowed to play the game)')
    print('"d"      open developer options')
    print('"exit"   exits the game')
    print()


def display_developer_help():
    print('"pn"     toggle player names on/off')
    print('"o"      displays all set options')


def change_player_count():
    print('** Player Count **')
    while True:
        print('Currently the player count is set to [{}]'.format(Options.player_count))
        print('Enter the amount of players that want to play the game:')
        try:
            command = int(input())
            if command < 3 or command > 6:
                print("The game only supports 3-6 players!")
                continue
            else:
                Options.player_count = command
                print("Changes accepted!")
                break
        except ValueError:
            print("Incorrect input! Wizard, I need a number!")
            continue


def change_player_names_random():
    if Options.player_names_random:
        Options.player_names_random = False
    else:
        Options.player_names_random = True
    print("Choose random player names is now set to [{}]".format(Options.player_names_random))


def user_input():
    command = input().casefold()
    if command == "h" or command == "help":
        display_help()
    elif command == "exit" or command == "x":
        exit()
    elif command == "p" or command == "player":
        change_player_count()
    elif command == "":
        welcome_message()
    elif command == "d":
        dev_options_menu()
    elif command == "n" or command == "new game" or command == "newgame":
        g = GameBoard(Options.player_count,
                      Options.cli_inputs,
                      Options.player_names_random)
        g.start()
    else:
        print('I did not get you there. \n'
              'If you need help just type "h" and then press enter')


def display_all_options():
    print('** Display_Options **')
    print('player_count = [{}]'.format(Options.player_count))
    print('cli_inputs = [{}]'.format(Options.cli_inputs))
    print('use_gui = [{}]'.format(Options.use_gui))
    print('player_names_random = [{}]'.format(Options.player_names_random))
    print()


def dev_options_menu():
    while True:
        print('* Dev Menu *')
        print('Note that these options are experimental and might not work properly!')
        print('Options: \n'
              '"prn"    toggle player random names\n'
              '"i"      starts interface\n'
              '"o"      displays state of all options\n'
              '"x"      get back to the main menu\n')
        command = input().casefold()
        if command == "prn":
            change_player_names_random()
        elif command == "i":
            print("Running Interface...")
            run_interface()
        elif command == "x" or command == "exit":
            break
        elif command == "o":
            display_all_options()
        else:
            continue


def run_menu():
    """Runs the menu"""
    while True:
        print("\n*** MainMenu ***")
        user_input()
