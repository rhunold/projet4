from models.player import Player
# from models.match import Match
# from models.tour import Tour
# from models.tournament import Tournament


raphael = Player(1,"hunold","raphael","04-04-1977","Homme",1, 0)
thea = Player(2,"Hunold","Théa","14-06-2015","Femme",5, 0)
gabriel = Player(3,"Hunold","Gabriel","11-07-1978","Homme",6, 0)
aloise = Player(4,"Hunold","Aloise","31-01-1980","Femme",7, 0)
francis = Player(5,"Hunold","Francis","12-12-1943","Homme",2, 0)
flora = Player(6,"Hunold","Flora","12-08-1980","Femme",10, 0)
christine = Player(7,"Hunold","Christine","12-12-1953","Femme",10, 0)
stephane = Player(8,"Hunold","Stephane","12-12-1973","Homme",9, 0)

# list_participants = [] # liste des joueurs du tournoi

list_players = [raphael, thea, gabriel, aloise, francis, flora, christine, stephane] # liste de tous les joueurs


# match0 = Match((raphael,thea))
# match1 = Match((gabriel,aloise))
# match2 = Match((francis,flora))
# match3 = Match((christine,stephane))

# list_matchs = [match0, match1, match2, match3]

# tour = Tour(1,[match, match])
# tour0 = Tour(1,[match0,match1,match2,match3])
# tour1 = Tour(1,[match0,match1,match2,match3])
# tour2 = Tour(2,[match2,match0,match3,match1])
# tour3 = Tour(2,[match2,match0,match3,match1])


# list_tours = [tour0, tour1, tour2, tour3]
# list_tours = []

# scores = ([player1, score_player1], [player2, score_player2])

# tournament = Tournament("Grand tournoi rentrée 2022", "Welcome !!!", 
#                          "30-09-2022 14:55:34", "Pas encore terminé", 
#                          "Lyon", 2, "Bullet", list_tours, list_players)


# tournament = Tournament("Grand tour été 2022", "Cela va être super !!!", 
#                          "30-05-2022 14:55:34", "Pas encore terminé", 
#                          "Lyon", 2, 
#                          [Tour(1,[Match(([Player(1,"hunold","raphael","04-04-1977","Homme",1, 0), 1],
#                                         [Player(2,"Hunold","Théa","14-06-2015","Femme",5, 0), 0])),
#                                   Match(([Player(3,"Hunold","Gabriel","11-07-1978","Homme",6, 0), 1],
#                                         [Player(4,"Hunold","Aloise","31-01-1980","Femme",7, 0), 0])),
#                                   Match(([Player(5,"Hunold","Francis","12-12-1943","Homme",2, 0), 1],
#                                         [Player(6,"Hunold","Flora","12-08-1980","Femme",10, 0), 0])),
#                                   Match(([Player(7,"Hunold","Christine","12-12-1953","Femme",10, 0), 1],
#                                         [Player(8,"Hunold","Stephane","12-12-1973","Homme",9, 0), 0]))
#                                   ]),
#                           Tour(2,[Match(([Player(1,"hunold","raphael","04-04-1977","Homme",1, 1), 1],
#                                         [Player(2,"Hunold","Théa","14-06-2015","Femme",5, 0), 0])),
#                                   Match(([Player(3,"Hunold","Gabriel","11-07-1978","Homme",6, 1), 1],
#                                         [Player(4,"Hunold","Aloise","31-01-1980","Femme",7, 0), 0])),
#                                   Match(([Player(5,"Hunold","Francis","12-12-1943","Homme",2, 1), 1],
#                                         [Player(6,"Hunold","Flora","12-08-1980","Femme",10, 0), 0])),
#                                   Match(([Player(7,"Hunold","Christine","12-12-1953","Femme",10, 1), 1],
#                                         [Player(8,"Hunold","Stephane","12-12-1973","Homme",9, 0), 0]))
#                                   ])
#                           ],
#                          [Player(1,"hunold","raphael","04-04-1977","Homme",1),
#                           Player(2,"Hunold","Théa","14-06-2015","Femme",5),
#                           Player(3,"Hunold","Gabriel","11-07-1978","Homme",6),
#                           Player(4,"Hunold","Aloise","31-01-1980","Femme",7),
#                           Player(5,"Hunold","Francis","12-12-1943","Homme",2),
#                           Player(6,"Hunold","Flora","12-08-1980","Femme",10),
#                           Player(8,"Hunold","Stephane","12-12-1973","Homme",9)],
#                          "Bullet")



# tournament = Tournament("Grand tour été 2022", "Cela va être super !!!", 
#                          "30-05-2022 14:55:34", "Pas encore terminé", 
#                          "Lyon", 2, 
#                          [tour0,tour1], 
#                          [raphael, thea, gabriel, aloise, francis, flora, christine, stephane],
#                          "Bullet")



# tournament_empty_list_tours = Tournament("Grand tournoi rentrée 2022", "Welcome !!!", 
#                          "30-09-2022 14:55:34", "Pas encore terminé", 
#                          "Lyon", 2, list_tours, list_players, "Bullet")
