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


def load_player(player_id):
    Load = Query()
    player_db = db.get(Load.player_id == player_id)
    player = Player().unserialized(player_db)
    print(f"Le joueur '{player.name}' a bien été chargé.")
    return player


def display_players_from_db(players):
    if players == []:
        print("\nAucun joueur en base de donnée.")
    else:
        print("\nJoueurs par ordre alphabétique")
        print(f"{'ID' : <6}{'Prénom' : <20}{'Nom' : <20} {'Classement' : ^10}{'Sex' : ^5}")
        for player in players:
            print(f"{player.player_id : <6}"
                  f"{player.first_name : <20}{player.name : <20}"
                  f"{player.rank : ^10} {player.sex : ^5}")


class CreatePlayerProcess:
    def display(self):
        user_input = CreatePlayerText().display()

        player_id = 0
        name = user_input[0]
        first_name = user_input[1]
        birthdate = user_input[2]
        sex = user_input[3]
        rank = user_input[4]
        player_score = 0

        player = Player(player_id, name, first_name, birthdate, sex, rank, player_score)

        player.insert()
        return player


class LoadPlayerProcess:
    def ask_player_id(self):
        players = load_players()
        if players:
            while True:
                display_players_from_db(players)
                player_id = LoadPlayerText().display()
                try:
                    player = load_player(player_id)
                except TypeError:
                    print("\nAucune correspondance. Veuillez réessayer.\n")
                    continue
                else:
                    return player
        else:
            print("\nAucun joueur n'est en base de donnée. Veuillez en créer un.\n")
            player = False
            return player


class ChangePlayerRankProcess:
    def display(self, player):
        user_input = ChangePlayerRankText().display()
        player.rank = user_input
        player.update_rank()
        print(f"Le classement de {player.first_name} "
              f"{player.name} a été mis à jour.")
        return player.update_rank()


class PlayerReportProcess:
    def display_by_name(self):
        players = load_players()
        players = sorted(players, key=lambda x: (x.name, x.first_name), reverse=False)
        return display_players_from_db(players)

    def display_by_rank(self):
        players = load_players()
        players = sorted(players, key=lambda x: x.rank, reverse=False)
        return display_players_from_db(players)
