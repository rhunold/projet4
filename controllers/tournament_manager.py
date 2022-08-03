import time
# import random
# import json
# from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp
from views.interface import CreateTournamentText, \
    LoadTournamentText, CreateOrLoadPlayerText

from controllers.player_manager import LoadPlayerProcess, CreatePlayerProcess

from tinydb import TinyDB, Query

db = TinyDB('db.json').table('tournaments')


def load_tournaments():
    tournaments_db = db.all()
    tournaments = []
    for tournament in tournaments_db:
        tournament = Tournament().unserialized(tournament)
        tournaments.append(tournament)
    return tournaments


def load_tournament(name):
    tournament_db = db.search(Query().fragment({'name': name}))

    if not tournament_db:
        print("Cet identifiant n'existe pas dans la base de donnée.")
        # return LoadTournamentProcess().ask_tournament_id()
    else:
        tournament = Tournament().unserialized(tournament_db[0])
        print(f"Le tournoi '{tournament.name}' a bien été chargé.")
        return tournament


def display_tournaments_from_db(tournaments):
    for tournament in tournaments:
        print(
            f"Nom du tournois : {tournament.name} / "
            f"Description : {tournament.description} / "
            f"Lieu : {tournament.place} / "
            f"Début : {tournament.start_date_and_hour} / "
            f"Fin : {tournament.end_date_and_hour}"
            )


class CreateTournamentProcess:
    def display(self):

        # Recuperation de la saisie des infos sur le tournois
        user_input = CreateTournamentText().display()

        # Instanciation Tournois

        name = user_input[0]
        description = user_input[1]

        place = user_input[2]
        tour_number = user_input[3]
        time_control = user_input[4]

        # tournament_id = 0
        start_date_and_hour = "Le tournois n'a pas commencé"
        end_date_and_hour = "Le tournois n'est pas fini"
        list_tours = []
        list_players = []

        tournament_number_players = user_input[5]

        tournament = Tournament(name, description, start_date_and_hour,
                                end_date_and_hour, place, tour_number,
                                time_control, list_players, list_tours)
        tournament.save()

        # AJOUT DES JOUEURS
        # Dynamique
        # Gerer cas ou il n'y a pas de joueurs dans la bdd...

        while len(tournament.list_players) <= tournament_number_players:

            # Casser la boucle si on dépasse le nombre de joueurs
            if len(tournament.list_players) == tournament_number_players:
                break

            print(tournament.list_players)

            # Demander si on veut créer un joueur ou en choisir un en base

            create_or_load = CreateOrLoadPlayerText().display()

            if create_or_load == "0":
                player = CreatePlayerProcess().display()
                tournament.list_players.append(player)
                # tournament.update_list_players()
                continue

            elif create_or_load == "1":
                player = LoadPlayerProcess().ask_player_id()
                tournament.list_players.append(player)
                continue

            # else:
            #     # Pour sortir du tournois...et y revenir...
            #     pass

            # Statique
            # raphael = Player("Hunold", "raphael",
            #                  "04-04-1977", "Homme", 1, 0)
            # thea = Player("Davron", "Thais",
            #               "14-06-2015", "Femme", 5, 0)
            # gabriel = Player("Vigilant", "Xavier",
            #                  "11-07-1978", "Homme", 6, 0)
            # inconnu = Player("Lemasson",
            #                  "Pierre", "31-01-1980", "Femme", 7, 0)
            # francis = Player("Deluxe", "Nolan",
            #                  "12-12-1943", "Homme", 2, 0)
            # flora = Player("Regier", "Flora",
            #                "12-08-1980", "Femme", 11, 0)
            # christine = Player("Rackam", "Marc",
            #                    "12-12-1953", "Femme", 10, 0)
            # stephane = Player("Perrotie", "Stef",
            #                   "12-12-1973", "Homme", 9, 0)

            # # liste de tous les joueurs
            # tournament.list_players = [raphael, thea, gabriel,
            #                            inconnu, francis, flora,
            #                            christine, stephane]

            tournament.update_list_players()

        # print(f'Liste des joueurs du tournois :'
        #       f'{[player.name for player in tournament.list_players]}')

        return tournament


class RunTournamentProcess:
    def run(self, tournament):

        tournament.start_date_and_hour = get_timestamp()
        tournament.update_start_date_and_hour()

        while tournament.tour_number != len(tournament.list_tours):

            # On génère le 1er tour si aucun tour n'est dans la liste
            if tournament.list_tours == []:

                print("1er tour")
                tour = Tour()
                tour.list_matchs = []
                tour.tour_id = 1
                tour.start_date_and_hour = get_timestamp()

                sort_participants_by_rank = sorted(tournament.list_players,
                                                   key=lambda x: x.rank,
                                                   reverse=False)

                # initialize the middle index with the length of first half
                middle = int(len(tournament.list_players)/2)

                # Firt list of players
                first_players = sort_participants_by_rank[:middle]

                # Second list of players
                sec_players = sort_participants_by_rank[middle:]

            else:
                print(f"{str(len(tournament.list_tours)+1)}ème tour")
                tour = Tour()
                tour.list_matchs = []
                tour.tour_id = len(tournament.list_tours) + 1
                tour.start_date_and_hour = get_timestamp()

                #  Trie par points et classement si nécessaire
                sort_player_by_score_and_rank = sorted(
                    tournament.list_players,
                    key=lambda x: (-x.player_score, x.rank))

                # Firt list of players
                first_players = sort_player_by_score_and_rank[::2]

                # Second list of players
                sec_players = sort_player_by_score_and_rank[1::2]

            allmatch = []
            for first_player, sec_player in zip(first_players, sec_players):

                player1_id = first_player.name
                player2_id = sec_player.name

                match = Match(player1_id, player2_id)

                # On ajoute le match au tour
                tour.list_matchs.append(match)

                # On crée aussi le match mirroir
                match2 = Match(player2_id, player1_id)

                # Je vérifie que ça ne match pas
                # si c'est le cas, je choisis un autre joueur 2
                for match_done in allmatch:
                    if match_done == match:
                        print(f"Le match {match} a déjà été joué."
                              f"On refait l'attribution du joueur 2")
                        print(match_done, match)
                        iteractir_player2_id = iter(sec_players)
                        # old_player2_id = next(iteractir_player2_id)
                        player2_id = next(iteractir_player2_id)
                        match = Match(player1_id, player2_id)
                        match2 = Match(player2_id, player1_id)
                        break
                    else:
                        continue

                # J'ajoute les pairs symetrique à ma liste de tous les matchs
                allmatch.append(match)
                allmatch.append(match2)

            # On joue les match du tour pour assigner le score du match
            for match in tour.list_matchs:

                # Verify score for loaded tournament
                if match.player1_score == 0 and match.player2_score == 0:

                    # print("On sort du tournois.")
                    if match.play_match() is False:
                        pause = tournament.save()
                        return pause
                    else:

                        # Assignation of score and saving
                        for player in tournament.list_players:
                            if player.name == match.player1_id:
                                player.player_score += match.player1_score
                            if player.name == match.player2_id:
                                player.player_score += match.player2_score

                            tournament.update_list_players()
                            # continue
                    # If match played, just continue
                    # continue

            tour._end_date_and_hour = get_timestamp()

            # On ajouter le tour au tournois
            tournament.list_tours.append(tour)
            tournament.update_list_tours()
            time.sleep(1)

        # Fin du Tounois
        tournament.end_date_and_hour = get_timestamp()
        tournament.update_end_date_and_hour()
        # tournament.save()

        # print(tournament)

        # and the winner of the tournament is
        sort_players_by_score = sorted(tournament.list_players,
                                       key=lambda x: x.player_score,
                                       reverse=True)

        # Attention il peut y avoir des gagnants  ex aequo.
        first_score = sort_players_by_score[0].player_score
        second_score = sort_players_by_score[1].player_score
        first_name = sort_players_by_score[0].name
        second_name = sort_players_by_score[1].name
        first_first_name = sort_players_by_score[0].first_name
        second_first_name = sort_players_by_score[1].first_name

        if first_score == second_score:
            print(f"Les gagnants sont {first_first_name} {first_name}"
                  f" et {second_first_name} {second_name}"
                  f"avec {first_score} points.")
        else:
            print(f"Le gagnant est {first_first_name}"
                  f" {first_name} avec {first_score}.")

        time.sleep(5)


class LoadTournamentProcess:
    def ask_tournament_id(self):
        tournaments = load_tournaments()
        while True:
            display_tournaments_from_db(tournaments)

            try:
                name = LoadTournamentText().display()
                tournament = load_tournament(name)

            except ValueError:
                print("ValueError detectée.")
            else:
                return tournament


class TournamentReportProcess:
    def display_by_player_name(self, tournament):
        players = tournament.list_players
        sorted_players = sorted(players, key=lambda x: x.name, reverse=False)
        for player in sorted_players:
            print(player)

    def display_by_player_rank(self, tournament):
        players = tournament.list_players
        sorted_players = sorted(players, key=lambda x: x.rank, reverse=True)
        for player in sorted_players:
            print(player)

    def display_by_tours(self, tournament):
        tours = tournament.list_tours
        for tour in tours:
            print(tour)

    def display_by_matchs(self, tournament):
        tours = tournament.list_tours
        for tour in tours:
            for match in tour.list_matchs:
                print(match)
