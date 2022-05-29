class Round:
    def __init__(self, matchs):
        
       for player_name, player_score in matchs.items():  # <== note "items" needed here
           setattr(self, player_name, player_score)

matchs = {'score_player1' : 0, 'score_player2' : 1}

round1 = Round(matchs)
print(round1.score_player1)  # 0
print(round1.score_player2)  # 1