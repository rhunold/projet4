# Tournois d'échec
Ce programme permet de lancer un tournois d'échecs et utilise le système suisse pour l'organisation des tours.
On peut créer des joueurs, changer leur classement.
On peut charger des joueurs et des tournois à partir d'une bade do de données (TinyDB).




## Créer et installer l'environnement virtuelle
- Clonez le reposotory git dans un dossier local
- Dans votre terminal, allez au dossier local et lancez la commande "python3 -m venv env"
- Dans votre terminal, activez l'environnement virtuelle en lançant la commande "source env/bin/activate"
- Dans votre terminal, lancez la commande "pip install -r requirements.txt"

## Présentation du programme
Le programme se présente comme une suite de menus dans lesquels on demande à l'utilisateur de naviguer ou de fournir des informations pour la création de tournois, de tours, de matchs et de jouers.
Il existe aussi un menu rapports permettant de consulter les informations via différents filtres.


## Lancer le programme
Pour lancer le programme, il faut écrire dans le terminal :
```
python main.py
```

## Arborescence du menu

```
Programme
├── Gestion des tournois
│   ├── Création d'un tournoi
│   └── Chargement d'un tournoi
│
├── Gestion des joueurs
│   ├── Créer un joueur
│   ├── Changer le classement d'un joueur
│
└── Voir les rapports
    ├── Tournois
    │   └── par nom des joueurs
    │   └── par rang des joueurs
    │   └── par tour
    │   └── par match
    │                
    ├── Joueur par odre alphabétique
    └── Joueur par classement
```    

## Flake 8
Flake8 permet de s'assurer que le code respecte la PEP8.


Pour lancer l'outil flake, il faut se positionner dans le dossier du programme et écrire dans le terminal :
```
flake8 --max-line-length 119
```

Pour obtenir un rapport généré en html, il faut utiliser cette commande
```
flake8 --format=html --htmldir=flake8-report
```

A date (03/08/2022), flake8-html ne marche pas avec la dernière version de flak8. J'ai donc utilisé une version plus ancienne.
https://github.com/lordmauve/flake8-html/issues/30

## Liste d'améliorations possibles
- Si on ajoute un joueur à un tournoi, il ne doit plus être possible de le reselectionner dans le même tournoi
- Modifier les autres attributs des joueurs (nom, prénom, date de naissance)
- Supprimer un joueur ou un tournoi.
- Afficher les menus de téléchargement uniquement si des données sont en base.