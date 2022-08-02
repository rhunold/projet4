from views.interface import HomeText, ManageTournamentText, \
    ManagePlayerText, ManageReportText, ManageTournamentReportText
from controllers.player_manager import CreatePlayerProcess, \
    ChangePlayerRankProcess, LoadPlayerProcess, PlayerReportProcess
from controllers.tournament_manager import CreateTournamentProcess, \
    LoadTournamentProcess, TournamentReportProcess
# from views.view import View

# HOME


class Home:
    def display(self):
        user_input = HomeText().display()
        if user_input == "0":
            CreateTournament().display()
        elif user_input == "1":
            ManagePlayer().display()

        elif user_input == "2":
            ManageReport().display()
        else:
            quit()

# PLAYER


class ManagePlayer:
    def display(self):
        user_input = ManagePlayerText().display()

        if user_input == "0":
            CreatePlayer().display()

        elif user_input == "1":
            ChangePlayerRank().display()
        else:
            Home().display()


class CreatePlayer:
    def display(self):
        CreatePlayerProcess().display()
        ManagePlayer().display()
        # Home().display()


class LoadPlayer:
    def display(self):
        LoadPlayerProcess().display()


# Ne pas afficher si pas de joueur dans la bd
class ChangePlayerRank:
    def display(self):
        player = LoadPlayerProcess().ask_player_id()
        ChangePlayerRankProcess().display(player)
        ManagePlayer().display()


# TOURNAMENT


class ManageTournament:
    def display(self):
        user_input = ManageTournamentText().display()

        if user_input == "0":
            CreateTournament().display()
            print("Infos du tournois enregistré."
                  "Maintenant il faut ajouter des joueurs"
                  "dans le fichier tournament_manager.py")

        elif user_input == "1":
            LoadTournament().display()
            Home().display()
            pass
        else:
            Home().display()


class CreateTournament:
    def display(self):
        CreateTournamentProcess().display()
        Home().display()


class LoadTournament:
    def display(self):
        tournament = LoadTournamentProcess().ask_tournament_id()
        # Home().display()
        return tournament


# RAPPORTS


class ManageReport:
    def display(self):
        user_input = ManageReportText().display()

        if user_input == "0":
            tournament = LoadTournament().display()
            ManageTournamentReport().display(tournament)
        elif user_input == "1":
            PlayerReport().display_by_name()
            # ManageReport().display()
        elif user_input == "2":
            PlayerReport().display_by_rank()
        else:
            Home().display()


class PlayerReport:
    def display_by_name(self):
        PlayerReportProcess().display_by_name()
        ManageReport().display()

    def display_by_rank(self):
        PlayerReportProcess().display_by_rank()
        ManageReport().display()


class ManageTournamentReport:
    def display(self, tournament):
        user_input = ManageTournamentReportText().display()

        if user_input == "0":
            TournamentReportProcess().display_by_player_name(tournament)
            ManageTournamentReport().display(tournament)
        elif user_input == "1":
            TournamentReportProcess().display_by_player_rank(tournament)
            ManageTournamentReport().display(tournament)
        elif user_input == "2":
            TournamentReportProcess().display_by_tours(tournament)
            ManageTournamentReport().display(tournament)
        elif user_input == "3":
            TournamentReportProcess().display_by_matchs(tournament)
            ManageTournamentReport().display(tournament)
        elif user_input == "4":
            ManageReport().display()

        # else:
        #     Home().display()
