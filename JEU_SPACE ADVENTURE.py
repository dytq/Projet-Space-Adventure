                ######################PROJET ISN#####################
                #        CONTRIBUTEURS: AMIR; LUCAS; TAARIQ         #
                #                *-Space adventure-*                #
                #   ---------------------------------------------   #
                #####################################################

#importation des modules:
from tkinter import *
from math import *
import random

#Démarage du jeu:
def start(event):
    """Fonction de départ:
        { Cette fonction appelle différentes fonctions qui permmet le démarrage du jeu (chronomètre, actualisation, le démmarage du niveau et la possiblité de faire bouger le vaisseau)
        }
        Elle prend en entré la touche espace et remplace l'image du fond"""
        
    can1.delete(fen1,debut)
    chronometre()
    actualisation()
    niveau_1()
    fin_de_jeu()
    fen1.bind('<Motion>',deplacement_du_vaisseau)
    #fen1.bind('<Button>',tire) non fonctionnelle 
    
#Création du niveau:
def niveau_1():
    """Fonction qui définit le niveau:
        { Cette fonction permet de placer les différents obstacles et ennemis selon un certain temps donnée
        }
    Dans chaque bloc, on a défini les coordonnées des obstacles dans des listes et appellé les fonctions ennemis, obstacle, bonnus"""
    global sec  

    if sec==5:
        """ce bloc contient les coordonées des obstacles, apparition de l'obstacle a 5 seconde"""
        liste1.append(200)  #x1
        liste1.append(100)  #y1
        liste2.append(500)  #x2
        liste2.append(0)    #y2
        obstacle()
        ennemi_E1()
        
    elif sec==8:
        liste1.append(0)
        liste1.append(100)             
        liste2.append(300)
        liste2.append(0)                
        obstacle()
        
    elif sec==10:
        liste1.append(200)
        liste1.append(100)                 
        liste2.append(500)
        liste2.append(0)
        obstacle()
        
    elif sec==12:
        liste1.append(0)
        liste1.append(100)             
        liste2.append(300)
        liste2.append(0)                
        obstacle()

    elif sec==14:
        liste1.append(200)
        liste1.append(100)                 
        liste2.append(500)
        liste2.append(0)
        obstacle()
        
    elif sec==16:
        liste1.append(0)
        liste1.append(100)             
        liste2.append(300)
        liste2.append(0)                
        obstacle()
        
    elif sec==18:
        liste1.append(200)
        liste1.append(100)                 
        liste2.append(500)
        liste2.append(0)            
        obstacle()
        
    elif sec==20:
        bonnus()
        ennemi_E2()
        
    elif sec==25:
        liste1.append(0)
        liste1.append(100)             
        liste2.append(300)
        liste2.append(0)                
        obstacle()
        
    elif sec==29:
        liste1.append(200)
        liste1.append(100)                 
        liste2.append(500)
        liste2.append(0)
        obstacle()
        
    elif sec==32:
        liste1.append(0)
        liste1.append(100)             
        liste2.append(300)
        liste2.append(0)                
        obstacle()
        
    elif sec==35:
        liste1.append(200)
        liste1.append(100)                 
        liste2.append(500)
        liste2.append(0)
        obstacle()
        ennemi_E1()
        
    elif sec==43:
        ennemi_E2()
        ennemi_E1()
        
    else:
        fen1.after(500,niveau_1)

#Les différents obstacles qui défilent dans le jeu:        
def obstacle():
    """Fonction qui fait défiler les obstacles:
    {Cette fonction permet de faire apparaitre les obstacles, ou les coordonnées initiales sont établies par les blocs qui se trouve dans la fonction niveau.
    }
    Cela permet de faire bouger les bloc en incrémentant un 'pas' tout les 25 ms. Elle appelle la fonction collision"""
    
    global dy,a,b #etat initiale, a=0 et b=1

    x3=liste1[a]                
    y3=liste1[b]+dy             
    x4=liste2[a]                
    y4=liste2[b]+dy             

    dy = dy + 10 #dy correspond au 'pas' de descente.

    can1.coords(obstacle1,x3,y3,x4,y4)
    collisions_obstacles(x3,x4,y3,y4) 
    
    if dy>700: #Si l'obstacle dépasse le bas de l'écran, il revient a niveau pour changer les coordonées de l'obstacle
        a=a+2
        b=b+2
        dy=0
        niveau_1()
        
    else:
        fen1.after(25,obstacle) #répète la fonction obstacle toutes les 25 millisecondes

def ennemi_E1():
    """Fonction qui fait défiler l'ennemis rouge:
    {Cette fonction fait défiler l'ennemis de manière transversale puis de manière horizontale au bout d'un certain temps de manière aléatoire
    }
    L'ennemi se déplace toute les 25 ms""" 

    global x_oval,y_oval,e #e designe un nombre aléatoire entre 50 et 450
    
    if x_oval<500:
        x_oval=x_oval+4
        y_oval=y_oval+3
        
    if x_oval>=e:
        x_oval=x_oval-6
        y_oval=y_oval+3
    can1.coords(ennemi_1,x_oval,y_oval)
    
    if y_oval>700:
        e=random.randint(50,450) # redéfinit un nombre aléatoire lors de la prochaine apparation de l'ennmis
        x_oval=-100 #point de retour (en dehors du jeu)
        y_oval=-100 #point de retour (en dehors du jeu)
        niveau_1()
    else:
        fen1.after(25,ennemi_E1)
        
def ennemi_E2():
    """Fonction ennemis orange:
    {Cette fonction fait apparaitre l'ennemis en le faisant défiler de facon ciculaire sur un axe horizontale
    }
    L'ennemis se déplace toute les 100ms."""
    global x_E2,y_E2,cosin
    y_E2=cos(cosin)*50+y_E2+10
    x_E2=sin(cosin)*50+x_E2
    cosin=cosin+1
    can1.coords(ennemi_2,x_E2,y_E2)
    
    if y_E2>700:
        y_E2=-40   #Point de retour (situé en dehors du jeu)
        niveau_1()
    else:
        fen1.after(100,ennemi_E2)   
        
def bonnus():
    """Fonction qui fait défiler le coeur
    {Cette fonction fait défiler le coeur de manière horizontale
    }
    Le coeur se déplace à un pas de 'y_coeur=35' et se réinitialisant après avoir dépassé le bas de l'écran à y=0. Le coeur se déplace toute les 100ms"""
    global y_coeur
    y_coeur=y_coeur+35
    can1.coords(coeur,100,y_coeur)

    if y_coeur>700:
        y_coeur=0
    else:
        fen1.after(100,bonnus)
        
#Gestionnaire de collision: 
def recupvie():
    """Fonction collision entre le vaisseau et le coeur:
    {fonction qui fait que le coeur sur l'écran fasse récupérer 3 points de vie
       quand il entre en contact avec le vaisseau
    }"""
    rayon=60 #rayon de l'objet 
    collision=sqrt(pow(can1.coords(Photo)[0]-can1.coords(coeur)[0],2)+(pow(can1.coords(Photo)[1]-can1.coords(coeur)[1],2)))#on utilise la formule permmetant de calculer la distance entre deux points dans un repère AB=(Xb-Xa)²+(Yb-Ya)² (ici on utilise sqrt(,(racine) et pow(,(puissance)
    if collision < rayon:
        barre_de_vie(-3)
        
       
def collision_ennemis1():
    """Fonction collision entre l'ennemis et le vaisseau:
    {Fonction qui fait perdre 2 points de vie au joueur lorsque le vaisseau touche l'ennemi
    }
    """
    rayon=85 
    collision=sqrt(pow(can1.coords(Photo)[0]-can1.coords(ennemi_1)[0],2)+(pow(can1.coords(Photo)[1]-can1.coords(ennemi_1)[1],2)))
    if collision < rayon:
        barre_de_vie(2)

def collision_ennemis2():
    """Fonction collision entre l'ennemis et le vaisseau:
    {Fonction qui faire perdre 2 points de vie au joueur lorsque le vaisseau touche l'ennemi
    }"""
    rayon=60
    collision=sqrt(pow(can1.coords(Photo)[0]-can1.coords(ennemi_2)[0],2)+(pow(can1.coords(Photo)[1]-can1.coords(ennemi_2)[1],2)))
    if collision < rayon:
        barre_de_vie(2)
        
def collisions_obstacles(x3,x4,y3,y4):
    """Fonction collison entre l'obstacle et le vaisseau:
    """
    if ((can1.coords(Photo)[0]>x3-40)and (can1.coords(Photo)[0]<x4+40 and(can1.coords(Photo)[1]<y3+40) and (can1.coords(Photo)[1]>y4-40))):
        barre_de_vie(1)
        
def collisions_bordure():
    """Fonction qui délimite les bordure""" 
    if (can1.coords(Photo)[0]>450) or (can1.coords(Photo)[0]<50): # a droite 450 et 50 c'est a gauche 
        barre_de_vie(1)
        
def actualisation():
    """Fonction qui permet de démarer la barre de progression et les collisions"""
    barre_de_progression()
    collisions_bordure()
    collision_ennemis1()
    collision_ennemis2()
    recupvie()
   
    fen1.after(50,actualisation)
    
def barre_de_vie(dommage): 
    """fonction de la barre de vie:"""
    global vie
    vie=vie-dommage
    can2.coords(barre,0,25,vie,40) #coordonnées de la part de vie 

def deplacement_du_vaisseau(event):  
    """Fonction du déplacement de l'objet"""
    collision_ennemis1()
    collision_ennemis2()
    can1.coords(Photo,event.x,event.y)  # Recupere les coordonnées de l'image quand la souris bouge ( la photo du vaisseau bouge avec la souris = le vaisseau ) 
    
def fin_de_jeu(): #A
    global vie,sec  # appel vie et la seconde 
    if vie <= 0:
        fen1.destroy()
        fen3=Tk()
        can5=Canvas(fen3,bg='black',width=711,height=574)
        can5.gameover=PhotoImage(file='game_over.gif')
        perdu=can5.create_image(356,287,image=can5.gameover)
        Button(fen3,text='Quitter',command=fen3.destroy).pack(side=BOTTOM)
        can5.pack()       

    elif sec>50:
        fen1.destroy()
        fen4=Tk()
        can6=Canvas(fen4,bg='black',width=593,height=700)
        can6.youwin=PhotoImage(file='you_win.gif')
        gagne=can6.create_image(300,280,image=can6.youwin)
        Button(fen4,text='Quitter',command=fen4.destroy).pack(side=TOP)
        can6.pack()

    else:
         fen1.after(1,fin_de_jeu)  # Attendre et repeter jusqu'a qu'elle soit dans la bonne condition pour se lancer 


#chronometre: 
def chronometre():
    global sec
    sec=sec+1 #1 sec + 1 = 2 
    time['text'] = sec
    fen1.after(1000, chronometre) # 1000 millisecondes = 1 seconde 

#barre de progression: 
def barre_de_progression():
    global sec
    progress=100/50   # 100 = longueur  ;; 50 = le nombre de seconde en tout pour que sa soit plein ( la durée du jeu ) 
    can2.coords(barre2,350,25,350+(sec*progress),40)

"""def tire(event) 
    global x2 , y2
    ty=ty-2    
    can1.coords(shoot,can1.coords(Photo)[0]-10 , can1.coords(Photo)[1]-10+ty ,can1.coords(Photo)[0]+10 , can1.coords(Photo)[1]+10+ty)

    fen1.after(10,tire,event)

    if can1.coords(shoot)[1]<0:
     can1.coords(shoot,x2,y2,x2+10,y2-10)"""

def aide():
    """Fonction aide qui fait apparaitre une fenetre avec du texte expliquant comment jouer"""
    fen5=Tk()
    fen5.geometry("300x80")
    text=Label(fen5,text="Dirigez votre vaisseau à l'aide de la souris \n et frayez-vous un chemin parmi les différents ennemis \n et obstacles qui se dresseront sur votre route !").pack()
    Button(fen5,text='Retour',command=fen5.destroy).pack(side=BOTTOM)



        
#--------------------------Appel des fonctions, coordonées initial, création des Canvas et de la fenetre ------------------------------------#
                        #----------------------------------------------------------------------------#

#les différentes coordonées initiales:

#obstacles:       
dy=0                                 # vitesse des obstacles 
a,b=0,1                              #permet d'appeler les coordonnées obstacles dans les listes

#ennemis:
x_oval,y_oval=0,0
cosin=0
x_E2=250
y_E2=0
e=random.randint(50,450) 

#récupération de la vie
y_coeur=0

#chronometre état intial:
sec = 0 

#niveaux:
liste1=[]                            #obstacles
liste2=[]                            #obstacles
vie=100                              #vie:

#fenêtre et Canvas du jeu:
fen1=Tk()
fen1.title("Jeu")
can1=Canvas(fen1,bg='dark blue', height=600, width=500)
can2=Canvas(fen1,bg='LightGoldenrodYellow',height=50,width=500)# Élément de base de l'interface graphique d'un logiciel  , support de different objet 
fond = PhotoImage(file="fond_image.gif")
can1.create_image(252,352, image=fond)

#création des différents objets et importation des images:

#coeur:
truc=PhotoImage(file='coeur.png')
coeur=can1.create_image(-100,-100, image=truc)
    
#ennemi: 
E1=PhotoImage(file='E1.gif')
ennemi_1=can1.create_image(-100,-100, image =E1)

E2=PhotoImage(file='E2.gif')
ennemi_2=can1.create_image(250,-40, image=E2)

#Time 
time = Label(fen1, fg='green')
time.pack(side=TOP)

#tir:
shoot=can1.create_oval(500,0,0,0,width=2,fill='red')

#obstacle:
obstacle1 = can1.create_rectangle(0,0,0,0, width=5,fill='light grey',outline='grey', tags='gris')

#écran départ
depart=PhotoImage(file='ecran_depart.gif')
debut=can1.create_image(250,320,image=depart)
fen1.bind('<space>',start)

#création d'une barre de vie: 
can2.create_text(30,12, text="VIE",font="Elephant 12",fill="black")
barre=can2.create_rectangle(0,25,vie,40,fill='red')

#barre_de_progression:
can2.create_text(400,12, text="BARRE DE PROGRESSION",font="Elephant 8",fill="black")
can2.create_rectangle(350,25,450,40)
barre2 = can2.create_rectangle(350,25,350,40,fill='blue')

#vaisseau:
vaisseau1 = PhotoImage(file ='vaisseau.gif')
Photo= can1.create_image(250,500, image=vaisseau1)

#création des boutons: 
Frame1 = Frame(fen1, borderwidth=2,relief=GROOVE) 
Frame1.pack(side=TOP)
Button(Frame1,text='Quitter',command=fen1.destroy).pack(side=RIGHT)
Button(Frame1,text='Aide',command=aide).pack(side=RIGHT)

#position des Canvas: 
can1.pack(side=TOP)
can2.pack(side=BOTTOM)

#démarrage du réceptionnaire d'évènements (boucle principale) :  
fen1.mainloop()