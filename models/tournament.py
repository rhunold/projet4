from controllers.time import get_timestamp



class Tournament:
    """Tournament Model"""    
    
    def __init__(self, name, description, start_date, end_date, location, round_number, list_rounds, list_players, time_control):
        self._name = name
        self._description = description
        self._start_date = start_date #get_timestamp()          
        self._end_date = end_date
        self._location = location
        self._round_number = round_number
        # self._active_round = active_round        
        self._list_rounds = list_rounds
        self._list_players = list_players   
        self._time_control = time_control  
          
        
    def __str__(self):
        return (
            f'Tournoi : {self._name}\n'
            f'Description : {self._description}\n'
            f'Start Date : {self._start_date}\n'
            f'End Date : {self._end_date}\n'
            f'Location : {self._location}\n'
            f'Number of Round : {self._round_number}\n'
            f'Rounds List : {[str(rounds) for rounds in self._list_rounds]}\n'
            f'Players List : {self._list_players}\n'
            f'Time Control : {self._time_control}\n'
            f'Lieu : {self._location}\n'
        )
    
    
    def __repr__(self):
        return (
            # f'{[str(rounds) for rounds in self._list_rounds]}'
            
            f'Tournament("{self._name}",'
            f'"{self._description}",'
            f'"{self._start_date}",'
            f'"{self._end_date}",'
            f'"{self._location}",'
            f'{self._round_number},'
            f'{[str(rounds) for rounds in self._list_rounds]},'
            f'{self._list_players},'
            f'{self._time_control})'
        )        
        
        return (f'{[str(rounds) for rounds in self._list_rounds]}')

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
    def round_number(self):
        return self._round_number


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

    @round_number.setter
    def round_number(self, x):
        self._round_number = x

 

    # Other methods
    def add_participant():
        pass # append player indice too the list
  
  
    def create_round(self, round_number):  
        pass
        

    # def run_rounds(self, round_number):

    #     if round_number == 1:
    #         # on range les joueurs par classement et on divise en 2 groupes (plus forts/moins fort. 
    #         # Ensuite on prend le 1 et le 5, le 2 et le 6, le 3 et le 7, le 4 et le 8ème joueur)        
    #         print("Round 1")
    #     else :
    #         # Algo suisse
    #         for rounds in self.list_rounds:        
    #             print("Rounds 2, 3 ...")

        

