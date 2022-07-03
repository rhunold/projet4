import time
import random

from controllers.time import get_timestamp, get_date

from models.player import Player, players
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from views.interface import HomeText, ManageTournamentText, ManagePlayerText, CreatePlayerText, CreateTournamentText, LoadPlayerText, ManageReportText

from views.view import View

from controllers.player_manager import CreatePlayerProcess, ChangePlayerRankProcess, LoadPlayerProcess, PlayerReportProcess
from controllers.tournament_manager import CreateTournamentProcess, LoadTournamentProcess, TournamentReportProcess

## HOME

class Home(View):
    def display(self):    
        user_input = HomeText().display()
        if user_input == "0":
            ManageTournament().display()
        elif user_input == "1":         
            ManagePlayer().display()
            
        elif user_input == "2":
            ManageReport().display()       
        else:   
            quit() 
            
            
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
            
               
            
class ManageReport(View):
    def display(self):     
        user_input = ManageReportText().display()
        
        if user_input == "0":
            TournamentReportProcess.display()
            
        elif user_input == "1":
            PlayerReport().display_by_name()
            # ManageReport().display()            
        elif user_input == "2":
            PlayerReport().display_by_rank()
     
        else:   
            Home().display()              
                       
                     

## PLAYER 
        
class ManagePlayer(View):
    def display(self):     
        user_input = ManagePlayerText().display()
        
        if user_input == "0":
            CreatePlayer().display()  
            
        elif user_input == "1":
            ChangePlayerRank().display()
        else:   
            Home().display()
            
class CreatePlayer(View):
    def display(self):     
        CreatePlayerProcess().display()        
        ManagePlayer().display()
        
        # Home().display()
                 
        
class LoadPlayer(View):
    def display(self):  
        
        # user_input = LoadPlayerText().display()   
        
        # print(user_input)     
        player_loaded = LoadPlayerProcess().display()
        print(f"dans la classe LoadPlayer {player_loaded}")

    
        # if any(players.player_id == player in players for player in players):
        #     print("on a trouvé l'id")
        #     return print(player)
            
        # ManagePlayer().display()   
           
        
        
class ChangePlayerRank(View):
    def display(self):

        player = LoadPlayerProcess().display()
        print(f"dans la classe ChangePlayerRank {player}")
        
        if player is None:
            self.display()
        else:
            


            ChangePlayerRankProcess().display(player)

        ManagePlayer().display()
        

   
                          
## TOURNAMENT


class ManageTournament(View):
    def display(self):     
        user_input = ManageTournamentText().display()
        
        if user_input == "0":
            CreateTournament().display()
            print("Infos du tournois enregistré. MAintenant il faut ajouter des joueurs dans le fichier tournament_manager.py")

        elif user_input == "1":
            LoadTournament().display()
            pass
        else:   
            Home().display()
            
class CreateTournament(View):
    def display(self):     
        CreateTournamentProcess().display()
        
        Home().display()        
        
        
class LoadTournament(View):
    def display(self):     
        LoadTournamentProcess().display() 
        
        Home().display()
        
        
## RAPPORTS
        
class PlayerReport(View):
    def display_by_name(self):
        PlayerReportProcess().display_by_name()
        ManageReport().display()

    def display_by_rank(self):
        PlayerReportProcess().display_by_rank()
        ManageReport().display()        
              


        

            
            
    


        

            
            
