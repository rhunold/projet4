from controllers.time import get_timestamp

# from models.match import Match

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

    def __init__(self, name, list_matchs):
        self._name = "Round " + str(name)
        self._list_matchs = list_matchs # c'est une list avec les instances de match [match1, match2, ...]
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



    # def create_round(self, tour_number):  
    #     pass
    #     current_round = 0

    #     if len(self._list_tours) == 0:
    #         print("On récupére la liste des joueurs et tri vs classement en 2 part, puis apparareillement") 
        
    #     while len(self._list_tours) >= 1:
    #         print("Round 2 et plus") 
    #         pass         
        

    # def run_rounds(self, round_number):

    #     if round_number == 1:
    #         # on range les joueurs par classement et on divise en 2 groupes (plus forts/moins fort. 
    #         # Ensuite on prend le 1 et le 5, le 2 et le 6, le 3 et le 7, le 4 et le 8ème joueur)        
    #         print("Round 1")
    #     else :
    #         # Algo suisse
    #         for rounds in self.list_rounds:        
    #             print("Rounds 2, 3 ...")

        



  
    
    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      

