import pygame
import algorithms
import random
from pygame.locals import *
dicoCouleurJoueur = {1:(255,0,0),2:(0,255,0),3:(0,0,255),4:(255,100,0),5:(0,255,100),6:(100,0,255),7:(100,0,100),8:(70,160,30),9:(30,100,200)}


def ChainReaction():

    pygame.init()
    jouer = True


    while jouer:
        maSurface = pygame.display.set_mode((1000, 700))
        totalJoueur, totalColonne, totalLigne = InitGame(maSurface)
        tableau = algorithms.NewBoard(totalLigne, totalColonne)
        GamePlay(maSurface,tableau,totalLigne,totalColonne,totalJoueur)

        fontObj = pygame.font.SysFont('Courier New Normal', 60)
        texteSurface = fontObj.render('Rejouer', True, (255,255,255), None)
        maSurface.blit(texteSurface,(30,100))
        fontObj = pygame.font.SysFont('Courier New Normal', 60)
        texteSurface = fontObj.render('Quit', True, (255, 255, 255), None)
        maSurface.blit(texteSurface, (30, 140))
        pygame.display.update()
        jouer=ChoixReplay(maSurface)



    pygame.quit()





def InitGame(mySurface):
    FPS = 60
    fpsClock = pygame.time.Clock()
    listeParametre = [2,3,3]
    listeJoueur=[]
    tupleParametre = ("Nombre de joueur :    <    {}    >","Nombre de colonne :  <    {}    >",
                      "Nombre de ligne :       <    {}    >","Jouer")
    white=(255,255,255)
    black=(0,0,0)
    continuer = True
    fond = pygame.image.load('backgroundChain.png')

    while continuer:
        mySurface.blit(fond,(0,0))
        sautDeLigne = 300


        for ligne in range(0, len(tupleParametre)):

            if ligne<3:
                fontObj = pygame.font.SysFont('Courier New Normal', 40)
                texteSurface = fontObj.render(tupleParametre[ligne].format(listeParametre[ligne]), True, white, None)
            if ligne == 3:
                fontObj = pygame.font.SysFont('Courier New Normal', 60)
                texteSurface = fontObj.render((tupleParametre[ligne]), True, white, None)
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (300, sautDeLigne)
            sautDeLigne = sautDeLigne + 50
            mySurface.blit(texteSurface, texteRect)
        sautDeLigne = 300
        for event in pygame.event.get() :
            if event.type == QUIT:
                continuer = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0]>590 and event.pos[0]<620 and event.pos[1]>sautDeLigne and event.pos[1]<sautDeLigne+20 and listeParametre[0]>2:
                        listeParametre[0] = listeParametre[0] - 1
                    if event.pos[0]>690 and event.pos[0]<720 and event.pos[1]>sautDeLigne and event.pos[1]<sautDeLigne+20 and listeParametre[0]<8:
                        listeParametre[0] = listeParametre[0] + 1
                    if event.pos[0]>590 and event.pos[0]<620 and event.pos[1]>sautDeLigne+50 and event.pos[1]<sautDeLigne+70 and listeParametre[1]>3:
                        listeParametre[1] = listeParametre[1] - 1
                    if event.pos[0]>690 and event.pos[0]<720 and event.pos[1]>sautDeLigne+50 and event.pos[1]<sautDeLigne+70 and listeParametre[1]<15:
                        listeParametre[1] = listeParametre[1] + 1
                    if event.pos[0]>590 and event.pos[0]<620 and event.pos[1]>sautDeLigne+100 and event.pos[1]<sautDeLigne+120 and listeParametre[2]>3:
                        listeParametre[2] = listeParametre[2] - 1
                    if event.pos[0]>690 and event.pos[0]<720 and event.pos[1]>sautDeLigne+100 and event.pos[1]<sautDeLigne+120 and listeParametre[2]<10:
                        listeParametre[2] = listeParametre[2] + 1
                    if event.pos[0] > 300 and event.pos[0] < 415 and event.pos[1] > sautDeLigne + 150 and event.pos[1] < sautDeLigne + 180:
                        maSurface = pygame.display.set_mode((80*listeParametre[1], 80*listeParametre[2]))


                        return listeParametre[0]*10,listeParametre[1],listeParametre[2]


        pygame.display.update()
    return 0,0,0

def DrawBoard(mySurface,gameBoard,nbLigne,nbColonne,player):


    case=pygame.image.load('case1.png')

    pygame.draw.rect(mySurface,dicoCouleurJoueur[player/10],(0,0,80*nbColonne,80*nbLigne))
    for ligne in range(0,nbLigne):
        for colonne in range (0,nbColonne):
            mySurface.blit(case,(colonne*80,ligne*80))
            if gameBoard[ligne][colonne]//10 != 0:
                drawCell(mySurface,gameBoard,nbLigne,nbColonne,colonne,ligne)



    pygame.display.update()



def drawCell(mySurface,tableau,nbLigne,nbColonne,colonne,ligne):


    ijoueur =tableau [ligne][colonne]//10
    nbpions = tableau[ligne][colonne]%10

    if nbpions == 1:
        pygame.draw.circle(mySurface,dicoCouleurJoueur[ijoueur],(colonne*80+40,ligne*80+40),10)
    elif nbpions == 2:
        pygame.draw.circle(mySurface,dicoCouleurJoueur[ijoueur],(colonne*80+20,ligne*80+20),10)
        pygame.draw.circle(mySurface, dicoCouleurJoueur[ijoueur], (colonne * 80 + 60, ligne * 80 + 60),10)
    elif nbpions == 3:
        pygame.draw.circle(mySurface, dicoCouleurJoueur[ijoueur], (colonne * 80 + 20, ligne * 80 + 20), 10)
        pygame.draw.circle(mySurface, dicoCouleurJoueur[ijoueur], (colonne * 80 + 60, ligne * 80 + 60), 10)
        pygame.draw.circle(mySurface, dicoCouleurJoueur[ijoueur], (colonne * 80 + 40, ligne * 80 + 40), 10)



def ChoixReplay(mySurface):
    choix =False
    while not choix:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x,y=event.pos
                if x>30 and y>100 and y<130:
                    return True
                if x>30 and y>140:
                    return False

def GamePlay(mySurface,gameBoard,nbLigne,nbColonne,nbJoueur):
    win=False
    loose=False
    tour = 1
    player = 10
    while win == False:

        print(nbJoueur)
        if tour == 2:
            loose = algorithms.loose(gameBoard, nbLigne, nbColonne, player)

        if tour == 1 or not loose:
            DrawBoard(mySurface, gameBoard, nbLigne, nbColonne, player)
            ligne, colonne = select(mySurface, gameBoard, nbLigne, nbColonne, player)


            algorithms.Put(gameBoard, nbLigne, nbColonne, ligne, colonne, player)
            if tour == 2:
                win = algorithms.win(gameBoard, nbLigne, nbColonne, player)
                if win :
                    DrawBoard(mySurface, gameBoard, nbLigne, nbColonne, player)
                    fontObj = pygame.font.SysFont('Courier New Normal', int(nbColonne)*10)
                    texteSurface = fontObj.render('Le joueur {} a gagné'.format(player//10), True, (255,255,255),
                                                  None)
                    mySurface.blit(texteSurface,(20,20))
                    pygame.display.update()
                    win=True


        print(gameBoard)
        if player == nbJoueur:
            player = 10
            tour = 2

        else:
            player += 10




def select(mySurface, gameBoard, nbLigne, nbColonne, player):
    FPS = 60
    fpsClock = pygame.time.Clock()
    possible = False

    ligne = 0
    colonne = 0
    while (possible == False):


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                print(x, y)
                ligne = y // 80
                colonne = x // 80
                print(ligne, colonne)
                possible = algorithms.possible(gameBoard, nbLigne, nbColonne, ligne, colonne, player)
        fpsClock.tick(FPS)
    return ligne, colonne


ChainReaction()
