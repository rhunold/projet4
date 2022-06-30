import time
import random

from controllers.time import get_timestamp, get_date

from models.player import Player, players
from models.match import Match
from models.tour import Tour
from models.tournament import Tournament

from views.interface import HomeText, ManageTournamentText, ManagePlayerText, CreatePlayerText, CreateTournamentText, LoadPlayerText
from views.view import View

from controllers.player_manager import CreatePlayerProcess, ChangePlayerRankProcess, LoadPlayerProcess
from controllers.tournament_manager import CreateTournamentProcess, LoadTournamentProcess


class Home(View):
    def display(self):    
        user_input = HomeText().display()
        
        if user_input == "0":
            ManageTournament().display()
        elif user_input == "1":         
            ManagePlayer().display()
        elif user_input == "2":
            pass
            # ViewReports        
        else:   
            quit()             
    

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
        
        
class ManagePlayer(View):
    def display(self):     
        user_input = ManagePlayerText().display()
        
        if user_input == "0":
            CreatePlayer().display()  
        elif user_input == "1":
            LoadPlayer().display()
        elif user_input == "2":
            ChangePlayerRank().display()
        else:   
            Home().display()              

class CreatePlayer(View):
    def display(self):     
        CreatePlayerProcess().display()        
        # ManagePlayer().display()
        
        Home().display()   
        
        
class CreateTournament(View):
    def display(self):     
        CreateTournamentProcess().display()
        
        
class LoadTournament(View):
    def display(self):     
        LoadTournamentProcess().display()     

        
        
class LoadPlayer(View):
    def display(self):     
        LoadPlayerProcess().display()
        
        
class ChangePlayerRank(View):
    def display(self):
        LoadPlayerProcess().display()         
        ChangePlayerRankProcess().display()           
      
        

            
            
