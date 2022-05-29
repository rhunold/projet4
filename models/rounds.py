

"""
En plus de la liste des correspondances, chaque instance du tour doit contenir un champ de nom.

Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 

Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin,
qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé.

Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.
"""


class Round:
    """Round Model"""

    def __init__(self, name, list_matchs):
        self._name = name
        self._list_matchs = list_matchs # c'est une list avec les instances de match [match1, match2, ...]
        self._start_date = "" # get_timestamp()
        self._end_date = ""

        # self._round_number = round_number # len de list_matchs
        # self._active_round = False     
                           

    def __str__(self):
        return f"Rounds : {self._name} "    

    def __repr__(self):
        # return f"Liste des Matchs du Round : "
        return (self.list_matchs)


    # setter method
    def set_name(self, x):
        self._name = x
        
    def set_list_matchs(self, x):
        self._list_matchs = x         

    def set_start_date(self, x):
        self._start_date = x
        
    def set_end_date(self, x):
        self._end_date = x 

    # get method
    def get_name(self):
        return self._name
    
    def get_list_matchs(self):
        return self._list_matchs    
  
    def get_start_date(self):
        return self._start_date
    
    def get_end_date(self):
        return self._end_date

    def next_round(self):
        pass    
  
    
    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      


