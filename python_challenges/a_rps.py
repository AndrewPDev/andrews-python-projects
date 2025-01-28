import random # Need random lib for random.choice() function.
import sys
import os

# Need to manually tell the script where a_lib is located.
sys.path.append( os.path.dirname( os.path.dirname( __file__ ) ) )
from a_lib import *

options = ["Rock", "Paper", "Scissors"] # Available options.

comp_count = 0 # Init empty to store computer wins.
user_count = 0 # Init empty to store user wins.

win_count = 5 # How many rounds does the user or computer need to win to win the game.

def UpdateLeaderboard( player_name, wins ):
    lb_file = "game_leaderboards.py"

    lb = LoadData( lb_file )
    if not lb:
        lb = []

    for player in lb:
        if player["name"].lower() == player_name.lower():
            player["wins"] = player["wins"] + wins
            break
        else:
            lb.append( { "name": player_name, "wins": wins } )

    SaveData( "game_leaderboards.py" )

while True: # Keep the loop running until break.
    init_choice = input( "Please choose a number from the above list: " )
    
    user_choice = input( "Rock, paper or scissors ('quit' to exit)? " ) # Get the users input.
    user_choice = user_choice.lower().capitalize() # Convert to lower case then capitalize first letter to match options list.
    
    if user_choice.lower() == "quit": # If users option is 'quit' then break the loop and exit the game.
        print( "Goodbye.." )
        break

    if user_choice not in options: # if users choice isn't in the options then repeat the loop.
        print( "Choice must be rock, paper or scissors ('quit' to exit the game)" )
        continue

    comp_choice = random.choice( options ) # Computers choice.
    print( f"Computer's Choice: {comp_choice}" )

    # If any of these conditions are met then user wins.
    win_conditions = ( user_choice == "Rock" and comp_choice == "Scissors" ) or ( user_choice == "Paper" and comp_choice == "Rock" ) or ( user_choice == "Scissors" and comp_choice == "Paper" )

    if win_conditions:
        print( "You won this round!" )
        user_count = user_count + 1 # Add 1 to users win count.
        if user_count == win_count:
            print( "Congratulations you won this game!" )
            user_name = input( "Please enter your name to update the leaderboard: " )
            UpdateLeaderboard( user_name, 1 )
    else:
        print( "You lost this round!" )
        comp_count = comp_count + 1