# import random
# import time
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


def load(tournament_id):
    Load = Query()
    tournament_db = db.get(Load.tournament_id == tournament_id)
    tournament = Tournament().unserialized(tournament_db)
    print(f"\nLe tournoi '{tournament.name}' a bien été chargé.")
    return tournament


def display_tournaments_from_db(tournaments):
    if tournaments == []:
        print("\nAucun tournois en base de donnée.")
    else:
        print(f"{'ID' : <5}{'Nom du tournois' : <25}{'Début' : <22}"
              f"{'Fin' : <22}{'Lieu' : <20}{'Description' : <50} ")
        for tournament in tournaments:
            # if tournament.end_date_and_hour != "":
            print(f"{tournament.tournament_id : <5}"
                  f"{tournament.name : <25}"
                  f"{tournament.start_date_and_hour : <22}"
                  f"{tournament.end_date_and_hour : <22}"
                  f"{tournament.place : <20}"
                  f"{tournament.description : <50}"
                  )


def sort_players_by_rank(tournament):
    """Sort players by rank """
    sort_players_by_rank = sorted(tournament.list_players,
                                  key=lambda x: x.rank,
                                  reverse=False)

    # initialize the middle index with the length of first half
    middle = int(len(tournament.list_players)/2)

    # Firt list of players
    first_players = sort_players_by_rank[:middle]

    # Second list of players
    sec_players = sort_players_by_rank[middle:]

    return first_players, sec_players


def sort_player_by_score_and_rank(tournament):
    """Sort players by score and rank if not enought"""

    #  Trie par points et classement si nécessaire
    sort_player_by_score_and_rank = sorted(
        tournament.list_players,
        key=lambda x: (-x.player_score, x.rank))

    # Firt list of players
    first_players = sort_player_by_score_and_rank[::2]

    # Second list of players
    sec_players = sort_player_by_score_and_rank[1::2]

    return first_players, sec_players


def generate_matchs(first_players, sec_players):
    generated_matchs = []

    for first_player, sec_player in zip(first_players, sec_players):

        player1_name = first_player.name
        player2_name = sec_player.name

        match = Match(player1_name, player2_name)
        generated_matchs.append(match)

    return generated_matchs


def generate_pair(match):
    # print(match)
    player_1 = match.player1_name
    player_2 = match.player2_name
    pair = (player_1, player_2)
    sorted_pair = tuple(sorted(pair))
    # print(sorted_pair)
    return sorted_pair


def display_winner(tournament):
    sort = sorted(tournament.list_players,
                  key=lambda x: x.player_score,
                  reverse=True)
    if sort[0].player_score == sort[1].player_score:
        print(f"\nLes gagnants sont {sort[0].first_name} {sort[0].name}"
              f" et {sort[1].first_name} {sort[1].name}"
              f" avec {sort[0].player_score} points.")
    else:
        print(f"\nLe gagnant est {sort[0].first_name}"
              f" {sort[0].name} avec {sort[0].player_score} points.\n")


def display_player(tournament_id, sorted_players):
    print(f"\nJoueurs du tournoi {tournament_id}\n")
    print(f"{'Prénom' : <20}{'Nom' : <20}{'Score' : <10}"
          f"{'Classement' : <12}{'Date de naissance' : <20}{'Sexe' : <10}")
    for player in sorted_players:
        print(
            f"{player.first_name : <20}"
            f"{player.name : <20}"
            f"{player.player_score : <10}"
            f"{player.rank : <12}"
            f"{player.birthdate : <20}"
            f"{player.sex : <10}"
            )


class CreateTournamentProcess:
    def display(self):

        # Collect datas from user input in a dict
        tournament = CreateTournamentText().display()

        # Instanciation of tournament

        tournament_id = 0

        name = tournament["name"]
        description = tournament["description"]

        place = tournament["place"]
        tour_number = tournament["tour_number"]
        time_control = tournament["time_control"]

        start_date_and_hour = "Pas commencé"
        end_date_and_hour = "Pas terminé"
        list_tours = []
        list_players = []

        number_players = tournament["number_players"]

        tournament = Tournament(tournament_id, name, description, start_date_and_hour,
                                end_date_and_hour, place, tour_number,
                                time_control, list_players, list_tours)

        tournament.insert()

        # Adding players
        while len(tournament.list_players) <= number_players:

            # Casser la boucle si on dépasse le nombre de joueurs
            if len(tournament.list_players) == number_players:
                break

            # print(tournament.list_players)

            # Ask user if he want to load a player or create one

            create_or_load = CreateOrLoadPlayerText().display()

            if create_or_load == "0":
                player = CreatePlayerProcess().display()
                tournament.list_players.append(player)
                print(f"{player.first.name} ajouté au tournois")
                continue

            elif create_or_load == "1":
                player = LoadPlayerProcess().ask_player_name()
                tournament.list_players.append(player)
                continue
            else:
                pass

            # Static
            # raphael = Player("aaa", "raphael",
            #                  "04-04-1977", "Homme", 1, 0)
            # thea = Player("bbb", "Thea",
            #               "14-06-2015", "Femme", 2, 0)
            # gabriel = Player("ccc", "Gabriel",
            #                  "11-07-1978", "Homme", 3, 0)
            # inconnu = Player("ddd",
            #                  "Pierre", "31-01-1980", "Femme", 4, 0)
            # francis = Player("eee", "Francis",
            #                  "12-12-1943", "Homme", 6, 0)
            # flora = Player("fff", "Flora",
            #                "12-08-1980", "Femme", 7, 0)
            # christine = Player("ggg", "Christine",
            #                    "12-12-1953", "Femme", 5, 0)
            # stephane = Player("hhh", "Stephane",
            #                   "12-12-1973", "Homme", 8, 0)

            # # liste de tous les joueurs
            # tournament.list_players = [raphael, thea, gabriel,
            #                            inconnu, francis, flora,
            #                            christine, stephane]

            tournament.update_list_players()

        # print(f'Tournoi crée. Liste des joueurs du tournois :\n'
        #       f'{[player.name for player in tournament.list_players]}')

        return tournament


class LoadTournamentProcess:
    def ask_tournament_id(self):
        tournaments = load_tournaments()
        if tournaments:
            while True:
                display_tournaments_from_db(tournaments)
                tournament_id = LoadTournamentText().display()
                try:
                    tournament = load(tournament_id)
                except TypeError:
                    print("\nAucune correspondance. Veuillez réessayer.\n")
                    continue
                else:
                    return tournament
        else:
            print("\nAucun tournoi n'est en base de donnée. Veuillez en créer un.\n")
            tournament = False
            return tournament


class TourProcess:
    def load_tour1(self, tournament):
        # Find the last match not played in tournament or create one
        try:
            # print(tournament)
            tournament.list_tours[-1]

        except IndexError:
            return False
        else:
            return True

    def new_tour(self):
        tour = Tour()
        tour.list_matchs = []
        tour.start_date_and_hour = get_timestamp()
        return tour


class RunTournamentProcess:

    def run(self, tournament):
        existing_pairs = []
        # existing_pairs.clear()

        load_tour1 = TourProcess().load_tour1(tournament)

        if load_tour1 is False:

            tournament.start_date_and_hour = get_timestamp()
            tournament.update_start_date_and_hour()

            tour = TourProcess().new_tour()

            tour_id = 1
            tour.tour_id = tour_id

            first_players = sort_players_by_rank(tournament)[0]
            sec_players = sort_players_by_rank(tournament)[1]

            generated_matchs = generate_matchs(first_players, sec_players)

            for match in generated_matchs:
                tour.list_matchs.append(match)

            tournament.list_tours.append(tour)
            tournament.update_list_tours()

        else:
            tour = tournament.list_tours[-1]

        while len(tournament.list_tours) <= tournament.tour_number:

            # If loading, generate a list of unique pairs
            if existing_pairs == []:
                # existing_pairs = generate_pairs(generated_matchs, existing_pairs)
                for tour in tournament.list_tours:
                    for match in tour.list_matchs:
                        sorted_pair = generate_pair(match)
                        existing_pairs.append(sorted_pair)
                # print({f"Paires existantes : {existing_pairs}"})

            # Break loop when enought tour has been created
            if tour.tour_id >= tournament.tour_number:
                break

            # Create new tour if last one is finished
            if tour.start_date_and_hour != "" and tour.end_date_and_hour != "":

                tour_id = tour.tour_id
                tour = TourProcess().new_tour()
                tour_id += 1
                tour.tour_id = tour_id

                first_players = sort_player_by_score_and_rank(tournament)[0]
                sec_players = sort_player_by_score_and_rank(tournament)[1]

                generated_matchs = generate_matchs(first_players, sec_players)
                # print(f"Matchs avant traitement : {generated_matchs}")

                # If pair already played together, take next player 2
                player_engaged_in_tour = []
                for match in generated_matchs:
                    sorted_pair = generate_pair(match)
                    # print(f"Paire initiale : {sorted_pair}")

                    player1_name = match.player1_name
                    player2_name = iter(sec_players)

                    if sorted_pair in existing_pairs:
                        player2_name_value = iter(sec_players)
                        # print(f"Rencontre {match} déjà faite....")
                        # print(f"Joueur 1 : {player1_name}")
                        # print(f"Ancien joueur 2 : {match.player2_name}")

                        while next(player2_name_value) not in player_engaged_in_tour:
                            try:
                                # player1_name = match.player1_name

                                player2_name = next(player2_name_value)
                                player2_name = player2_name.name
                                # print(f"Nouveau joueur2 : {player2_name}")

                            except StopIteration:
                                # print("StopIteration")
                                # exception will happen when iteration will over
                                break
                            else:
                                # match.player2_name = player2_name.name
                                match = Match(player1_name, player2_name)
                                # print()
                                # print(f"Nouveau match : {match}")
                                break
                        continue
                    else:
                        pass

                    player_engaged_in_tour.append(match.player1_name)
                    player_engaged_in_tour.append(match.player2_name)

                    existing_pairs.append(sorted_pair)
                    # print()
                    # print("Resultats après traitements tour 2+")
                    # print(f"Paires : {existing_pairs}")
                    # print(f"Paires engagées dans le tour : \n{player_engaged_in_tour}")
                    # print()
                player_engaged_in_tour.clear()

            # Add Generated matchs if list match is empty
            if tour.list_matchs == []:

                generated_matchs = generate_matchs(first_players, sec_players)
                for match in generated_matchs:
                    tour.list_matchs.append(match)

                tournament.list_tours.append(tour)
                tournament.update_list_tours()

            # Time to play

            # time.sleep(1)
            if tour.start_date_and_hour != "" and tour.end_date_and_hour == "":
                print(f"\nTour {tour.tour_id}")

                for match in tour.list_matchs:
                    # print(f"Match à venir : {match}")

                    # We are looking for unplayed match
                    if match.player1_score == 0 and match.player2_score == 0:
                        # We ask to design a winner in the match or to exit from tournament
                        if match.play_match() is not False:
                            # Assignation of score and saving
                            for player in tournament.list_players:
                                if player.name == match.player1_name:
                                    player.player_score += match.player1_score
                                    tournament.update_list_players()
                                    tournament.update_list_tours()
                                elif player.name == match.player2_name:
                                    player.player_score += match.player2_score
                                    tournament.update_list_players()
                                    tournament.update_list_tours()
                            # print(tour.list_matchs)

                        else:
                            print("On sort du tournois")
                            # print(tournament.list_tours)
                            tournament.update_list_players()
                            tournament.update_list_tours()
                            return

                print("\nFin de tour")
                # print(tour)
                # print(tour.list_matchs)
                # time.sleep(0.1)

                tour.end_date_and_hour = get_timestamp()
                tournament.update_list_tours()

        tournament.end_date_and_hour = get_timestamp()
        tournament.update_end_date_and_hour()

        # print(tournament)

        # and the winner of the tournament is
        display_winner(tournament)


class TournamentReportProcess:
    def display_by_player_name(self, tournament):
        players = tournament.list_players
        tournament_id = tournament.tournament_id
        sorted_players = sorted(players, key=lambda x: x.name, reverse=False)
        display_player(tournament_id, sorted_players)

    def display_by_player_rank(self, tournament):
        players = tournament.list_players
        tournament_id = tournament.tournament_id
        sorted_players = sorted(players, key=lambda x: x.rank, reverse=False)
        display_player(tournament_id, sorted_players)

    def display_by_tours(self, tournament):
        tours = tournament.list_tours
        print(f"\nTours du tournoi {tournament.tournament_id}\n")
        for tour in tours:
            print(tour)

    def display_by_matchs(self, tournament):
        tours = tournament.list_tours
        print(f"\nMatchs du tournoi {tournament.tournament_id}\n")
        if tours:
            for tour in tours:
                for match in tour.list_matchs:
                    print(match)
