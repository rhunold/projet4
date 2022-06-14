from controllers.time import get_timestamp
from database import *

# from models.player import Player
# from models.match import Match
# from models.tour import Tour

class Tournament:
    """Tournament Model"""    
    
    def __init__(self, name="", description="", start_date="", end_date="", location="", tour_number=4, time_control="", list_tours=None, list_participants=None):
        self._name = name
        self._description = description
        self._start_date = start_date #get_timestamp()          
        self._end_date = end_date
        self._location = location
        self._tour_number = tour_number
        self._time_control = time_control 
               
        if list_tours is None: 
            self._list_tours = []
            # print("Il faut vérfier que ")
        else:
            self._list_tours = list_tours

        if list_participants is None: 
            self._list_participants= []
        else:
            self._list_participants= list_participants            


        # self._tournament_id = tournament_id  
        

        
    def __str__(self):
        return (
            f'Tournoi : {self._name}\n'
            f'Description : {self._description}\n'
            f'Date de début : {self._start_date}\n'
            f'Date de fin : {self._end_date}\n'
            f'Lieu : {self._location}\n'
            f'Nombre de rounds : {self._tour_number}\n'
            f'Time Control : {self._time_control}\n'            
            f'Liste des rounds : {[str(tour) for tour in self._list_tours]}\n'
            f'Liste des participants : {self._list_participants}\n'

        )
    
    
    def __repr__(self):
        tournament = (
            # f'{[str(rounds) for rounds in self._list_rounds]}'
            
            f'Tournament("{self._name}",'
            f'"{self._description}",'
            f'"{self._start_date}",'
            f'"{self._end_date}",'
            f'"{self._location}",'
            f'{self._tour_number},'
            f'{self._time_control},'            
            f'{[str(tour) for tour in self._list_tours]},'
            f'{self._list_participants})'

        )        
        
        return tournament

   # get method
    @property
    def name(self):
        return self._name

    @property    
    def start_date(self):
        return self._start_date  
        
    @property
    def end_date(self):
        return self._end_date      

    @property
    def description(self):
        return self._description

    @property     
    def tour_number(self):
        return self._tour_number
    
    @property     
    def list_tours(self):
        return self._list_tours  

    @property
    def list_participants(self):
        return self._list_participants

    # setter method
    @name.setter
    def name(self, x):
        self._name = x
    
    @description.setter    
    def description(self, x):
        self._description = x

    @start_date.setter
    def start_date(self, x):
        self._start_date = x  

    @end_date.setter
    def end_date(self, x):
        self._end_date = x        

    @tour_number.setter
    def tour_number(self, x):
        self._tour_number = x
              
    @list_tours.setter
    def list_tours(self, x):
        self._list_tours = x
        
    @list_participants.setter
    def list_participants(self, x):
        self._list_participants = x        

    # Other methods
    


    
    def add_player(self, player_id):
        # On s'assure que la liste des joueurs comprend un joueur avec l'id demandé
        
        # si match, on ajoute le joueur en tant que participant
        if any(player.player_id == player_id for player in list_players):
            for player in list_players:
                if player.player_id == player_id :
                    
                    self._list_participants.append(player) # on ajoute le joueur dans les participants
                    list_players.remove(player) # On enlève le joueur des joueurs disponibles
            return None 


        else:
            print(f"Il n'existe pas de joueur avec l'identifiant {player_id} ou il a déjà été sélectionné")



    # def sort_players_by_rank(self):
    #     sort_players_by_rank = sorted(self.list_players, key=lambda x: x.rank, reverse=False)
    #     return sort_players_by_rank


        


  
