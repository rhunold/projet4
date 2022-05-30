from controllers.time import get_timestamp

"""
En plus de la liste des correspondances, chaque instance du tour doit contenir un champ de nom.

Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 

Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin,
qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé.

Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.

round1 = Round("1", [match1, match2, match3, match4])
"""


class Round:
    """Round Model"""

    def __init__(self, name, list_matchs):
        self._name = name
        self._list_matchs = list_matchs # c'est une list avec les instances de match [match1, match2, ...]
        self._start_date = get_timestamp()
        self._end_date = ""

        # self._round_number = round_number # len de list_matchs
        # self._active_round = False     
                        
  
    def __str__(self):
        return (
            f'Round {self._name}'
            f'{[str(match) for match in self._list_matchs]}'
            )


    def __repr__(self):
        return f'{[str(match) for match in self._list_matchs]}' 
     


    # get method
    @property    
    def name(self):
        return self._name

    @property    
    def list_matchs(self):
        return self._list_matchs    

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date
    

    # setter method
    @name.setter 
    def name(self, x):
        self._name = x

    @list_matchs.setter         
    def list_matchs(self, x):
        self._list_matchs = x         

    @start_date.setter 
    def start_date(self, x):
        self._start_date = x

    @end_date.setter 
    def end_date(self, x):
        self._end_date = x 
        

    # others methods

    def next_round(self):
        pass    
  
    
    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      


