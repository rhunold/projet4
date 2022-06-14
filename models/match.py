import random

from controllers.time import get_timestamp



"""
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant deux éléments : une référence à une instance de joueur et un score.
Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour. 

"""

# format du tuple
# player_pair = ([], []) => player_pair = (player1, player2)
# scores = ([player1, score_player1]
# , [player2, score_player2])
# output = ([Player("Hunold", "Raphael", "03/04/1977", "Homme", 1), 0], [Player("Hunold", "Théa", "14/06/2015", "Femme", , 3), 1])


class Match:
    """Match Model"""

    def __init__(self, player1_id=0, player2_id=0, player1_score=0, player2_score=0):
        self._match_pair = ([player1_id, player1_score], [player2_id, player2_score])
        self._player1_id = player1_id
        self._player2_id = player2_id
        self._player1_score = player1_score
        self._player2_score = player2_score
        
        
        # self._match_id = 
        # self._start_date = get_timestamp()
        self._end_date = ""        
        # self._winner = ""                            

    def __str__(self):
        # return f'{self.player1_id} : { self.player1_score}  vs {self.player2_id} : { self._player2_score}'
        return f'{self._match_pair}'


    def __repr__(self):
        match = (
            # f'{self._player1} vs {self._player2}'
            
            f'Match("{self._player1_id}",'
            f'{self._player1_score},'
            f'"{self._player2_id}",'
            f'{self._player2_score})'        
        )
        return match    

    # get method
    @property
    def player1_id(self):
        return self._player1_id

    @property
    def player2_id(self):
        return self._player2_id
    
    @property
    def player1_score(self):
        return self._player1_score
    
    @property
    def player2_score(self):
        return self._player2_score
    
    

    # setter method
    @player1_id.setter          
    def player1_id(self, x):
        self._player1_id = x

    @player2_id.setter 
    def player2_id(self, x):
        self._player2_id = x
        
    @player1_score.setter 
    def player1_score(self, x):
        self._player1_score = x
        # On ajoute les points du match à ceux du tournoi
        
    @player2_score.setter 
    def player2_score(self, x):
        self._player2_score = x





    def play_match(self):
        scores = [0, 1, 0.5]
        player2_score = 0 #init
                
        # Mode random score
        player1_score = random.choice(scores) 
        
        # Mode saisie manuelle des scores
        # player1_score = float(input("Quel est le score du joueur 1 (0, 1 ou 0.5) ?"))
        
        if player1_score == 0:        
            self._player2_score = 1

        elif player1_score == 1: 
            self._player1_score = 1
          
        elif player1_score == 0.5:
            self._player2_score = 0.5
            self._player1_score = 0.5
                   
       
        else:
            print("Try again")  
        
        # Permet de changer le score...sinon ça veut pas.
        self._match_pair = ([self._player1_id, self._player1_score], [self._player2_id, self._player2_score])     
        


    # def add_score_to_participant(self):
    #     pass
    



    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      



