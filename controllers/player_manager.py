import time
import random

from models.player import Player, players

from controllers.time import get_timestamp




player = Player()

class CreatePlayer:
    # Instanciation Joueur    
    
    
    # first_name = input("Prénom du joueur : ")   
    first_name = "Raphael"  
    player.first_name = first_name    
    
    # name = input("Nom du joueur : ")
    name = "Hunold"  
    player.name = name
  
    
    # birthdate = input("Date de naissance du joueur : ")
    birthdate = "03-04-1977"    
    player.birthdate = birthdate
    
    # rank = int(input("Classment du joueur : ")) 
    rank = 1
    
    player.rank = rank

    # sex = input("Sexe du joueur : ")   
    sex = "H"    
    player.sex = sex
    
    player_id = player.player_id
    
    player_score = 0

    players.append(player) # Ajout à la liste des joueurs
    
    # On enregistre le joueur dans le json
    player.save(player_id, name, first_name, birthdate, sex, rank, player_score)
    
    # time.sleep(1)   
    
class ChangePlayerRank:
    
    # on doit connaitre l'id du joueur dont on veut changer le classement.
    player.player_id = input("Quel est l'identifiant du joueur dont vous voulez changer le classement ?")
    
    rank = int(input("Nouveau classement du joueur : ")) 
    player.rank = rank     
    
    # On enregistre le joueur dans les 2 json (player et tournois en cours ? ) Juste dans le player pour le moment.
    player.update_rank(player.player_id)    

    