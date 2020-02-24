# Siege Teams Generator
# By Dustin Sison

from random import randint
blue_team = []
orange_team = []
players = ["XMasterPrime", "sayonarapuppy", "Willis", "FueledByJon", "g dot", "Classixxs", "GPWAP2"]
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
            if len(blue_team) == team_size_limit:
                orange_team.append(i)
            else:
                blue_team.append(i)
        else:
            if len(orange_team) == team_size_limit:
                blue_team.append(i)
            else:
                orange_team.append(i)

print("Registered Players: ")
print_players(players)

# Asks the user if any of the registered players are missing and removes them from the list if so.
remove_player = int(input("Anyone missing? Type the number of the player missing (0 = no one): "))
if remove_player == 0:
    print("> No one was removed.")
else:
    del players[remove_player - 1]
    print("> Removed player " + str(remove_player))
print(" ")
print("Updated Player List: ")
print_players(players)
print(" ")
input("Press Enter to generate teams")
print(" ")

# Limit team sizes by number of total players, to ensure balanced teams
if len(players) == 7:
    team_size_limit = 4
else:
    team_size_limit = 3

# Uses function to assign teams
assign_players(players)

#Prints results
print(" ")
print("Blue Team: ")
print_players(blue_team)
print(" ")
print("Orange Team: ")
print_players(orange_team)
print(" ")
input("Press Enter to terminate the program.")