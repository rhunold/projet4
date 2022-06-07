import time
import random

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp, get_date

from controllers.controller import CreateTournament, CreatePlayer





# def add_player(player_id):
#     # On s'assure que la liste des joueurs comprend un joueur avec l'id demandé
#     if any(player.player_id == player_id for player in list_players):
#         for player in list_players:
#             if player.player_id == player_id:
#                 # f'"Le joueur {player_id} existe et a été ajouté au tournoi.'
#                 list_participants.append(player)
#         return None 

#     else:
#         print("Il n'existe pas de joueur avec cet identifiant")





def main():
    
    

    CreateTournament()


    



    # time.sleep(2.5)    
        

if __name__ == "__main__":
    main()
 