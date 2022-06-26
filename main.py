import time
import random

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp, get_date

from controllers.tournament_manager import CreateTournament
# from controllers.player_manager import CreatePlayer, ChangePlayerRank


def main(): 

    CreateTournament()

        

if __name__ == "__main__":
    main()
 