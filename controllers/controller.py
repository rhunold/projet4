from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from controllers.time import get_timestamp

from database import *

class CreateTournament:
    
    NUMBER_PARTICIPANTS = 4

    # Instanciation Tournois

    tournament = Tournament()
    
    # match = Match()
    player = Player()

    # tournament.name = "Grand tournoi rentrée 2022"
    # tournament.description = "Welcome !!!"
    # tournament.start_date = get_timestamp()
    # tournament.end_date = ""
    # tournament.list_participants = []
    # tournament.tour_number = 4    
    # tournament.list_tours = [] 
    # tournament.time_control = ""  
    # tournament.location = ""    
    # time.sleep(2.5)   
    
    # print(tournament)
    

    

    
    registered_participants = len(tournament.list_participants)
    print(f"Il y a {str(registered_participants)} joueurs inscrits au tournoi")    
  
    # On demande au directeur de choisir 8 participants parmi les joueurs crées au préalable.
    while registered_participants <= NUMBER_PARTICIPANTS:

        player_id = int(input("Ajouter un joueur avec son identifiant : "))
        tournament.add_player(player_id)
        
        print(f"Il y a {str(len(tournament.list_participants))} joueurs inscrits au tournoi. Il en manque {str(NUMBER_PARTICIPANTS - len(tournament.list_participants))}")        

        if len(tournament.list_participants) == NUMBER_PARTICIPANTS:  
            break
                
    print(f'Liste des joueurs du tournois : {tournament.list_participants}')
    
    
    
    print(f"Ok pour les joueurs. On va générer le 1er tour.")
    


    # On génère le 1er tour si aucun tour n'est dans la liste
    if tournament.list_tours == []:
        
        tour1 = Tour()

        sort_participants_by_rank = sorted(tournament.list_participants, key=lambda x: x.rank, reverse=False)
        
        # Vérifier que l'on a bien un nombre pair de joueur.
        
        #initialize the middle index with the length of first half
        middle=int(len(tournament.list_participants)/2)

        #Split the list from starting index upto middle index in first half
        first_players=sort_participants_by_rank[:middle]

        #Split the list from middle index index upto the last index in second half
        sec_players=sort_participants_by_rank[middle:]

        for i, (first_player, sec_player) in enumerate(zip(first_players, sec_players)):
            # print(repr(first_player), repr(sec_player)) 
            
            player1_id = first_player.player_id
            player2_id = sec_player.player_id
            
            # player1_total_score = first_player.player_score
            # player2_total_score = sec_player.player_score            

            tour1.list_matchs.append(Match(player1_id, player2_id))


        # On ajouter le 1er tour au tournois
        tournament.list_tours.append(tour1)  

              
        
        # On joue les match du tour 1 pour assigner le score du match
        for match in tour1.list_matchs:
            match.play_match()
            
            # print(player1_total_score)
            # print(match.player1_score)            
            # player1_total_score += match.player1_score

            # print(f"Le joueur avec l'id {player1_id} a {player1_total_score} points")            
            
        tour1._end_date_and_hour = get_timestamp()
  


        print(tournament.list_tours)
        # print(tournament.list_participants)               
        
        if tour1:
            print("On passe au tours 2 et suivants")
            
            # On passe au deuxième tour
            # sort_participants_by_score = sorted(tournament.list_participants, key=lambda x: x.player_score, reverse=False)
            
            # print(sort_participants_by_score)            
            
            tour = Tour()
            tournament.list_tours.append(tour)  
            print(tournament.list_tours)
            pass




 


        
        """
        Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. 
        Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        
        Répétez les étapes jusqu'à ce que le tournoi soit terminé.
          """          

        

    # print(tournament)
                 


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
    