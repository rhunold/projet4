#from models.round import Round

class Tournament:
    """Tournament Model"""    
    
    def __init__(self, name, description, start_date, end_date, location, round_number, round_list, player_list, time_control):
        self._name = name
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._location = location
        self._round_number = round_number
        # self._active_round = active_round        
        self._round_list = round_list
        self._player_list = player_list      
        self._time_control = time_control      
        
    def __str__(self):
                return (
                    f'Tournoi : {self._name}\n'
                    f'Description : {self._description}\n'
                    f'Start Date : {self._start_date}\n'
                    f'End Date : {self._end_date}\n'
                    f'Location : {self._location}\n'
                    f'Number of Round : {self._round_number}\n'
                    f'Rounds List : {[str(rounds) for rounds in self._round_list]}\n'
                    f'Players List : {self._player_list}\n'
                    f'Time Control : {self._time_control}\n'
                    f'Lieu : {self._location}'
                )
    
    
    def __repr__(self):
        return f" Infos dont moi j'ai besoin pour voir le programme bien tourner comme round_number : {self._round_number}..."
    
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


# Instanciations  



