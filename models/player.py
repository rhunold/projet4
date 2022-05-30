from datetime import datetime
from wsgiref import validate

class Player:
    """Player Model"""

    def __init__(self, name, first_name, birthdate, sex, rank, played_with, tournament_score=0):
        self._name = name.capitalize()
        self._first_name = first_name.capitalize()
        self._birthdate = birthdate
        self._sex = sex
        
        # Attribus que l'on va manipuler
        self._rank = rank
        self._played_with = played_with # on indique la liste des joueurs avec qui il a joué durant le tournoi
        self._tournament_score = tournament_score # Score cumulé en cours enregistrable

    def __str__(self):
        return f"{self._first_name} {self._name} a {self._tournament_score} points dans le tournoi."
    
    def __str__(self):
                str = (
                    f'{self._first_name} {self._name}\n'
                    f'Score du tournoi : {self._tournament_score}\n'
                    f'Classement : {self._rank}\n'
                    f'Liste Joueurs avec qui déjà joué : {self._played_with}\n'
                    f'Naissance : {self._birthdate}\n'                    
                )
                return str    
    
    def __repr__(self):
        return f"{self._first_name} {self._name}"

    # get method
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
    def played_with(self):
        return self._played_with     

    @property
    def tournament_score(self):
        return self._tournament_score

    # setter method
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
    
    @tournament_score.setter     
    def tournament_score(self, x):
        self._tournament_score = x
    
    @played_with.setter   
    def played_with(self, x):
        self._played_with = x           

    @birthdate.setter    
    def birthdate(self, x):
        self._birthdate = x 
        
        # Vérifier format de la date de naissance      
        try:
            datetime.strptime(self.birthdate, '%d-%m-%Y')
            print('Bon format de date')
        except ValueError: 
            # raise ValueError("Mauvais format de date")
            self._birthdate = "Mauvaise valeur...Remettre ancienne valeur" 
            
            print('Mauvais format, le bon format est JJ-MM-AAAA')


    # others methods

    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      







