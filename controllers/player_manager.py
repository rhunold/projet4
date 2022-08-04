# from datetime import datetime
# import time
# import random
# import json
# from controllers.time import get_timestamp

from models.player import Player
from views.interface import CreatePlayerText, \
    ChangePlayerRankText, LoadPlayerText
from tinydb import TinyDB, Query

db = TinyDB('db.json').table('players')


def load_players():
    players_db = db.all()
    players = []
    for player in players_db:
        player = Player().unserialized(player)
        players.append(player)
    return players


def load_player(name):
    player_db = db.search(Query().fragment({'name': name}))
    player = Player().unserialized(player_db[0])
    print(f"Le joueur '{player.name}' a bien été chargé.")
    return player


def display_players_from_db(players):
    for player in players:
        print(f" {player.first_name} {player.name} Classement : {player.rank}")


class CreatePlayerProcess:
    def display(self):
        user_input = CreatePlayerText().display()

        name = user_input[0]
        first_name = user_input[1]
        birthdate = user_input[2]
        sex = user_input[3]
        rank = user_input[4]
        player_score = 0

        player = Player(name, first_name, birthdate, sex, rank, player_score)

        player.insert()
        return player


class LoadPlayerProcess:
    def ask_player_name(self):
        players = load_players()
        if players:

            while True:
                display_players_from_db(players)
                name = LoadPlayerText().display()
                try:
                    player = load_player(name)
                except IndexError:
                    print("Aucun nom correspondant.")
                    continue
                else:
                    return player
        else:
            player = False
            return player


class ChangePlayerRankProcess:
    def display(self, player):
        user_input = ChangePlayerRankText().display()
        player.rank = user_input
        player.update_rank()
        print(f"Le classement de {player.first_name} "
              f"{player.name} a été mis à jour.")


class PlayerReportProcess:
    def display_by_name(self):
        players = load_players()
        players = sorted(players, key=lambda x: x.first_name, reverse=False)
        players = sorted(players, key=lambda x: x.name, reverse=True)
        display_players_from_db(players)

    def display_by_rank(self):
        players = load_players()
        players = sorted(players, key=lambda x: x.rank, reverse=False)
        display_players_from_db(players)
