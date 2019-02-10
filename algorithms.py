import pygame
from pygame import  *

def NewBoard (nbLigne,nbColonne):
    tableau = [[0]*nbColonne for i in range (nbLigne)]
    return tableau

def win(tableau, totalLigne,totalColonne,player):

    for ligne in range(0, totalLigne):
        for colonne in range(0, totalColonne):
            if tableau[ligne][colonne]-(tableau[ligne][colonne] % 10) != player and tableau[ligne][colonne] != 0:
                return False

    return True

def loose(tableau, totalLigne,totalColonne,player):

    for ligne in range(0, totalLigne):
        for colonne in range(0, totalColonne):
            if tableau[ligne][colonne]-(tableau[ligne][colonne] % 10) == player and tableau[ligne][colonne] != 0:
                return False

    return True

def Put(gameBoard, nbLigne, nbColonne, i, j, player):

    reaction = 0

    if gameBoard[i][j] == 0:
        gameBoard[i][j] = player+1
    else:
        gameBoard[i][j] += 1
        reaction = 1


    while reaction>0:
        tic = 1
        for ligne in range(0, nbLigne):  ##Calcul reactions
            for colonne in range(0, nbColonne):

                if ligne>0:
                    if ((((ligne == nbLigne-1 and colonne == 0)or (ligne == nbLigne-1 and colonne == nbColonne-1))and gameBoard[ligne][colonne] % 10 >1)or
                            ((ligne == nbLigne - 1 or colonne == 0 or colonne == nbColonne - 1)and gameBoard[ligne][colonne] % 10 > 2 )or gameBoard[ligne][colonne] % 10 > 3):

                        gameBoard[ligne - 1][colonne] = player + (gameBoard[ligne - 1][colonne] % 10) + 1
                        tic = 2
                        reaction = 2

                if ligne<nbLigne-1:
                    if ((((ligne == 0 and colonne == 0)or (ligne == 0 and colonne == nbColonne-1)) and gameBoard[ligne][colonne] % 10 >1)or
                            ((ligne == 0 or colonne == 0 or colonne == nbColonne - 1)and gameBoard[ligne][colonne] % 10 > 2) or gameBoard[ligne][colonne] % 10 > 3):

                        gameBoard[ligne + 1][colonne] = player + (gameBoard[ligne + 1][colonne] % 10) + 1
                        tic = 2
                        reaction = 2

                if colonne>0:
                    if ((((ligne == nbLigne-1 and colonne == nbColonne-1)or (ligne == 0 and colonne == nbColonne-1)) and gameBoard[ligne][colonne] % 10 >1) or
                            ((ligne == 0 or ligne == nbLigne - 1 or colonne == nbColonne - 1)and gameBoard[ligne][colonne] % 10 > 2)or  gameBoard[ligne][colonne] % 10 > 3):

                        gameBoard[ligne][colonne - 1] = player + (gameBoard[ligne][colonne - 1] % 10) + 1
                        tic = 2
                        reaction = 2
                if colonne<nbColonne-1:
                    if ((((ligne == 0 and colonne == 0)or (ligne == nbLigne-1 and colonne == 0)) and gameBoard[ligne][colonne] % 10 >1)or
                            ((ligne == 0 or ligne == nbLigne - 1 or colonne == 0)and gameBoard[ligne][colonne] % 10 > 2) or gameBoard[ligne][colonne] % 10 > 3):

                        gameBoard[ligne][colonne + 1] = player + (gameBoard[ligne][colonne + 1] % 10) + 1
                        tic = 2
                        reaction = 2

                if tic == 2 :

                    gameBoard[ligne][colonne]=0
                    tic = 1
        reaction -=1


def possible(NewBoard, nbLigne, nbColonne, i, j, player):
    # si la case est vide, c'est possible
    if NewBoard[i][j]== 0:
        return True
    else:
        # si la case est occupee avec des pions du joueur player, c'est possible aussi
        if NewBoard[i][j]//10 == player/10:
            return True
        else:
            # sinon la case est forcement occupee par un autre joueur et donc ce n'est possible
            return False










