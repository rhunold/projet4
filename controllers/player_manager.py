from copyreg import add_extension
from datetime import datetime
from multiprocessing.spawn import old_main_modules
import time
import random

import json

from models.player import Player, players
from controllers.time import get_timestamp
from views.interface import CreatePlayerText, ChangePlayerRankText, LoadPlayerText

from tinydb import TinyDB, where, Query

json_player = 'models/players.json'
db = TinyDB(json_player)


def load_player(player_id):  
    search_result = db.search(Query().fragment({'_player_id': player_id}))
    
    if not search_result:
        print("Pas d'identifiant existant en base de donnée.")
        LoadPlayerProcess().display()
            
        # load_player(player_id)
    else:
        player = Player().unserialized(search_result[0])
        
    
    # Probleme ici quand l'id n'existe pas dans la recherche.

        return player

def display_players(): 
    players_db = db.all()
    players = []     
    for player in players_db:
        player = Player().unserialized(player)
        players.append(player)
        print(f"{player.player_id} {player.first_name} {player.name} Classement : {player.rank}")
    return players




class CreatePlayerProcess:
    def display(self):
        player = CreatePlayerText().display()
        
        
        name = player[0]
        first_name = player[1]
        birthdate = player[2]
        sex = player[3]  
        rank = player[4]      
        player_score = 0
        player_id = 0
        
        player = Player(player_id, name, first_name, birthdate, sex, rank, player_score)
        
        # players.append(player) # Ajout à la liste des joueurs
        
        print(f"Le joueur {player.first_name} a écé crée.")

        player.save() 
        
    
class LoadPlayerProcess:
    def display(self):
        
        while True:    
            display_players()
            try: 
                # print("test a")
                player_id = LoadPlayerText().display()
                print(player_id)
                player = load_player(player_id)
                
            except ValueError:
                print("test c")
            else:
                return player
                    
                      
        # players = sorted(players, key=lambda x: x._player_id, reverse=True)
        


class ChangePlayerRankProcess:
    def display(self, player): 
        
        # On demande le nouveau classement
        rank = ChangePlayerRankText().display()
        
        player.rank = rank
        player.update_rank()
        print(f"Le classement de {player.first_name} {player.name} a été mis à jour.")
        # time.sleep(1.5)     
        
        # Player().update_rank() 
         

class PlayerReportProcess:
    def display_by_name(self): 

        players_db = db.all()
        players = []
        
        for player in players_db:
            player = Player().unserialized(player)
            players.append(player)
            print(f"{player.player_id} {player.first_name} {player.name} Classement : {player.rank}")     
 
        players = sorted(players, key=lambda x: x._first_name, reverse=True)        
        players = sorted(players, key=lambda x: x._name, reverse=True)            
        
  
   
        # for player in players:
        #     return print(f" {player.player_id} {player.first_name} {player.name} Classement : {player.rank}")
            

        
    def display_by_rank(self): 
        pass

        # players_db = db.all()
        # players = []
        
        # for player in players_db:
        #     player = Player().unserialized(player)
        #     players.append(player)
            
        # players_by_rank = sorted(players, key=lambda x: x._rank, reverse=False)
                     
            
            
        # for player in players_by_rank:
        #     print(f" {player.player_id} {player.first_name} {player.name} Classement : {player.rank}")
    

           
        



    