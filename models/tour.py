from controllers.time import get_timestamp

from models.match import Match

from typing import List
import json

# from tinydb import TinyDB
# tournament_database = TinyDB('models/tournament.json')

# from models.tournament import Tournament
# from models.player import Player


class Tour():
    """Round Model"""
    class_counter= 1
    
    def __init__(self, list_matchs=None):
        # self._name = "Round " + str(name)
        self._tour_id= Tour.class_counter
        Tour.class_counter += 1        
        
        if list_matchs is None: 
            self._list_matchs= []
        else:
            self._list_matchs=  List[Match]  
        
        self._start_date_and_hour = get_timestamp()
        self._end_date_and_hour = "0"

       
        
        # self._tour_id = 0
        # self._round_number = len(list_matchs)
        # self._active_round = False 
            
                        
  
    def __str__(self):
        return (
            f'Round {self._tour_id},'
            f'{[str(match) for match in self._list_matchs]},'
            f'{self._start_date_and_hour},'
            f'{self._end_date_and_hour}'              

            # f'Roundssssss("{self._id}",'

            # f'{[str(match) for match in self._list_matchs]},'
            # f'"{self._start_date_and_hour}",'
            # f'"{self._end_date_and_hour}")'  
                        
            )


    def __repr__(self):
        tour = (
            # f'({self._name}, {[str(match) for match in self._list_matchs]})'
            
            f'Round ("{self._tour_id}",'

            f'{[str(match) for match in self._list_matchs]},'
            f'"{self._start_date_and_hour}",'
            f'"{self._end_date_and_hour}")'                
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
        self._end_date = x 
        

    # others methods

    def from_json(cls, data):
        list_matchs = list(map(Match.from_json, data["list_matchs"]))
        return cls(list_matchs)

  
    
    # serialization
    # def serialized(self):
    #     serialized_tour =  {
    #         "tour_id": self.tour_id,
    #         "list_matchs": [match.serialized() for match in self.list_matchs]
    #     }
    #     return serialized_tour       
        


    # def unserialized(self, serialized_tour):
    #     tour_id = serialized_tour['tour_id']
    #     list_matchs = serialized_tour['list_matchs']
    #     return Tour(tour_id,
    #                 list_matchs
    #                 )
    
