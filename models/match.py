


"""
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,

chacune contenant deux éléments : une référence à une instance de joueur et un score.

Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour. 

"""


# player_pair = ([player1, score_player1], [player2, score_player2])
# player_pair = ([Player("Hunold", "Raphael", "03/04/1977", "Homme", 1, [1, 3, 6], 5), 0], [Player("Hunold", "Théa", "14/06/2015", "Femme", 2, [2, 4, 5], 3), 1])

class Match:
    """Match Model"""

    def __init__(self, player_pair):
        self._player1 = player_pair[0]
        self._player2 = player_pair[1]
        self._start_date = ""
        self._end_date = ""
        self._score_player1 = 0
        self._score_player2 = 0
        self._winner = ""                            

    def __str__(self):
        return f"Match : {self._player1} vs {self._player2}"


    def __repr__(self):
        return ([self._player1, self._score_player1], [self._player2, self._score_player2])

    # setter method
        
    def set_player1(self, x):
        self._player1 = x
  
    def set_player2(self, x):
        self._player2 = x
        
    def set_winner(self, x):
        self._winner = x        
          

    # get method
    
    def get_player1(self):
        return self._player1
    
    def get_player2(self):
        return self._player2
    
    def get_winner(self):
        return self._winner


    def play_match():
        # On demande qui a gagé pour pouvoir assigner les points et désigner le vainqueur
        pass
    
    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      




# Instanciations  


score_player1 = 0
score_player2 = 1

