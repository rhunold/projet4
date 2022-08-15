from tinydb import TinyDB, Query


db = TinyDB('db.json').table('players')


class Player:
    """Player Model"""
    def __init__(self,  name="", first_name="",
                 birthdate="", sex="", rank=0, player_score=0):
        self._name = name
        self._first_name = first_name.capitalize()
        self._birthdate = birthdate
        self._sex = sex
        self._rank = rank
        self._player_score = player_score

    def __str__(self):
        str = (
            f'{self._first_name} {self._name},'
            f'classement : {self._rank}, score : {self._player_score}'
            )
        return str

    def __repr__(self):
        player = (
            f'Player('
            f'"{self._name}",'
            f'"{self._first_name}",'
            f'"{self._birthdate}",'
            f'"{self._sex}",'
            f'{self._rank},'
            f'{self._player_score})'
        )
        return player

    @property
    def name(self):
        return self._name

    @property
    def first_name(self):
        return self._first_name

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def sex(self):
        return self._sex

    @property
    def rank(self):
        return self._rank

    @property
    def player_score(self):
        return self._player_score

    @name.setter
    def name(self, x):
        self._name = x

    @first_name.setter
    def first_name(self, x):
        self._first_name = x

    @sex.setter
    def sex(self, x):
        self._sex = x

    @rank.setter
    def rank(self, x):
        self._rank = x

    @birthdate.setter
    def birthdate(self, x):
        self._birthdate = x

    @player_score.setter
    def player_score(self, x):
        self._player_score = x

    # others methods

    def serialized(self):
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "birthdate": self.birthdate,
            "sex": self.sex,
            "rank": self.rank,
            "player_score": self.player_score
        }
        return serialized_player

    def unserialized(self, serialized_player):
        name = serialized_player["name"]
        first_name = serialized_player["first_name"]
        birthdate = serialized_player["birthdate"]
        sex = serialized_player["sex"]
        rank = serialized_player["rank"]
        player_score = serialized_player["player_score"]

        return Player(name, first_name, birthdate, sex, rank, player_score)

    def insert(self):
        db.insert(self.serialized())

    def update_rank(self):
        db.update({'rank': self.rank}, Query().name == self.name)
