from controllers.time import get_timestamp

from models.match import Match

# from models.tournament import Tournament
# from models.player import Player


"""
En plus de la liste des correspondances, chaque instance du tour doit contenir un champ de nom.

Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. 

Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin,
qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé.

Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.

tour1 = Tour("1", [match1, match2, match3, match4])

tour1 = Tour("1", [Match(raphael, thea), Match(gabriel, francis)])
"""


class Tour():
    """Round Model"""

    def __init__(self, name, list_matchs=None):
        self._name = "Round " + str(name)
        if list_matchs is None: 
            self._list_matchs= []
        else:
            self._list_matchs= list_matchs  
        
        self._start_date_and_hour = get_timestamp()
        self._end_date_and_hour = "0"

       
        
        # self._tour_id = 0
        # self._round_number = len(list_matchs)
        # self._active_round = False 
            
                        
  
    def __str__(self):
        return (
            f'{self._name},'
            f'{[str(match) for match in self._list_matchs]},'
            f'{self._start_date_and_hour},'
            f'{self._end_date_and_hour}'              

            # f'Roundssssss("{self._name}",'

            # f'{[str(match) for match in self._list_matchs]},'
            # f'"{self._start_date_and_hour}",'
            # f'"{self._end_date_and_hour}")'  
                        
            )


    def __repr__(self):
        tour = (
            # f'({self._name}, {[str(match) for match in self._list_matchs]})'
            
            f'Round ("{self._name}",'

            f'{[str(match) for match in self._list_matchs]},'
            f'"{self._start_date_and_hour}",'
            f'"{self._end_date_and_hour}")'                
        )
        return tour 

    # get method
    @property    
    def name(self):
        return self._name

    @property    
    def list_matchs(self):
        return self._list_matchs    

    @property
    def start_date_and_hour(self):
        return self._start_date_and_hour

    @property
    def end_date_and_hour(self):
        return self._end_date_and_hour
    

    # setter method
    @name.setter 
    def name(self, x):
        self._name = x

    @list_matchs.setter         
    def list_matchs(self, x):
        self._list_matchs = x         

    @start_date_and_hour.setter 
    def start_date_and_hour(self, x):
        self._start_date_and_hour = x

    @end_date_and_hour.setter 
    def end_date_and_hour(self, x):
        self._end_date = x 
        

    # others methods


    # def create_matchs(self):
    #     matchs = []
    #     for i in self.list_matchs:
    #         matchs.append(Match(i))
    #     return matchs   

    # def mark_as_complete(self):
    #     # self.end_date = get_timestamp()
    #     print(f"{self.end_date} : {self.name} terminé.")
    #     print("Entrer les résultats des matchs:")
    #     for match in self.matchs:
    #         match.end_match()




  
    
    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      

