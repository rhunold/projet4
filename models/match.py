# import random
from views.interface import MatchWinnerText


class Match:
    """Match Model"""

    def __init__(self, player1_id=0, player2_id=0,
                 player1_score=0, player2_score=0):
        self._match_pair = ([player1_id, player1_score],
                            [player2_id, player2_score])
        self._player1_id = player1_id
        self._player2_id = player2_id
        self._player1_score = player1_score
        self._player2_score = player2_score

    def __str__(self):
        return (
            f'Match : {self.player1_id} ({self.player1_score})'
            f' vs {self.player2_id} ({ self._player2_score})'
            )

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

    @player2_score.setter
    def player2_score(self, x):
        self._player2_score = x

    def play_match(self):
        # Mode random score
        # choice = ["0", "1", "2", "3"]
        # winner = random.choice(choice)

        # Mode saisie manuelle des scores
        winner = MatchWinnerText().display(self._player1_id, self._player2_id)

        if winner == "0":
            self._player1_score = 1

        elif winner == "1":
            self._player2_score = 1

        elif winner == "2":
            self._player2_score = 0.5
            self._player1_score = 0.5

        elif winner == "3":
            stop = False
            return stop

        # On écrase la version vierge précédente
        self._match_pair = ([self._player1_id, self._player1_score],
                            [self._player2_id, self._player2_score])

    # serialization

    def serialized(self):
        serialized_match = {
            "player1_id": self.player1_id,
            "player1_score": self.player1_score,
            "player2_id": self.player2_id,
            "player2_score": self.player2_score
        }
        return serialized_match

    def unserialized(self, serialized_match):
        # match_id = serialized_match['Match ID']
        player1_id = serialized_match["player1_id"]
        player2_id = serialized_match["player2_id"]
        player1_score = serialized_match["player1_score"]
        player2_score = serialized_match["player2_score"]
        return Match(player1_id,
                     player2_id,
                     player1_score,
                     player2_score)
