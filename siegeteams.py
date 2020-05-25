# Simple Team Generator
# By Dustin Sison

from random import randint
active = True
team_alpha = []
team_omega = []
players = []
team_size_limit = 0

def print_players(player):
    player_number = 0
    for i in player:
        player_number = player_number + 1
        print(str(player_number) + " " + str(i))

# Function which assigns players to teams
def assign_players(player):
    for i in player:
        team_assignment = randint(0, 1)
        if team_assignment == 0:
            if len(team_alpha) == team_size_limit:
                team_omega.append(i)
            else:
                team_alpha.append(i)
        else:
            if len(team_omega) == team_size_limit:
                team_alpha.append(i)
            else:
                team_omega.append(i)
    # Prints results
    print(" ")
    print("Attackers/Blue Team: ")
    print_players(team_alpha)
    print(" ")
    print("Defenders/Orange Team: ")
    print_players(team_omega)
    print(" ")

def remove_players():
    # Asks the user if any of the registered players are missing and removes them from the list if so.
    remove_player = int(input("Anyone missing? Type the number of the player missing (0 = no one): "))
    removal_function = True

    while removal_function:
        try:
            if remove_player == 0:
                print("> No one was removed.")
                removal_function = False
            else:
                removed_name = players[remove_player - 1]
                del players[remove_player - 1]
                print("> Removed player " + removed_name)
                print(" ")
                try:
                    print("Updated Player List: ")
                    print_players(players)
                    print(" ")
                    remove_answer = int(input(
                        "Anyone else? Enter another number to remove another player, or press Enter to continue: "))
                    if int(remove_answer) <= len(players):
                        remove_player = remove_answer
                        print(" ")
                    else:
                        print(" ")
                        removal_function = False
                except ValueError:
                    print(" ")
                    removal_function = False
        except ValueError:
            print(" ")

while active:
    retries = 1
    players = ["XMasterPrime", "sayonarapuppy", "Willis", "FueledByJon", "g dot", "Classixxs", "GPWAP2", "ap", "Andrew", "Domisteez", "Ahh"]

    print("Registered Players: ")
    print_players(players)

    remove_players()

    print("Updated Player List: ")
    print_players(players)
    print(" ")

    input("Press Enter to generate teams")
    print(" ")

    # Limit team sizes by number of total players, to ensure balanced teams
    if len(players) >= 7:
        team_size_limit = 4
    else:
        team_size_limit = 3
    while retries == 1:
        # Uses function to assign teams
        assign_players(players)

        endgame = int(input("Press 1 to reroll, press 2 to start over, or press 3 to quit: "))
        if endgame == 1:
            team_alpha = []
            team_omega = []
        elif endgame == 2:
            retries = 0
            team_alpha = []
            team_omega = []
            continue
        elif endgame == 3:
            retries = 0
            active = False