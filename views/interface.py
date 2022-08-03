from views.view import View


class HomeText(View):
    def display(self):
        # while True:
        user_input = self.get_user_input(
            msg_display="Menu principal\n"
            "0 - Gestion des tournois\n"
            "1 - Gestion des joueurs\n"
            "2 - Voir les rapports\n"
            "q - Quitter\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2", "q"]
            )
        return user_input


class ManageTournamentText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Gestion des tournois\n"
            "0 - Créer un tournoi \n"
            "1 - Charger un tournois non terminé.\n"
            "2 - Accueil\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2"]
            )
        return user_input


class ManagePlayerText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Gestion des joueurs\n"
            "0 - Créer un joueur \n"
            "1 - Changer le classement d'un joueur\n"
            "2 - Accueil\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2"]
            )
        return user_input


class ManageReportText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Rapports :\n"
            "0 - Tournois\n"
            "1 - Joueurs par ordre alphabétique\n"
            "2 - Joueurs par classement\n"
            "3 - Accueil\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2", "3"]
            )
        return user_input


class ManageTournamentReportText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Classement du tournois :\n"
            "0 - par nom des joueurs\n"
            "1 - par rang des joueurs\n"
            "2 - par tour\n"
            "3 - par match\n"
            "4 - Retour au menu des rapports\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2", "3", "4"]
            )
        return user_input


class CreateTournamentText(View):
    def display(self):

        name = input("Nom du tournoi:\n>")

        place = self.get_user_input(
            msg_display="Lieu:\n> ",
            msg_error="Veuillez entrer un lieu",
            value_type="string"
        )

        time_control = self.get_user_input(
            msg_display="Type de partie:\n"
            "0 - Bullet\n"
            "1 - Blitz\n"
            "2 - Coup Rapide\n"
            "Votre choix : ",
            msg_error="Veuillez entrer 0, 1 ou 2.",
            value_type="selection",
            assertions=["0", "1", "2"]
        )

        if time_control == "0":
            time_control = "Bullet"
        elif time_control == "1":
            time_control = "Blitz"
        else:
            time_control = "Coup Rapide"

        number_players = self.get_user_input(
            msg_display="Nombre de joueurs:\n> ",
            msg_error="Entrer un nombre entier supérieur ou égal à 2.",
            value_type="num_superior",
            default_value=8
        )

        tour_number = self.get_user_input(
            msg_display="Nombre de tours (4 par défaut):\n> ",
            msg_error="Entrer 4 ou plus.",
            value_type="num_superior",
            default_value=4
        )

        description = input("Description du tournoi:\n> ")

        # description = "Description"
        # place = "Lyon"
        # tour_number = 4
        # time_control = "Blitz"
        # number_players = 8

        user_input = [name, description, place,
                      tour_number, time_control, number_players]

        print(f"Le tournoi \"{name}\" a été crée."
              f"Vous devez ajouter {number_players} joueurs.")
        return user_input


class CreatePlayerText(View):
    def display(self):
        first_name = input("Prénom du joueur:\n> ")

        name = input("Nom du joueur:\n> ")

        birthdate = self.get_user_input(
            msg_display="Date de naissance (format JJ-MM-AAAA):\n>",
            msg_error="Veuillez entrer une date"
            "au format valide: JJ-MM-AAAA",
            value_type="date"
        )

        sex = self.get_user_input(
            msg_display="Sexe (H ou F):\n> ",
            msg_error="Veuillez entrer H ou F",
            value_type="selection",
            assertions=["H", "h", "F", "f"]
        ).upper()

        rank = self.get_user_input(
            msg_display="Classement:\n>",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )

        # first_name = "Aloise"
        # # name = "Hunold"
        # birthdate = "03-04-1977"
        # sex = "H"
        # rank = 30

        player = [name, first_name, birthdate, sex, rank]

        print(f"\nJoueur {first_name} {name} créé.\n")

        return player


class ChangePlayerRankText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Nouveau classement :\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        return user_input


class LoadPlayerText(View):
    def display(self):
        user_input = input("Quel est le nom du joueur ?\n> ")
        return user_input


class CreateOrLoadPlayerText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="0 - Créer un joueur \n"
            "1 - Choisir un joueur en base\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1"]
        )
        return user_input


class LoadTournamentText(View):
    def display(self):
        user_input = input("Quel est le nom du tournois ?\n")
        # print(user_input)
        return user_input


class MatchWinnerText(View):
    def display(self, player1_id, player2_id):
        user_input = self.get_user_input(
            msg_display=f"Qui a gagné le match ?\n"
            f"0 - {player1_id}\n"
            f"1 - {player2_id}\n"
            f"2 - Egalité\n"
            f"3 - Sortir du tournoi\n"
            f"Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2", "3"]
            )
        return user_input
