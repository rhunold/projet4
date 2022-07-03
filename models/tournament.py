from controllers.time import get_timestamp
from database import *

import json
# from json import JSONEncoder
from typing import List


from models.tour import Tour
from models.player import Player, players


from tinydb import TinyDB, Query
db = TinyDB('models/tournament.json')

# from models.player import Player
# from models.match import Match
# from models.tour import Tour

class Tournament:
    """Tournament Model"""  
    class_counter= 1      
    
    def __init__(self, tournament_id=0, name="", description="", start_date_and_hour="", end_date_and_hour="", place="", tour_number=4, time_control="", list_tours=None, list_players=None):
        # self._tournament_id = Tournament.class_counter
        # Tournament.class_counter += 1   
        self._tournament_id = tournament_id
        self._name = name
        self._description = description
        self._start_date_and_hour = start_date_and_hour #get_timestamp()          
        self._end_date_and_hour = end_date_and_hour
        self._place = place
        self._tour_number = tour_number
        self._time_control = time_control 
               
        if list_tours is None: 
            self._list_tours = []
        else:
            self._list_tours = List[Tour]     

        if list_players is None: 
            self._list_players= []
        else:
            self._list_players= List[Player]            
        

        
    def __str__(self):
        return (
            f'Id du tournoi : {self._tournament_id}\n'            
            f'Nom du tournoi : {self._name}\n'
            f'Description : {self._description}\n'
            f'Date de début : {self._start_date_and_hour}\n'
            f'Date de fin : {self._end_date_and_hour}\n'
            f'Lieu : {self._place}\n'
            f'Nombre de rounds : {self._tour_number}\n'
            f'Time Control : {self._time_control}\n'            
            f'Liste des tours : {[str(tour) for tour in self._list_tours]}\n'
            f'Liste des joueurs : {self._list_players}\n'

        )
    
    
    def __repr__(self):
        tournament = (
            # f'{[str(rounds) for rounds in self._list_rounds]}'
            
            f'Tournament("{self._tournament_id}",'
            f'"{self._name}",'            
            f'"{self._description}",'
            f'"{self._start_date_and_hour}",'
            f'"{self._end_date_and_hour}",'
            f'"{self._place}",'
            f'{self._tour_number},'
            f'{self._time_control},'            
            f'{[str(tour) for tour in self._list_tours]},'
            f'{self._list_players})'

        )        
        
        return tournament



   # get method
    @property
    def tournament_id(self):
        return self._tournament_id   
   
    @property
    def name(self):
        return self._name

    @property    
    def start_date_and_hour(self):
        return self._start_date_and_hour  
        
    @property
    def end_date_and_hour(self):
        return self._end_date_and_hour      

    @property
    def description(self):
        return self._description
    
    @property
    def place(self):
        return self._place
    
    @property
    def time_control(self):
        return self._time_control

    @property     
    def tour_number(self):
        return self._tour_number
    
    @property     
    def list_tours(self):
        return self._list_tours  

    @property
    def list_players(self):
        return self._list_players

    # setter method
    @tournament_id.setter
    def tournament_id(self, x):
        self._tournament_id = x 
           
    @name.setter
    def name(self, x):
        self._name = x
    
    @description.setter    
    def description(self, x):
        self._description = x
        
    @place.setter    
    def place(self, x):
        self._place = x
        
    @time_control.setter    
    def time_control(self, x):
        self._time_control = x               

    @start_date_and_hour.setter
    def start_date_and_hour(self, x):
        self._start_date_and_hour = x  

    @end_date_and_hour.setter
    def end_date_and_hour(self, x):
        self._end_date_and_hour = x        

    @tour_number.setter
    def tour_number(self, x):
        self._tour_number = x
              
    @list_tours.setter
    def list_tours(self, x):
        self._list_tours = x
        
    @list_players.setter
    def list_players(self, x):
        self._list_players = x        

    # Other methods
    


    
    def add_player(self, player_id):
        # On s'assure que la liste des joueurs comprend un joueur avec l'id demandé
        
        # si on trouve l'id, on ajoute le joueur en tant que participant
        if any(player.player_id == player_id for player in players):
            for player in players:
                if player.player_id == player_id :
                    
                    self._list_players.append(player) # on ajoute le joueur dans les participants
                    players.remove(player) # On enlève le joueur des joueurs disponibles
            return None 


        else:
            print(f"Il n'existe pas de joueur avec l'identifiant {player_id} ou il a déjà été sélectionné")


    # def serialized(self):
        
    #     serialized_tournament = {
    #         "tournament_id": self.tournament_id,            
    #         "name": self.name,
    #         "description": self.description,            
    #         "start_date_and_hour": self.start_date_and_hour,
    #         "end_date_and_hour": self.end_date_and_hour,  
    #         "place": self.place,                      
    #         "time_control": self.time_control,
    #         "tour_number": self.tour_number,
    #         "list_tours": [tour.serialized() for tour in self.list_tours],
    #         "list_players": [player.serialized() for player in self.list_players]
    #     }
    #     return serialized_tournament



    def unserialized(self, serialized_tournament):
        tournament_id = serialized_tournament["_tournament_id"]        
        name = serialized_tournament['_name']
        description = serialized_tournament['_description']
        start_date_and_hour = serialized_tournament['_start_date_and_hour']
        end_date_and_hour = serialized_tournament['_end_date_and_hour']
        place = serialized_tournament['_place']   
        time_control = serialized_tournament['_time_control']              
        tour_number = serialized_tournament['_tour_number']
        list_tours = serialized_tournament["_list_tours"]
        list_players= serialized_tournament["_list_players"]
        
        tournament = Tournament(tournament_id,
                          name,
                          description,
                          start_date_and_hour,                          
                          end_date_and_hour,
                          place,
                          time_control,                          
                          tour_number,
                          list_tours,                          
                          list_players
                          )

        return tournament
        
        
    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, indent=4))

    
    @classmethod
    def from_json(cls, data):
        print("test dans le from_jason du model tournament")
        list_players = list(map(Player().from_json, data["_list_players"]))
        list_tours = list(map(Tour().from_json, data["_list_tours"]))        
        return cls(list_players, list_tours)


    # def save(self):
    #     serialized_tournament = self.toJson()
    #     tournament_id = db.insert(serialized_tournament)
        
    #     # On update l'id du tournoi dans le json
    #     db.update({"_tournament_id": tournament_id}, doc_ids=[tournament_id])
        

          
    # def update(self):
    #     serialized_tournament = self.toJson()   
    #     # tournament_id = db.search(Query().fragment({'_tournament_id': self.tournament_id}))
             
    #     db.update({"_tournament_id": tournament_id}, doc_ids=[tournament_id])  
        
        
        # Tournament= Query() 
        # tournament_id = self.tournament_id          
        
        # serialized_tournament = db.search(Tournament._tournament_id == tournament_id)
        # serialized_tournament = serialized_tournament[0]
        
        # print(serialized_tournament)        
        
        # unserialized_tournament = self.load()
        
        # print(unserialized_tournament)   
        # serialized_tournament = self.toJson()
 

        # db.update(serialized_tournament, doc_ids=[tournament_id])   
        

        
        
        
        
    def load(self):
        return json.load(json.loads(self, default=lambda o: o.__dict__, indent=4))   