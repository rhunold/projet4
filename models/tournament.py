from controllers.time import get_timestamp


class Tournament:
    """Tournament Model"""    
    
    def __init__(self, name, description, start_date, end_date, location, round_number, list_rounds, list_players, time_control):
        self._name = name
        self._description = description
        self._start_date = get_timestamp()
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
        return (f'{[str(rounds) for rounds in self._list_rounds]}')
    
    # setter method
    def set_name(self, x):
        self._name = x
        
    def set_description(self, x):
        self._description = x        
        
    # get method
    def get_name(self):
        return self._name

    def add_participant():
        pass # append player indice too the list
  
    def create_round(self, round_number):
        pass


