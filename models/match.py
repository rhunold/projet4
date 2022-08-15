# import random
from views.interface import MatchWinnerText


class Match:
    """Match Model"""

    def __init__(self, player1_name=0, player2_name=0,
                 player1_score=0, player2_score=0):
        self._match_pair = ([player1_name, player1_score],
                            [player2_name, player2_score])
        self._player1_name = player1_name
        self._player2_name = player2_name
        self._player1_score = player1_score
        self._player2_score = player2_score

    def __str__(self):
        return (
            f'{self.player1_name} ({self.player1_score})'
            f' - {self.player2_name} ({ self._player2_score})'
            )

    def __repr__(self):
        match = (
            # f'{self._player1} vs {self._player2}'
            f'Match("{self._player1_name}",'
            f'{self._player1_score},'
            f'"{self._player2_name}",'
            f'{self._player2_score})'
        )
        return match

    # get method
    @property
    def player1_name(self):
        return self._player1_name

    @property
    def player2_name(self):
        return self._player2_name

    @property
    def player1_score(self):
        return self._player1_score

    @property
    def player2_score(self):
        return self._player2_score

    # setter method
    @player1_name.setter
    def player1_name(self, x):
        self._player1_name = x

    @player2_name.setter
    def player2_name(self, x):
        self._player2_name = x

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
        winner = MatchWinnerText().display(self._player1_name,
                                           self._player2_name)

        if winner == "0":
            self._player1_score = 1

        elif winner == "1":
            self._player2_score = 1

        elif winner == "2":
            self._player2_score = 0.5
            self._player1_score = 0.5

        # Exit the match and tournament
        elif winner == "3":
            return False

        # On écrase la version vierge précédente
        self._match_pair = ([self._player1_name, self._player1_score],
                            [self._player2_name, self._player2_score])

    # serialization

    def serialized(self):
        serialized_match = {
            "player1_name": self.player1_name,
            "player1_score": self.player1_score,
            "player2_name": self.player2_name,
            "player2_score": self.player2_score
        }
        return serialized_match

    def unserialized(self, serialized_match):
        # match_name = serialized_match['Match ID']
        player1_name = serialized_match["player1_name"]
        player2_name = serialized_match["player2_name"]
        player1_score = serialized_match["player1_score"]
        player2_score = serialized_match["player2_score"]
        return Match(player1_name,
                     player2_name,
                     player1_score,
                     player2_score)
