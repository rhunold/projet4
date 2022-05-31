from datetime import datetime


class Player:
    """Player Model"""

    def __init__(self, player_id, name, first_name, birthdate, sex, rank):
        self._player_id = player_id
        self._name = name.capitalize()
        self._first_name = first_name.capitalize()
        self._birthdate = birthdate
        self._sex = sex
        
        # Attribus que l'on va manipuler
        self._rank = rank
        # self._played_with = played_with # on indique la liste des joueurs avec qui il a joué durant le tournoi
        # self._tournament_score = tournament_score # Score cumulé en cours enregistrable


    def __str__(self):
        str = (
            f'{self._first_name} {self._name}'
            )
        return str    
    
    def __repr__(self):
        display_repr = (
            # f'{self._first_name} {self._name}'
            f'Player("{self._name}",'
            f'"{self._first_name}",'
            f'"{self._birthdate}",'   
            f'"{self.sex}",' 
            f'{self._rank})'
        )
        
        return display_repr

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
        self._birthdate = x 
        
        # # Vérifier format de la date de naissance      
        # try:
        #     datetime.strptime(self.birthdate, '%d-%m-%Y')
        #     print('Bon format de date')
        # except ValueError: 
        #     # raise ValueError("Mauvais format de date")
        #     self._birthdate = "Mauvaise valeur...Remettre ancienne valeur" 
            
        #     print('Mauvais format, le bon format est JJ-MM-AAAA')


    # others methods

    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      


