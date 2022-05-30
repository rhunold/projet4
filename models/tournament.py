from controllers.time import get_timestamp


class Tournament:
    """Tournament Model"""    
    
    def __init__(self, name, description, end_date, location, round_number, list_rounds, list_players, time_control):
        self._name = name
        self._description = description
        self._end_date = "Pas encore terminé"
        self._location = location
        self._round_number = round_number
        # self._active_round = active_round        
        self._list_rounds = list_rounds
        self._list_players = list_players   
        self._time_control = time_control  
        self._start_date = get_timestamp()            
        
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

    def set_start_date(self, x):
        self._start_date = x  

    def set_end_date(self, x):
        self._end_date = x        

    def set_round_number(self, x):
        self._round_number = x

    # get method
    def get_name(self):
        return self._name
    
    def get_start_date(self):
        return self._start_date      
    
    def get_end_date(self):
        return self._end_date      

    def get_description(self):
        return self._description
     
    def get_round_number(self):
        return self._round_number


    def add_participant():
        pass # append player indice too the list
  

    def run_rounds(self, round_number):

        if round_number == 1:
            # on range les joueurs par classement et on divise en 2 groupes (plus forts/moins fort. 
            # Ensuite on prend le 1 et le 5, le 2 et le 6, le 3 et le 7, le 4 et le 8ème joueur)        
            print("Round 1")
        else :
            # Algo suisse
            for rounds in self.list_rounds:        
                print("Rounds 2, 3 ...")

        

