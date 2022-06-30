from copyreg import add_extension
from datetime import datetime
import time
import random

import json

from models.player import Player, players, raphael
from controllers.time import get_timestamp
from views.interface import CreatePlayerText, ChangePlayerRankText, LoadPlayerText

# from controllers.menu_manager import ManagePlayer

from tinydb import TinyDB, where, Query
db = TinyDB('models/players.json')


def load_player(player_id):  
    search_result = db.search(Query().fragment({'_player_id': player_id}))
    loaded_player = Player().unserialized(search_result[0])
    return loaded_player


def load_all_players(self):  
    f = open(json_player)
    all_players = json.load(f)
    print(all_players)


class CreatePlayerProcess:
    def display(self):
        user_input = CreatePlayerText().display()
        
        name = user_input[0]
        first_name = user_input[1]
        birthdate = user_input[2]
        sex = user_input[3]  
        rank = user_input[4]      
        player_score = 0
        player_id = 0
        
        player = Player(player_id, name, first_name, birthdate, sex, rank, player_score)
        
        players.append(player) # Ajout à la liste des joueurs

        player.save() 
        
        # print(load_player(111))
        
        # player.update()                     
        
        #  # Serializing
        # data = json.dumps(player, default=lambda o: o.__dict__, indent=4)
        # print(data)
        
        
        # # data = {
        # #     "player_id": 0,
        # #     "name": "Hunold",
        # #     "first_name": "Raphael",
        # #     "birthdate": "03-04-1977",
        # #     "sex": "H",
        # #     "rank": 30,
        # #     "player_score": 0
        # # }        

        # # Deserializing
        # load = json.load(data)
        # # load["_birthdate"] = datetime.datetime.strftime(load["_birthdate"], '%d-%m-%Y')
        # decoded_team = player.from_json(load)
        # print(load)               
            

    
class LoadPlayerProcess:
    def display(self):
        print(f"Voic la liste des joueurs disponibles.")
        Player().show_players()
        
        user_input = LoadPlayerText().display()  
        player_id = user_input
        loaded_player = load_player(player_id)
        print(f"Le profil de {loaded_player.first_name} a été chargé avec succés.")  
        


class ChangePlayerRankProcess:
    def display(self): 
        
        player = Player()   
        
        user_input = ChangePlayerRankText().display()
        
        # On fait les opération nécessaire
        rank = user_input
        print("Test")
        
        player.rank = rank
        
        player.update()
  
           
        



    