import time
import random

from models.player import Player
from models.match import Match
from models.rounds import Round
from models.tournament import Tournament


# Instanciations
raphael = Player(1,"hunold","raphael","04-04-1977","Homme",1)
thea = Player(2,"Hunold","Théa","14-06-2015","Femme",8)
gabriel = Player(3,"Hunold","Gabriel","11-07-1978","Homme",6)
aloise = Player(4,"Hunold","Aloise","31-01-1980","Femme",8)
francis = Player(5,"Hunold","Francis","12-12-1943","Homme",2)
flora = Player(6,"Hunold","Flora","12-08-1980","Femme",10)
christine = Player(7,"Hunold","Christine","12-12-1953","Femme",14)
stephane = Player(8,"Hunold","Stephane","12-12-1973","Homme",9)

players = [raphael, thea, gabriel, aloise, francis, flora, christine, stephane]



match1 = Match((raphael,thea))
match2 = Match((gabriel,aloise))
match3 = Match((francis,flora))
match4 = Match((christine,stephane))

# match1 = Match(player_pair())
# match2 = Match(player_pair())
# match3 = Match(player_pair())
# match4 = Match(player_pair())


# match1 = Match(([player1,0],[player2,1])) # winner = player2
# match2 = Match(([player1,1],[player2,0])) # winner = player1
# match3 = Match(([player1,0.5],[player2,0.5])) # egalité
# match4 = Match(([player1,0],[player2,0])) # match pas encore joué

round1 = Round(1,[match1,match2,match3,match4])
round2 = Round(2,[match2,match4,match3,match1])


tournament1 = Tournament("Grand tour été 2022", "Cela va être super !!!", 
                         "30-05-2022 14:55:34", "30-05-2022 18:55:34", 
                         "Lyon", 2, 
                         [round1,round2], 
                         [raphael,thea, francis,
                          aloise,gabriel,christine, 
                          flora, stephane],
                         "Bullet")

def main():

    print("########### Joueur1 #############")
    print(raphael)
    # print(random_player1())       
    
    print("########### Match1 #############")    

    
    Match.play_match(match1)
    print(match1)
    

    # print("########### Round1 #############")      
    # print(round1)


    # print("########### Tournoi1 #############")    
    # print(tournament1)
   # print(repr(tournament1))

    # time.sleep(2.5)    
        

if __name__ == "__main__":
    main()
 