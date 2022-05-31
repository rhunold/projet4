from controllers.time import get_timestamp
import random



"""
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant deux éléments : une référence à une instance de joueur et un score.
Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour. 

"""

# format du tuple
# player_pair = ([], []) => player_pair = (player1, player2)
# scores = ([player1, score_player1], [player2, score_player2])
# output = ([Player("Hunold", "Raphael", "03/04/1977", "Homme", 1), 0], [Player("Hunold", "Théa", "14/06/2015", "Femme", , 3), 1])




class Match:
    """Match Model"""

    def __init__(self, player_pair):
        self._player1 = player_pair[0]
        self._player2 = player_pair[1]
        self._score_player1 = 0
        self._score_player2 = 0
        # self._start_date = get_timestamp()
        # self._end_date = ""        
        # self._winner = ""                            

    def __str__(self):
        return f'{self._player1} : { self._score_player1}  vs {self._player2} : { self._score_player2}'


    def __repr__(self):
        display_repr = (
            # f'{self._player1} vs {self._player2}'
            
            f'Match("{self._player1}",'
            f'{self._score_player1},'
            f'"{self._player2}",'
            f'{self._score_player2})'        
        )
        return display_repr    

    # get method
    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2
    
    @property
    def score_player1(self):
        return self._score_player1
    
    @property
    def score_player2(self):
        return self._score_player2
    
    

    # @property    
    # def winner(self):
    #     return self._winner

    # @property    
    # def start_date(self):
    #     return self._start_date
    # @property
    # def end_date(self):
    #     return self._end_date

    # setter method
    @player1.setter          
    def player1(self, x):
        self._player1 = x

    @player2.setter 
    def player2(self, x):
        self._player2 = x
        
    @score_player1.setter 
    def score_player1(self, x):
        self._score_player1 = x
        
    @score_player2.setter 
    def score_player2(self, x):
        self._score_player2 = x   

    # @winner.setter     
    # def winner(self, x):
    #     self._winner = x
    #     self._end_date = get_timestamp()

    # @end_date.setter 
    # def end_date(self, x):
    #     self._end_date = x   

    # def random_score():  
    #     scores = [0, 1, 0.5]        
    #     score = random.choices([score for score in scores], k = 1) 
    #     return score
    
    def play_match(self):
        scores = [0, 1, 0.5]     
        self._score_player1 = random.choice(scores) 
        self._score_player2 = random.choice(scores) 

        if self._score_player1 == 1:
            self.score_player1 += 1
        elif self._score_player2 == 1:
            self.score_player2 += 1
        else:
            self.score_player1 += 0.5
            self.score_player2 += 0.5

        # self.player1.tournament_score += self.score_player1
        # self.player2.tournament_score += self.score_player2        


    # def player_pair():
    #     player_pair = (random_player(), random_player())
    #     # player_pair = (top_player(), bottom_player())    
    #     return player_pair



    # serialization
    def serialized(self):
        pass  
    
    def unserialized(self):
        pass      






