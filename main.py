import time
import random

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp, get_date


from database import *


# def add_player(player_id):
#     # On s'assure que la liste des joueurs comprend un joueur avec l'id demandé
#     if any(player.player_id == player_id for player in list_players):
#         for player in list_players:
#             if player.player_id == player_id:
#                 # f'"Le joueur {player_id} existe et a été ajouté au tournoi.'
#                 list_participants.append(player)
#         return None 

#     else:
#         print("Il n'existe pas de joueur avec cet identifiant")


NUMBER_PARTICIPANTS = 8


def main():
    
    
    # Instanciation Tournois

    tournament = Tournament()

    tournament.name = "Grand tournoi rentrée 2022"
    tournament.description = "Welcome !!!"
    # tournament.start_date = get_timestamp()
    # tournament.end_date = ""
    # tournament.list_participants = []
    # tournament.tour_number = 4    
    # tournament.list_tours = [] 
    # tournament.time_control = ""  
    # tournament.location = ""    

    print(tournament)

    
    # Instanciation Joueur    
    player = Player()
    player.name = "Hunold"
    player.first_name = "Gael"
    player.birthdate = "30-07-2014"
    player.rank = 25
    player.sex = "Homme"
    player.player_id = 9

    list_players.append(player) # Ajout à la liste des joueurs
    

    
    print(tournament.list_participants)
    
    # print(any(players)) On vérifie qu'il existe des joueurs avant de les ajouter au tournois
    
    registered_participants = len(tournament.list_participants)
    
    print(f"Il y a {str(registered_participants)} joueurs inscrits au tournoi")    
    
  
    # On demande au directeur de choisir 8 participants parmi les joueurs crées au préalable.
    while registered_participants <= NUMBER_PARTICIPANTS:
        
        player_id = int(input("Ajouter un joueur avec son identifiant : "))
        tournament.add_player(player_id)
        print(f"Il y a {str(len(tournament.list_participants))} joueurs inscrits au tournoi. Il en manque {str(NUMBER_PARTICIPANTS - len(tournament.list_participants))}")        

        if len(tournament.list_participants) == NUMBER_PARTICIPANTS:
            
            break
                
    # print(f'Liste des joueurs du tournois : {tournament.list_participants}')
    
    print("Ok pour les joueurs. On va générer le 1er tour et maintenant on va entrer les scores.")
    


    


    # On génère le 1er tour si aucun tour n'est dans la liste
    if tournament.list_tours == []:

        sort_players_by_rank = sorted(tournament.list_participants, key=lambda x: x.rank, reverse=False)
        
        # Vérifier que l'on a bien un nombre pair de joueur.
        
        #initialize the middle index with the length of first half
        middle=int(len(tournament.list_participants)/2)

        #Split the list from starting index upto middle index in first half
        first_players=sort_players_by_rank[:middle]
        # print(first_players)

        #Split the list from middle index index upto the last index in second half
        sec_players=sort_players_by_rank[middle:]
        # print(sec_players)
    
        list_matchs = []
        tour1 = Tour(1, list_matchs)          

        for i, (first_player, sec_player) in enumerate(zip(first_players, sec_players)):
            # print(repr(first_player), repr(sec_player))
            player1_id = first_player.player_id
            player2_id = sec_player.player_id
            list_matchs.append(Match(player1_id, player2_id, 0, 0))
            
        
        
        tournament.list_tours.append(tour1)
        
        print(tour1)
        
        # Ensuite on demande qui a gagné pour chaque match joué.
 
    else:
        
        """Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        4.	Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        5.	Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.
        

        """    
        print("Test")

        sort_players_by_score = sorted(list_participants, key=lambda x: x.player_score, reverse=False)
        
        print(sort_players_by_score)
        
        # for player in list_players:
        #     pass

    print(tournament)
        

    # time.sleep(2.5)    
        

if __name__ == "__main__":
    main()
 