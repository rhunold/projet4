from datetime import datetime

from tinydb import TinyDB, where, Query

json_player = 'models/players.json'
db = TinyDB(json_player)
import json


class Player:
    """Player Model"""

    def __init__(self, player_id="", name="", first_name="", birthdate="", sex="", rank=0, player_score=0):
        self._player_id = player_id
        self._name = name.capitalize()
        self._first_name = first_name.capitalize()
        self._birthdate = birthdate
        self._sex = sex
        self._rank = rank        
        self._player_score = player_score
        
        # Attribus que l'on va manipuler




    def __str__(self):
        str = (
            f'{self._first_name} {self._name}, classement : {self._rank}'
            )
        return str    
    
    def __repr__(self):
        player = (
            # f'Player("{self._player_id}",'
            # f'"{self._name}",'            
            # f'"{self._first_name}",'
            # f'"{self._birthdate}",'   
            # f'"{self._sex}",' 
            # f'{self._rank},'
            # f'{self._player_score})'
            f'Player({self._player_id}, '
            f'"{self._name}", '            
            f'"{self._first_name}", '
            f'"{self._birthdate}", '   
            f'"{self._sex}", ' 
            f'{self._rank}, '
            f'{self._player_score})'                      
        )
        
        return player

    # get method
    @property 
    def player_id(self):
        return self._player_id
        
    @property 
    def name(self):
        return self._name

    @property 
    def first_name(self):
        return self._first_name 

    @property 
    def birthdate(self):
        return self._birthdate

    @property 
    def sex(self):
        return self._sex

    @property
    def rank(self):
        return self._rank
    
    @property
    def player_score(self):
        return self._player_score   

    # setter method
    
    @player_id.setter     
    def player_id(self, x):
        self._player_id= x
        
            
    @name.setter     
    def name(self, x):
        self._name= x
        
    @first_name.setter     
    def first_name(self, x):
        self._first_name= x        

    @sex.setter     
    def sex(self, x):
        self._sex= x
    
    @rank.setter  
    def rank(self, x):
        self._rank = x
             

    @birthdate.setter    
    def birthdate(self, x):
        self._birthdate= x
        
    @player_score.setter     
    def player_score(self, x):
        self._player_score= x
        
        
        
    # others methods


    def unserialized(self, serialized_player):
        player_id = serialized_player["_player_id"]        
        name = serialized_player["_name"]
        first_name = serialized_player["_first_name"]
        birthdate = serialized_player["_birthdate"]
        sex = serialized_player["_sex"]
        rank = serialized_player["_rank"]
        player_score = serialized_player["_player_score"]

        return Player(player_id,
                      name,
                      first_name,
                      birthdate,
                      sex,
                      rank,
                      player_score
                      )  
    


    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, indent=4))
   
    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def save(self):
        serialized_player= self.toJson()
        player_id = db.insert(serialized_player)
        
        # On update l'id du tournoi dans le json
        db.update({"_player_id": player_id}, doc_ids=[player_id])
        
    def update_rank(self):
        db.update({'_rank': self.rank}, doc_ids=[self.player_id]) 

            


raphael = Player(1,"hunold","raphael","04-04-1977","Homme",1, 0)
thea = Player(2,"Hunold","Théa","14-06-2015","Femme",5, 0)
gabriel = Player(3,"Hunold","Gabriel","11-07-1978","Homme",6, 0)
aloise = Player(4,"Hunold","Aloise","31-01-1980","Femme",7, 0)
francis = Player(5,"Hunold","Francis","12-12-1943","Homme",2, 0)
flora = Player(6,"Hunold","Flora","12-08-1980","Femme",11, 0)
christine = Player(7,"Hunold","Christine","12-12-1953","Femme",10, 0)
stephane = Player(8,"Hunold","Stephane","12-12-1973","Homme",9, 0)


players = [raphael, thea, gabriel, aloise, francis, flora, christine, stephane] # liste de tous les joueurs
# players = [] 