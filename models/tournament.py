from models.tour import Tour
from models.player import Player
from tinydb import TinyDB, Query


db = TinyDB('db.json').table('tournaments')


class Tournament:
    """Tournament Model"""
    # class_counter= 1

    def __init__(self, name="", description="", start_date_and_hour="",
                 end_date_and_hour="", place="", tour_number=4,
                 time_control="", list_players=[], list_tours=[]):
        # self._tournament_id = Tournament.class_counter
        # Tournament.class_counter += 1
        # self._tournament_id = tournament_id
        self._name = name
        self._description = description
        self._start_date_and_hour = start_date_and_hour  # get_timestamp()
        self._end_date_and_hour = end_date_and_hour
        self._place = place
        self._tour_number = tour_number
        self._time_control = time_control
        self._list_tours = list_tours
        self._list_players = list_players

    def __str__(self):
        str = (
            # f'Id du tournoi : {self._tournament_id}\n'
            f'Nom du tournoi : {self._name}\n'
            f'Description : {self._description}\n'
            f'Date de début : {self._start_date_and_hour}\n'
            f'Date de fin : {self._end_date_and_hour}\n'
            f'Lieu : {self._place}\n'
            f'Nombre de rounds : {self._tour_number}\n'
            f'Time Control : {self._time_control}\n'
            # f'Liste des joueurs : {self._list_players}\n'
            f'Liste des joueurs :'
            f'{[player for player in self._list_players]}\n'
            f'Liste des tours : {[tour for tour in self._list_tours]}\n'
            # f'Liste des tours : {self._list_tours}\n'
        )
        return str

    def __repr__(self):
        tournament = (
            f'Tournament("{self._name}",'
            # f'"{self._tournament_id}",'
            f'"{self._description}",'
            f'"{self._start_date_and_hour}",'
            f'"{self._end_date_and_hour}",'
            f'"{self._place}",'
            f'{self._tour_number},'
            f'"{self._time_control}",'
            f'"{[player for player in self._list_players]}",'
            # f'"{self._list_players}",'
            f'"{[tour for tour in self._list_tours]}")'
            # f'"{self._list_tours}")'
        )
        return tournament

    # get method
    # @property
    # def tournament_id(self):
    #     return self._tournament_id

    @property
    def name(self):
        return self._name

    @property
    def start_date_and_hour(self):
        return self._start_date_and_hour

    @property
    def end_date_and_hour(self):
        return self._end_date_and_hour

    @property
    def description(self):
        return self._description

    @property
    def place(self):
        return self._place

    @property
    def time_control(self):
        return self._time_control

    @property
    def tour_number(self):
        return self._tour_number

    @property
    def list_tours(self):
        return self._list_tours

    @property
    def list_players(self):
        return self._list_players

    # setter method
    # @tournament_id.setter
    # def tournament_id(self, x):
    #     self._tournament_id = x

    @name.setter
    def name(self, x):
        self._name = x

    @description.setter
    def description(self, x):
        self._description = x

    @place.setter
    def place(self, x):
        self._place = x

    @time_control.setter
    def time_control(self, x):
        self._time_control = x

    @start_date_and_hour.setter
    def start_date_and_hour(self, x):
        self._start_date_and_hour = x

    @end_date_and_hour.setter
    def end_date_and_hour(self, x):
        self._end_date_and_hour = x

    @tour_number.setter
    def tour_number(self, x):
        self._tour_number = x

    @list_tours.setter
    def list_tours(self, x):
        self._list_tours = x

    @list_players.setter
    def list_players(self, x):
        self._list_players = x

    # Other methods
    def serialized(self):
        serialized_tournament = {
            # "tournament_id": self.tournament_id,
            "name": self.name,
            "description": self.description,
            "start_date_and_hour": self.start_date_and_hour,
            "end_date_and_hour": self.end_date_and_hour,
            "place": self.place,
            "tour_number": self.tour_number,
            "time_control": self.time_control,
            "list_players":
                [player.serialized() for player in self.list_players],
            "list_tours": [tour.serialized() for tour in self.list_tours]
        }
        return serialized_tournament

    def unserialized(self, serialized_tournament):
        # tournament_id = serialized_tournament["_tournament_id"]
        name = serialized_tournament['name']
        description = serialized_tournament['description']
        start_date_and_hour = serialized_tournament['start_date_and_hour']
        end_date_and_hour = serialized_tournament['end_date_and_hour']
        place = serialized_tournament['place']
        tour_number = serialized_tournament['tour_number']
        time_control = serialized_tournament['time_control']
        # list_players= serialized_tournament["list_players"]
        list_players = [Player().unserialized(serialized_player)
                        for serialized_player
                        in serialized_tournament['list_players']]

        # list_players = [Player().unserialized(serialized_player)
        # for serialized_player in serialized_tournament['list_players']]
        list_tours = [Tour().unserialized(serialized_tour)
                      for serialized_tour
                      in serialized_tournament['list_tours']]
        # list_tours = serialized_tournament["list_tours"]
        tournament = Tournament(  # tournament_id,
                          name,
                          description,
                          start_date_and_hour,
                          end_date_and_hour,
                          place,
                          tour_number,
                          time_control,
                          list_players,
                          list_tours
                          )

        return tournament

    def insert(self):
        db.insert(self.serialized())
        # db.update({"tournament_id": tournament_id}, doc_ids=[tournament_id])
        # return tournament_id

    def update_start_date_and_hour(self):
        db.update({'start_date_and_hour': self.start_date_and_hour},
                  Query().name == self.name)

    def update_end_date_and_hour(self):
        db.update({'end_date_and_hour': self.end_date_and_hour},
                  Query().name == self.name)

    def update_list_players(self):
        db.update({'list_players': [
            player.serialized() for player in self.list_players]},
                  Query().name == self.name)
        print("On update la liste des joueurs")

    def update_list_tours(self):
        db.update({'list_tours': [
            tour.serialized() for tour in self.list_tours]},
                  Query().name == self.name)
        print("On update la liste des tours")
