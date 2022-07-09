import time
import random
import json
from tkinter import N

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp
from views.interface import CreateTournamentText, LoadTournamentText, LoadPlayerText, CreateOrLoadPlayerText

from controllers.player_manager import LoadPlayerProcess, CreatePlayerProcess
from tinydb import TinyDB, where, Query

json_tournament = 'models/tournament.json'
db = TinyDB(json_tournament)




def load_tournaments():
    tournaments_db = db.all()
    tournaments = []
    for tournament in tournaments_db:
        tournament = Tournament().unserialized(tournament)
        tournaments.append(tournament)       
    return tournaments

    # print(tournaments[0])      

def load_tournament(tournament_id):  
    tournament_db = db.search(Query().fragment({'_tournament_id': tournament_id}))
    if not tournament_db:
        print(f"Cet identifiant n'existe pas dans la base de donnée. Veuillez choisir un identifiant disponible.")
        return LoadTournamentProcess().ask_tournament_id()    
    else:
        tournament = Tournament().unserialized(tournament_db[0])
        return tournament

def display_tournaments_from_db(tournaments):
    for tournament in tournaments:
        print(f"{tournament.tournament_id} {tournament.name} {tournament.description}  {tournament.place}")



def update(tournament_id):
    return json.load(json.loads(tournament_id, default=lambda o: o.__dict__, indent=4))     

class CreateTournamentProcess:
    def display(self):
        
        # Recuperation de la saisie des infos sur le tournois
        user_input = CreateTournamentText().display() 

        # Instanciation Tournois
        tournament_id = user_input[8]
        name = user_input[0]
        description = user_input[1]   
        start_date_and_hour = user_input[2]
        end_date_and_hour = user_input[3]  
        place = user_input[4]               
        tour_number = user_input[5]                  
        time_control = user_input[6]
        list_tours = None
        list_players = None

        tournament_number_players = user_input[7]    
        
        tournament = Tournament(tournament_id, name, description, start_date_and_hour, end_date_and_hour, place, tour_number, time_control, list_tours , list_players)  # Initialisation  
        
        tournament.save()  
        
        # return tournament_info
    # def add_players(self):     
    
    
        # AJOUT DES JOUEURS
        # Dynamique
        
        # while len(tournament.list_players) <= tournament_number_players:
        #     # Demander si on veut créer un joueur ou en choisir un en base
            
        #     create_or_load = CreateOrLoadPlayerText().display()             
                            
        #     if create_or_load == "0":
        #         player = CreatePlayerProcess().display()
        #         tournament.list_players.append(player)
        #         continue
                
        #         # print(player)

        #     elif create_or_load == "1":
        #         player = LoadPlayerProcess().ask_player_id()  
        #         tournament.list_players.append(player)
        #         # tournament.update_list_players(player)
        #         continue
            
        #     else:
        #         # Pour sortir du tournois...et y revenir...
        #         pass
            
        #     if len(tournament.list_players) == tournament_number_players:
        #         break
                
            
        #     # else:
        #     #     print("Cas que l'on aurait pas détecté ou erreur ?")
        #     #     pass
            

        # print(f'Liste des joueurs du tournois : {[player.first_name for player in tournament.list_players]}')

        # Statique
        # EQuivalent de la boucle while pour ajouter des joueurs (créer ou loadé)
        raphael = Player(1,"hunold","raphael","04-04-1977","Homme",1, 0)
        thea = Player(2,"Hunold","Théa","14-06-2015","Femme",5, 0)
        gabriel = Player(3,"Hunold","Gabriel","11-07-1978","Homme",6, 0)
        aloise = Player(4,"Hunold","Aloise","31-01-1980","Femme",7, 0)
        francis = Player(5,"Hunold","Francis","12-12-1943","Homme",2, 0)
        flora = Player(6,"Hunold","Flora","12-08-1980","Femme",11, 0)
        christine = Player(7,"Hunold","Christine","12-12-1953","Femme",10, 0)
        stephane = Player(8,"Hunold","Stephane","12-12-1973","Homme",9, 0)
        
        tournament.list_players = [raphael, thea, gabriel, aloise, francis, flora, christine, stephane] # liste de tous les joueurs    
        
        print(f'Liste des joueurs du tournois : {[player.first_name for player in tournament.list_players]}')
        
            
        # WORKING HERE
        # tournament.update_list_players()        
 
        # return tournament_players
    # def add_tours(self):  
        
        while tournament.tour_number != len(tournament.list_tours): 

            # On génère le 1er tour si aucun tour n'est dans la liste
            if tournament.list_tours == []:
                
                tournament.start_date_and_hour = get_timestamp()
                
                print(f"1er tour")
                
                tour = Tour()

                sort_participants_by_rank = sorted(tournament.list_players, key=lambda x: x.rank, reverse=False)
                
                #initialize the middle index with the length of first half
                middle=int(len(tournament.list_players)/2)

                #Split the list from starting index upto middle index in first half
                first_players = sort_participants_by_rank[:middle]

                #Split the list from middle index index upto the last index in second half
                sec_players = sort_participants_by_rank[middle:]

            else :
                print(f"{str(len(tournament.list_tours)+1)}ème tour")
                tour = Tour()               
                
                #  triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
                sort_participants_by_score_and_rank = sorted(tournament.list_players, key=lambda x: (-x.player_score, x.rank))
                
                #Split the list from starting index upto middle index in first half
                first_players = sort_participants_by_score_and_rank[::2]

                #Split the list from middle index index upto the last index in second half
                sec_players = sort_participants_by_score_and_rank[1::2]            


            allmatch = []
            for first_player, sec_player in zip(first_players, sec_players):
                
                player1_id = first_player.player_id
                player2_id = sec_player.player_id
                    
                match = Match(player1_id, player2_id) 
                
                # Je crée un deuxième match avec pair inversé pour pouvoir vérifier tous les matchs.
                match2 = Match(player2_id, player1_id)                
                
                # Je vérifie que ça ne match pas et si c'est le cas, je choisis un autre joueur 2. Pas 100% sur que ça marche bien...
                for match_done in allmatch:      
                    if match_done == match:
                        print(f"Le match {match} a déjà été joué. On refait l'attribution du joueur 2")  
                        print(match_done, match)
                        iteractir_player2_id = iter(sec_players)
                        old_player2_id = next(iteractir_player2_id)
                        player2_id = next(iteractir_player2_id)
                        match = Match(player1_id, player2_id)
                        match2 = Match(player2_id, player1_id)   
                        break
                    else:
                        continue

                
                # J'ajoute les pairs symetrique à ma liste de tous les matchs
                allmatch.append(match)    
                allmatch.append(match2)    
                
                # On ajoute le match au tour
                tour.list_matchs.append(match)
                
                # On enregistre dans le json
                # tournament.update() 
        
                
            # On joue les match du tour pour assigner le score du match
            for match in tour.list_matchs:

                match.play_match()
                
                # Assignation des points obtenus au score des joueurs
                for player in tournament.list_players:
                    if match.player1_id == player.player_id:
                        player.player_score += match.player1_score
                    if match.player2_id == player.player_id:
                            player.player_score += match.player2_score
                    
                    # print(f"le nouveau score de {participant.player_id} est {participant.player_score}")
            
            time.sleep(0.5)      
            tour._end_date_and_hour = get_timestamp()
            

            # On ajouter le tour au tournois
            tournament.list_tours.append(tour)
        
        # list_tours = tournament.list_tours
        
      

        # Fin du Tounois
        tournament.end_date_and_hour = get_timestamp()
        
        # On enreistre en json
        tournament.save() 
        
        # On serialize / marche pas actuellemnt pour enregistré dans le json...wording on it pour les update de data (car faut aussi deserialiser)
        # data = json.dumps(tournament, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        # print(data)
        
             
        # and the winner of the tournament is / en faire une fonction à mettre plus haut (mais pas trop... après que tournament.list_players soit fixé)
        sort_participants_by_score = sorted(tournament.list_players, key=lambda x: x.player_score, reverse=True)
        
        # Attention il peut y avoir des gagnants  ex aequo.
        print(f"Le gagnant est {sort_participants_by_score[0]}")


         
class LoadTournamentProcess:
    def ask_tournament_id(self):
        while True:    
            tournaments = load_tournaments()
            display_tournaments_from_db(tournaments)
            
            try: 
                tournament_id = LoadTournamentText().display()
                # print(player_id)
                tournament = load_tournament(tournament_id)
                # print(player)
                
            except ValueError:
                print("test ValueError")
            else:
                # print(f"return {player}")
                return tournament
 
    def load_tournament(self, tournament_id):
        tournament = load_tournament(tournament_id)
        return tournament                 
      
        
"""

Liste de tous les tournois (afficher tous les tournois, en selectionner un avant de passer à la suite)
    Liste de tous les joueurs d'un tournoi par ordre alphabétique
    Liste de tous les joueurs d'un tournoi par ordre classement    
    Liste de tous les tours d'un tournoi.
    Liste de tous les matchs d'un tournoi.
    
    
Liste de tous les joueurs :
    par ordre alphabétique ;
    par classement.
    
"""              


        
class TournamentReportProcess:
    
    def display_by_player_name(tournament): 


        tournaments = sorted(tournaments, key=lambda x: x._name, reverse=True)  
        
        display_tournaments_from_db(tournaments)    

    # def display_by_player_rank():
    #     pass
    
    # def display_by_tours():
    #     pass    
    
    # def display_by_matchs():
    #     pass        
                
            

        