from datetime import datetime

class Player:
    """Player Model"""

    def __init__(self, name, first_name, birthdate, sex, rank, played_with, tournament_score=0):
        self._name = name
        self._first_name = first_name
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

    # setter method
    def set_name(self, x):
        self._name = x
        
    def set_first_name(self, x):
        self._first_name = x

        
    def set_birthdate(self, x):
        self._birthdate = x
        try:
            datetime.strptime(self.get_birthdate(), '%d-%m-%Y')
        except ValueError:
            raise ValueError("Mauvais format, le bon format est JJ-MM-AAAA")
    
        
    def set_sex(self, x):
        self._sex= x
    
    def set_rank(self, x):
        self._rank = x
        
    def set_tournament_score(self, x):
        self._tournament_score = x
        
    def set_played_with(self, x):
        self._played_with = x           

    # get method
    def get_name(self):
        return self._name
    
    def get_first_name(self):
        return self._first_name 
      
    def get_birthdate(self):
        return self._birthdate

    def get_sex(self):
        return self._sex

    def get_rank(self):
        return self._rank
    
    def get_played_with(self):
        return self._played_with     
    
    def get_tournament_score(self):
        return self._tournament_score
    
    

    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      







