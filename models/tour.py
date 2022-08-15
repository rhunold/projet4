from models.match import Match


class Tour():
    """Tour Model"""
    # counter = 1

    def __init__(self, tour_id=0,
                 start_date_and_hour="", end_date_and_hour="", list_matchs=[]):
        self._tour_id = tour_id
        # self._tour_id = Tour.counter
        # Tour.counter += 1
        self._start_date_and_hour = start_date_and_hour
        self._end_date_and_hour = end_date_and_hour
        self._list_matchs = list_matchs

    def __str__(self):
        matchs = ', '.join(['{}'.format(str(match)) for match in self._list_matchs])
        return (
            f'Tour {self._tour_id}\n'
            f'Date de début : {self._start_date_and_hour}\n'
            f'Liste des matchs : {matchs}\n'
            f'Date de fin : {self._end_date_and_hour}\n'
            )

    def __repr__(self):
        tour = (
            f'Round({self._tour_id},'
            f'"{self._start_date_and_hour}",'
            f'"{self._end_date_and_hour}",'
            f'{[str(match) for match in self._list_matchs]})'
        )
        return tour

    # get method
    @property
    def tour_id(self):
        return self._tour_id

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
    @tour_id.setter
    def tour_id(self, x):
        self._tour_id = x

    @list_matchs.setter
    def list_matchs(self, x):
        self._list_matchs = x

    @start_date_and_hour.setter
    def start_date_and_hour(self, x):
        self._start_date_and_hour = x

    @end_date_and_hour.setter
    def end_date_and_hour(self, x):
        self._end_date_and_hour = x

    # serialization
    def serialized(self):
        serialized_tour = {
            "tour_id": self.tour_id,
            "start_date_and_hour": self.start_date_and_hour,
            "end_date_and_hour": self.end_date_and_hour,
            "list_matchs": [match.serialized() for match in self.list_matchs]
        }
        return serialized_tour

    def unserialized(self, serialized_tour):
        tour_id = serialized_tour['tour_id']
        start_date_and_hour = serialized_tour['start_date_and_hour']
        end_date_and_hour = serialized_tour['end_date_and_hour']
        list_matchs = [Match().unserialized(serialized_match)
                       for serialized_match in serialized_tour['list_matchs']]
        return Tour(tour_id, start_date_and_hour,
                    end_date_and_hour, list_matchs)
