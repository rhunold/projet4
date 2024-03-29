from views.view import View


class HomeText(View):
    def display(self):
        # while True:
        user_input = self.get_user_input(
            msg_display="\nMenu principal\n"
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
            msg_display="\nGestion des tournois\n"
            "0 - Créer un tournoi \n"
            "1 - Charger un tournois\n"
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
            msg_display="\nGestion des joueurs\n"
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
            msg_display="\nRapports :\n"
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
            msg_display="\nClassement du tournois :\n"
            "0 - Par nom des joueurs\n"
            "1 - Par rang des joueurs\n"
            "2 - Par tour\n"
            "3 - Par match\n"
            "4 - Retour au menu des rapports\n"
            "Votre choix : ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2", "3", "4"]
            )
        return user_input


class CreateTournamentText(View):
    def display(self):

        name = self.get_user_input(
            msg_display="\nNom du tournois:\n",
            msg_error="Veuillez entrer des lettres",
            value_type="string"
        )

        place = self.get_user_input(
            msg_display="\nLieu:\n",
            msg_error="Veuillez entrer des lettres",
            value_type="string"
        )

        time_control = self.get_user_input(
            msg_display="\nType de partie:\n"
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
            msg_display="\nNombre de joueurs:\n",
            msg_error="Entrer un nombre entier supérieur ou égal à 2.",
            value_type="num_superior",
            default_value=8
        )

        tour_number = self.get_user_input(
            msg_display="\nNombre de tours (4 par défaut):\n",
            msg_error="Entrer 4 ou plus.",
            value_type="num_superior",
            default_value=4
        )

        description = self.get_user_input(
            msg_display="\nDescription du tournoi:\n",
            msg_error="Veuillez entrer des lettres",
            value_type="string"
        )

        # Static Values
        # name = input("Nom du tournoi:")
        # description = "Description"
        # place = "Lyon"
        # tour_number = 4
        # time_control = "Blitz"
        # number_players = 8

        tournament = {"name": name, "description": description,
                      "place": place, "tour_number": tour_number,
                      "time_control": time_control,
                      "number_players": number_players}

        print(f'\nLe tournoi {tournament["name"]} a été crée.\n'
              f'Vous devez ajouter {tournament["number_players"]} joueurs.\n')
        return tournament


class CreatePlayerText(View):
    def display(self):
        first_name = self.get_user_input(
            msg_display="\nPrénom:\n",
            msg_error="Veuillez entrer des lettres",
            value_type="string"
        )

        name = self.get_user_input(
            msg_display="\nNom:\n",
            msg_error="Veuillez entrer des lettres",
            value_type="string"
        )

        birthdate = self.get_user_input(
            msg_display="\nDate de naissance (format JJ-MM-AAAA):\n",
            msg_error="Veuillez entrer une date au format valide: JJ-MM-AAAA",
            value_type="date"
        )

        sex = self.get_user_input(
            msg_display="\nSexe (H ou F):\n",
            msg_error="Veuillez entrer H ou F",
            value_type="selection",
            assertions=["H", "h", "F", "f"]
        ).upper()

        rank = self.get_user_input(
            msg_display="\nClassement:\n",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )

        # Statics Values
        # name = "Hunold"
        # first_name = "Aloise"
        # name = "Hunold"
        # birthdate = "03-04-1977"
        # sex = "H"
        # rank = 30

        player = [name, first_name, birthdate, sex, rank]

        print(f"\nJoueur {first_name} {name} créé.\n")

        return player


class ChangePlayerRankText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="\nNouveau classement :\n",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        return user_input


class LoadPlayerText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="\nQuel est le numero du joueur ?\n",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        return user_input


class CreateOrLoadPlayerText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="\n0 - Créer un joueur \n"
            "1 - Choisir un joueur en base\n"
            "Votre choix : \n",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1"]
        )
        return user_input


class LoadTournamentText(View):
    def display(self):
        # user_input = input("\nQuel est le numero du tournois ?\n")
        user_input = self.get_user_input(
            msg_display="\nQuel est le numero du tournois ?\n",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        return user_input


class MatchWinnerText(View):
    def display(self, player1_id, player2_id):
        user_input = self.get_user_input(
            msg_display=f"\nQui a gagné le match ?\n"
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
