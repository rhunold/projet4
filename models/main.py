from player import Player
from match import Match
from rounds import Round
from tournament import Tournament



player1 = Player("Hunold", "Raphael", "03/04/1977", "Homme", 1, [1, 3, 6], 5)
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

round1 = Round("Round 1", [match1, match2, match3, match4])


tournament1 = Tournament("Grand tour été 2022", "Cela va être super !!!", "22/05/2022", "02/06/2022", "Lyon", 4, [0,1,2,3,4], [4,8,22,36,42,52,69,103,88], "Bullet")


# print("On modififie le joueur 1 et on reaffiche en mettant la valeur 22")
# match2.set_player1(22)

# print(player0,player1,player3)

# # retrieving age using getter / 2 way to call
# print(player.get_name())
# print(player._tournament_score)

# setting attributs using setter
# player0.set_played_with([11,12,22])
# print(player0.get_played_with())

# print(player0.get_first_name() + " va affronter " + player3.get_first_name())
# print()
# print(repr(player3))

# print()
# print(f'{player0}\n{player3}')




def main():
    
    # print("########### Joueur1 #############")
    # print(player1)
    print("########### Match1 #############")    
    print(match1)
    print("########### Round1 #############")      
    print(round1)
    # print("########### Tournoi1 #############")    
    # print(tournament1)        
        

if __name__ == "__main__":
    main()
