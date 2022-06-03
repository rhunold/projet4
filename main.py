import time
import random

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from database import *
# match = Match(1, 5, 0.5, 0.5)


def main():
    
    
    

    # On génère le 1er tour si aucun tour n'est dans la liste
    if list_tours == []:

        sort_players_by_rank = sorted(list_players, key=lambda x: x.rank, reverse=False)
        
        # Vérifier que l'on a bien un nombre pair de joueur.
        
        #initialize the middle index with the length of first half
        middle=int(len(list_players)/2)

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
        
        
        list_tours.append(tour1)
 


        """Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        4.	Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        5.	Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.
        """    

    
   
        

    else:
        pass


    # print("########### Joueur1 #############")
    # print(raphael)
    # raphael.rank = 10 
    # print(raphael.rank)    
    # print(random_player1())       
    
    # print("########### Match1 #############")    

    print(tournament)
        

    # time.sleep(2.5)    
        

if __name__ == "__main__":
    main()
 