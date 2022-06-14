import time
import random

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp

from database import *

class CreateTournament:
    
    NUMBER_PARTICIPANTS = 8

    # Instanciation Tournois

    tournament = Tournament()
    
    # match = Match()
    player = Player()

    tournament.name = "Grand tournoi rentrée 2022"
    tournament.description = "Welcome !!!"
    tournament.start_date = get_timestamp()
    tournament.end_date = ""
    tournament.list_participants = []
    tournament.tour_number = 4    
    tournament.list_tours = [] 
    tournament.time_control = ""  
    tournament.location = ""    
    # time.sleep(2.5)   
    
    # print(tournament)

    
    registered_participants = len(tournament.list_participants)
    print(f"Il y a {str(registered_participants)} joueurs inscrits au tournoi")    
  
    # On demande au directeur de choisir 8 participants parmi les joueurs crées au préalable.
    while registered_participants <= NUMBER_PARTICIPANTS:
        
        player_id = random.randrange(10) # Ajout automatique d'un joueur ayant id de 0 à 10
        # player_id = int(input("Ajouter un joueur avec son identifiant : "))
        
        tournament.add_player(player_id)
        
        print(f"Il y a {str(len(tournament.list_participants))} joueurs inscrits au tournoi. Il en manque {str(NUMBER_PARTICIPANTS - len(tournament.list_participants))}")        

        if len(tournament.list_participants) == NUMBER_PARTICIPANTS:  
            break
                
    print(f'Liste des joueurs du tournois : {tournament.list_participants}')
    
    
    
    print(f"Ok pour les joueurs.")
    
    while tournament.tour_number != len(tournament.list_tours): 

        # On génère le 1er tour si aucun tour n'est dans la liste
        if tournament.list_tours == []:
            
            print(f"1er tour")
            
            tour = Tour()

            sort_participants_by_rank = sorted(tournament.list_participants, key=lambda x: x.rank, reverse=False)
            
            # Vérifier que l'on a bien un nombre pair de joueur.
            
            #initialize the middle index with the length of first half
            middle=int(len(tournament.list_participants)/2)

            #Split the list from starting index upto middle index in first half
            first_players=sort_participants_by_rank[:middle]

            #Split the list from middle index index upto the last index in second half
            sec_players=sort_participants_by_rank[middle:]

        else :
            print(f"{str(len(tournament.list_tours)+1)}ème tour")
            tour = Tour()               
            
            #  triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
            sort_participants_by_score_and_rank = sorted(tournament.list_participants, key=lambda x: (-x.player_score, x.rank))
            
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
            
            for match_done in allmatch:      
                if match_done == match:
                    print(f"Le match {match} a déjà été joué. On refait l'attribution du joueur 2")  
                    # print(match_done, match)
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
        
            
        # On joue les match du tour pour assigner le score du match
        for match in tour.list_matchs:

            match.play_match()
            
            # Assignation des points obtenus au score des joueurs
            for participant in tournament.list_participants:
                if match.player1_id == participant.player_id:
                    participant.player_score += match.player1_score
                if match.player2_id == participant.player_id:
                        participant.player_score += match.player2_score
                
                # print(f"le nouveau score de {participant.player_id} est {participant.player_score}")
        
        time.sleep(1.5)      
        tour._end_date_and_hour = get_timestamp()

        # On ajouter le tour au tournois
        tournament.list_tours.append(tour)
        
    print(tournament)
    
    # and the winner of the tournament is 
    sort_participants_by_score = sorted(tournament.list_participants, key=lambda x: x.player_score, reverse=True)
    print(f"Le gagnant est {sort_participants_by_score[0]}")

    
        
            


class CreatePlayer:
    # Instanciation Joueur    
    player = Player()
    player.name = "Hunold"
    player.first_name = "Gael"
    player.birthdate = "30-07-2014"
    player.rank = 25
    player.sex = "Homme"
    player.player_id = 9

    list_players.append(player) # Ajout à la liste des joueurs
    