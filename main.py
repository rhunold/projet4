import time

from models.player import Player
from models.match import Match
from models.rounds import Round
from models.tournament import Tournament


player1 = Player("Hunold", "Raphael", "04/04/1977", "Homme", 1, [1, 3, 6], 5)
player2 = Player("Hunold", "Théa", "14/06/2015", "Femme", 2, [2, 4, 5], 3)
player3 = Player("Hunold", "Gabriel", "11/07/1978", "Homme", 3, [1, 3, 6], 5)
player4 = Player("Hunold", "Aloise", "31/01/1980", "Femme", 4, [2, 4, 5], 3)
player5 = Player("Hunold", "Francis", "12/12/1943", "Homme", 5, [6, 0, 4], 7)
player6 = Player("Hunold", "Flora", "12/08/1980", "Femme", 6, [6, 0, 4], 4)
player7 = Player("Hunold", "Christine", "12/12/1953", "Femme", 7, [6, 0, 4], 2)
player8 = Player("Hunold", "Stephane", "12/12/1973", "Homme", 5, [6, 0, 4], 7)

match1 = Match(([player1,0], [player2,1]))
match2 = Match(([player3,1], [player4,0]))
match3 = Match(([player5,0.5], [player6,0.5]))
match4 = Match(([player7,0], [player8,0]))

round1 = Round("1", [match1, match2, match3, match4])
round2 = Round("2", [match2, match4, match3, match1])

tournament1 = Tournament("Grand tour été 2022", "Cela va être super !!!", "22/05/2022", "02/06/2022", "Lyon", 4, [round1, round2], [player1, player2, player3, player4, player5, player6, player7, player8], "Bullet")



# # retrieving age using getter / 2 way to call
# print(player1.get_name())
# print(player1._name)

# setting attributs using setter
# player1.set_played_with([11,12,22])
# print(player1.get_played_with())

def main():
    
    # print("########### Joueur1 #############")
    # print(player1)
    
    # print("########### Match1 #############")    
    # print(match1)
    
    # print("########### Round1 #############")      
    # print(round1)
    
    # print("########### Tournoi1 #############")    
    # print(tournament1)

    print("########### Vérifier format date joueurs #############")       
    player1.set_birthdate("22-12-2000")  
    
    
    print(player1)    

    
    # print("########### Changer le ranking du joueur 1 #############")       
    # player1.set_rank(12)    
    # print(player1)    
    
    # print("########### Indiqué un gagnant dans le match1 #############")  
    # print(match1)
    # time.sleep(2.5)
    
    # print(match1.set_winner("Raphael"))        
    # print(match1.get_winner())
    # print("Date début")
    # print(match1.get_start_date())
    # print("Date fin après assignation gagnant")           
    # print(match1.get_end_date())    
 
    # print(repr(tournament1))
        

if __name__ == "__main__":
    main()
