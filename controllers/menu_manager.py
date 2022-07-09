import time
import random

from controllers.time import get_timestamp, get_date

from models.player import Player
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from views.interface import HomeText, ManageTournamentText, ManagePlayerText, CreatePlayerText, CreateTournamentText, LoadPlayerText, ManageReportText, ManageTournamentReportText

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
        LoadPlayerProcess().display()

    

# Ne pas afficher si pas de joueur dans la bd
class ChangePlayerRank(View):
    def display(self):

        player = LoadPlayerProcess().ask_player_id()
        ChangePlayerRankProcess().display(player)
        ManagePlayer().display()
        

   
                          
## TOURNAMENT


class ManageTournament(View):
    def display(self):     
        user_input = ManageTournamentText().display()
        
        if user_input == "0":
            CreateTournament().display()
            print("Infos du tournois enregistré. Maintenant il faut ajouter des joueurs dans le fichier tournament_manager.py")

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
        LoadTournamentProcess().ask_tournament_id()
        

      
                  
                
## RAPPORTS

class ManageReport(View):
    def display(self):     
        user_input = ManageReportText().display()
        
        if user_input == "0":
            ManageTournamentReport().display()
            
        elif user_input == "1":
            PlayerReport().display_by_name()
            # ManageReport().display()            
        elif user_input == "2":
            PlayerReport().display_by_rank()
        else:   
            Home().display()     
        
class PlayerReport(View):
    def display_by_name(self):
        PlayerReportProcess().display_by_name()
        ManageReport().display()

    def display_by_rank(self):
        PlayerReportProcess().display_by_rank()
        ManageReport().display()        
        
        
class ManageTournamentReport(View):  
    def display(self):
    
        tournament = LoadTournamentProcess().ask_tournament_id()
        
        user_input = ManageTournamentReportText().display()
                
        if user_input == "0":
            TournamentReportProcess().display_by_player_name(tournament)
            ManageReport().display() 
        elif user_input == "1":
            TournamentReportProcess().display_by_player_rank(tournament)
            ManageReport().display()  
        elif user_input == "2":
            TournamentReportProcess().display_by_tours(tournament)
            ManageReport().display()  
        elif user_input == "3":
            TournamentReportProcess().display_by_matchs(tournament)            
            ManageReport().display()  
        else:   
            Home().display()     
     
   

        

            
            
    


        

            
            
