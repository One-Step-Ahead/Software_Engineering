from gui.interface import run_interface


class Options:
    player_count = 6
    cli_inputs = True
    use_gui = False
    player_names = False
    player_names_random = False


def ask_what_to_do():
    print("*** MainMenu ***")


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


def change_player_names():
    while True:
        print("Player names support is set to [{}]".format(Options.player_names))
        command = input().casefold()
        if command == "true":
            Options.player_names = True
            print("Set!")
            break
        elif command == "false":
            Options.player_names = False
            print("Set!")
            break
        else:
            continue


def user_input():
    command = input().casefold()
    if command == "h" or command == "help":
        display_help()
    elif command == "exit":
        exit()
    elif command == "p" or command == "player":
        change_player_count()
    elif command == "":
        welcome_message()
    else:
        print('I did not get you there. \n'
              'If you need help just type "h" and then press enter')


def dev_options_menu():
    while True:
        print('* Dev Menu *')
        print('Note that these options are experimental and might not work properly!')
        print('Options: \n'
              '"pn"     toggle player names support\n'
              '"prn"    toggle player random names\n'
              '"i"      starts interface')
        command = input().casefold()
        if command == "":
            continue
        elif command == "pn":
            change_player_names()
        elif command == "prn":
            print("Error! This is not working!")
        elif command == "i":
            run_interface()


def run_menu():
    """Runs the menu"""
    while True:
        ask_what_to_do()
        user_input()


run_menu()
