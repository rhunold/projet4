# from controllers.time import get_timestamp

# from tour import Tour
# from player import Player
# from match import Match


class Tournament:
    """Tournament Model"""    
    
    def __init__(self, name, description, start_date, end_date, location, tour_number=4, time_control="", list_tours=None, list_players=None):
        self._name = name
        self._description = description
        self._start_date = start_date #get_timestamp()          
        self._end_date = end_date
        self._location = location
        self._tour_number = tour_number
        self._time_control = time_control        
        self._list_tours = list_tours
        self._list_players = list_players   
 
        # self._tournament_id = tournament_id  
        # self._active_round = active_round
        
        if list_tours is None: 
            self._list_tours = []
            # print("Il faut vérfier que ")
            
            
        if list_players is None: 
            self._list_players= []


        
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
            f'Liste des joueurs : {self._list_players}\n'

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
            f'{self._list_players})'

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
    def list_players(self):
        return self._list_players

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
    def round_number(self, x):
        self._tour_number = x
              
    @list_tours.setter
    def list_tours(self, x):
        self._list_tours = x
        
    @list_players.setter
    def list_players(self, x):
        self._list_players = x        

    # Other methods
    def add_player(self, player):
        # self._list_players= [] #indiqué en haut
        pass # append player indice too the list
  

    # def sort_players_by_rank(self):
    #     sort_players_by_rank = sorted(self.list_players, key=lambda x: x.rank, reverse=False)
    #     return sort_players_by_rank


        




        
        # print("On refait un liste vs score du round 1 (départage par classemnt si egalité)")
        # players.sort(key=lambda x: x.tournament_score, reverse=True)
        # print(players)        



  
