
from views.view import View

class HomeText(View):  
    def display(self):
        # while True:
        user_input = self.get_user_input(
            msg_display = "Menu principal\n0 - Gestion des tournois \n1 - Gestion des joueurs\n2 - Voir les rapports\nq - Quitter\nVotre choix : ",
            msg_error = "Veuillez entrer une valeur valide",
            value_type = "selection",
            assertions = ["0", "1", "2", "q"]
            )
        return user_input

class ManageTournamentText(View):  
    def display(self): 
        user_input = self.get_user_input(
            msg_display = "Gestion des tournois\n0 - Créer un tournoi \n1 - Charger un tournois\n2 - Accueil\nVotre choix : ",
            msg_error = "Veuillez entrer une valeur valide",
            value_type = "selection",
            assertions = ["0", "1", "2"]
            )  
        return user_input  
    
    
class ManagePlayerText(View):
    def display(self):     
        user_input = self.get_user_input(
            msg_display = "Gestion des joueurs\n0 - Créer un joueur \n1 - Changer le classement d'un joueur\n2 - Accueil\nVotre choix : ",
            msg_error = "Veuillez entrer une valeur valide",
            value_type = "selection",
            assertions = ["0", "1", "2"]
            ) 
        return user_input 
    
    

    
class ManageReportText(View):
    def display(self):     
        user_input = self.get_user_input(
            msg_display = "Rapports\n0 - Tournois \n1 - Joueurs par ordre alphabétique \n2 - Joueurs par classement \n3 - Accueil\nVotre choix : ",
            msg_error = "Veuillez entrer une valeur valide",
            value_type = "selection",
            assertions = ["0", "1", "2", "3"]
            ) 
        return user_input   
    
    
class ManageTournamentReportText(View):
    def display(self):     
        user_input = self.get_user_input(
            msg_display = "Rapports du tournois XXX \n0 - par nom des joueurs \n1 - par rang des joueurs \n2 - par tour \n3 - par match  \n4 - Retour au menu des rapports\nVotre choix : ",
            msg_error = "Veuillez entrer une valeur valide",
            value_type = "selection",
            assertions = ["0", "1", "2", "3", "4"]
            ) 
        return user_input   
             
    
class CreateTournamentText(View):
    def display(self):  
        # Pointer ver tournament_manager.py   
        
        # name = input("Nom du tournoi:\n> ")

        # place = self.get_user_input(
        #     msg_display="Lieu:\n> ",
        #     msg_error="Veuillez entrer un lieu",
        #     value_type="string"
        # )

        # time_control = self.get_user_input(
        #     msg_display="Type de partie:\n0 - Bullet\n1 - Blitz\n2 - Coup Rapide\n> ",
        #     msg_error="Veuillez entrer 0, 1 ou 2.",
        #     value_type="selection",
        #     assertions=["0", "1", "2"]
        # )
        
        # if time_control == "0":
        #     time_control = "Bullet"
        # elif time_control == "1":
        #     time_control = "Blitz"
        # else:
        #     time_control = "Coup Rapide"

        # number_players = self.get_user_input(
        #     msg_display="Nombre de joueurs:\n> ",
        #     msg_error="Entrer un nombre entier supérieur ou égal à 2.",
        #     value_type="num_superior",
        #     default_value=8
        # )

        # tour_number = self.get_user_input(
        #     msg_display="Nombre de tours (4 par défaut):\n> ",
        #     msg_error="Entrer 4 ou plus.",
        #     value_type="num_superior",
        #     default_value=4
        # )
        
        # description = input("Description du tournoi:\n> ")


        # print(f"\nLe tournoi \"{name}\" a été crée. Vous devez ajouter {number_players} joueurs.")
        
        # user_input = {
        #     "name": name,
        #     "place": place,
        #     "time_control": time_control,
        #     "number_players": number_players,
        #     "tour_number": tour_number,
        #     "description": description
        # }  
        
        tournament_id = 0
        name = "Grand tournois"
        description = "Description"
        start_date_and_hour = "Le tournois n'a pas commencé"
        end_date_and_hour = "Le tournois n'est pas fini"
        place = "Lyon"
        tour_number = 4
        time_control = "Blitz"
        
        number_players = 8

        
        tournament = [name, description, start_date_and_hour, end_date_and_hour, place, tour_number, time_control, number_players, tournament_id]
        
        return tournament  
        

class LoadTournamentText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Quel tournois souhaitez-vous charger ?\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        print("Le tournois à bien été chargé")
        return user_input
    

    
class CreatePlayerText(View):
    def display(self):
        

        # first_name = "Li"
        # name = "Hunold"
        # birthdate = "03-04-1977"
        # sex = "H"
        # rank = 30
                
        
        # first_name = input("""Prénom du joueur:\n> """)
        
        # name = input("""Nom du joueur:\n> """)

        # birthdate = self.get_user_input(
        #     msg_display="Date de naissance (format JJ-MM-AAAA):\n> ",
        #     msg_error="Veuillez entrer une date au format valide: JJ-MM-AAAA",
        #     value_type="date"
        # )

        # sex = self.get_user_input(
        #     msg_display="Sexe (H ou F):\n> ",
        #     msg_error="Veuillez entrer H ou F",
        #     value_type="selection",
        #     assertions=["H", "h", "F", "f"]
        # ).upper()

        # rank = self.get_user_input(
        #     msg_display="Classement:\n> ",
        #     msg_error="Veuillez entrer une valeur numérique valide.",
        #     value_type="numeric"
        # )

        
        first_name = "Aloise"
        name = "Hunold"
        birthdate = "03-04-1977"
        sex = "H"
        rank = 30
        
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
        user_input = self.get_user_input(
            msg_display="Quel joueur souhaitez-vous choisir ?:\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        
        return user_input
    
    
class CreateOrLoadPlayerText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display = "0 - Créer un joueur \n1 - Choisir un joueur en base\nVotre choix : ",
            msg_error = "Veuillez entrer une valeur valide",
            value_type = "selection",
            assertions = ["0", "1"]
        )
        
        return user_input    
    
class LoadTournamentText(View):
    def display(self):
        user_input = self.get_user_input(
            msg_display="Identifiant du tournois à charger:\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )
        
        return user_input
    
    


   