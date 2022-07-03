import time
import random
import json

from models.player import Player, players
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp
from views.interface import CreateTournamentText, LoadTournamentText

from tinydb import TinyDB, where, Query

json_tournament = 'models/tournament.json'
db = TinyDB(json_tournament)


# list_players = []

def show_tournaments():
    tournaments_db = db.all()
    tournaments = []
    
    for tournament in tournaments_db:
        # tournament = Tournament().unserialized(tournament)
        # tournament = Tournament().from_json(json.loads(Tournament().toJson()))        
        tournaments.append(tournament)
        print(tournament)

    # print(tournaments[0])      

def load_tournament(tournament_id):  
    search_result = db.search(Query().fragment({'_tournament_id': tournament_id}))
    loaded_tournament = Tournament().unserialized(search_result[0])
    return loaded_tournament

def add_player_to_tournament(player_id):
    if any(player.player_id == player_id for player in players):
        for player in players:
            if player.player_id == player_id :
                
                list_players.append(player) # on ajoute le joueur dans les participants
                players.remove(player) # On enlève le joueur des joueurs disponibles
        return None 


    else:
        print(f"Il n'existe pas de joueur avec l'identifiant {player_id} ou il a déjà été sélectionné")     

 

class CreateTournamentProcess:
    def display(self):
        tournament = Tournament()  # Initialisation
        
        user_input = CreateTournamentText().display() # Saisie

        # Instanciation Tournois
        tournament.name = user_input["name"]
        tournament.place = user_input["place"]                
        tournament.time_control = user_input["time_control"]
        tournament.tour_number = user_input["tour_number"]
        tournament.description = user_input["description"]    
        
        tournament_number_players = user_input["number_players"]          

        # tournament.save() 
                
                
        # Si pas de joueurs dans la bdd ou pas assez (inferieur à tournament_number_players), afficher un message indiquant qu'il faut d'abord crée au moins x joueurs
        # Code à écrire...
        
        
        registered_participants = len(tournament.list_players)
        # print(f"Il y a {str(registered_participants)} joueurs inscrits au tournoi")    
    
        # On demande au directeur de choisir 8 participants parmi les joueurs crées au préalable.
        while registered_participants <= tournament_number_players:
            
            # On affiche un menu pour proposer 1/ soit de créer un nouveau joueur, 2/ soit de le charger à partir de la bdd
            
            player_id = random.randrange(10) # Ajout automatique d'un joueur ayant id de 0 à 10
            
            # Faire en sorte que le code ci dessous se retourve dans  interface.py 
            # player_id = int(input("Ajouter un joueur avec son identifiant : "))
            
            tournament.add_player(player_id)
            # add_player_to_tournament(player_id)            
            
            # # Faire en sorte que le code ci dessous se retourve dans  interface.py             
            print(f"Il y a {str(len(tournament.list_players))} joueurs inscrits au tournoi. Il en manque {str(tournament_number_players - len(tournament.list_players))}")        

            if len(tournament.list_players) == tournament_number_players:  
                break
                    
        print(f'Liste des joueurs du tournois : {tournament.list_players}')

        # tournament.save() 
        # tournament.update() 
        
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
                first_players=sort_participants_by_rank[:middle]

                #Split the list from middle index index upto the last index in second half
                sec_players=sort_participants_by_rank[middle:]

            else :
                print(f"{str(len(tournament.list_tours)+1)}ème tour")
                tour = Tour()               
                
                #  triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
                sort_participants_by_score_and_rank = sorted(tournament.list_players, key=lambda x: (-x.player_score, x.rank))
                
                #Split the list from starting index upto middle index in first half
                first_players=sort_participants_by_score_and_rank[::2]

                #Split the list from middle index index upto the last index in second half
                sec_players=sort_participants_by_score_and_rank[1::2]            


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
        # tournament.update() 
        
        # On serialize / marche pas actuellemnt pour enregistré dans le json...wording on it pour les update de data (car faut aussi deserialiser)
        # data = json.dumps(tournament, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        # print(data)

        # On deserialize 
        data = json.dumps(tournament, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        deserialize_data = tournament.from_json(json.loads(data))
        deserialize_data
             
        # deserialize_data = tournament.from_json(json.loads(json.loads(json.dumps(tournament, default=lambda o: o.__dict__, indent=4))))
        print(deserialize_data)        
        
        # and the winner of the tournament is / en faire une fonction à mettre plus haut (mais pas trop... après que tournament.list_players soit fixé)
        sort_participants_by_score = sorted(tournament.list_players, key=lambda x: x.player_score, reverse=True)
        
        # Attention il peut y avoir des gagnants  ex aequo.
        print(f"Le gagnant est {sort_participants_by_score[0]}")


class LoadTournamentProcess:
    def display(self):   
        
        show_tournaments()
        
        user_input = LoadTournamentText().display()  

        tournament_id = user_input
        tournament = load_tournament(tournament_id)

        print(f"Le tournois {tournament.name} a été chargé avec succés.") 
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
    def display_player_by_name(self): 
        pass
    
    def display_player_by_rank(self): 
        pass    
        
    def display_tour(self): 
        pass     
    
    def display_match(self): 
        pass             
        