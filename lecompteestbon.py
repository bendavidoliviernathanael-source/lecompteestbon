#!/usr/bin/python3
from math import *
import doctest
import time
import tkinter as tk
from tkinter import messagebox, simpledialog


# ==========================
# CALCULS ET SÉQUENCES DE CALCULS
# ==========================

def copierCalcul(calcul,sequence):
 """
 Copie d'un calcul dans une séquence réceptacle

 Requis : 
 -calcul --> un calcul
 ex : [1,2,"+"]
 
 -sequence --> une séquence
 ex : []

 Fourni : 
 
 >>> copierCalcul([1,2,"+"], [])
 
 """
 sequence.clear
 cpt=0
 while(cpt<len(calcul)):
  sequence.append(calcul[cpt])
  cpt=cpt+1

def copierSequenceCalculs(sequenceCalculs,sequence):
 """
 Copie d'une séquence de calculs dans une séquence réceptacle

 Requis : 
 -sequenceCalculs --> une séquence de calculs
 ex : [[1,2,"+"],[5,9,"+"]]
 
 -sequence --> une séquence
 ex : []

 Fourni : 
 
 >>> copierSequenceCalculs([[1,2,"+"]], [])
 
 """
 sequence.clear()
 cpt=0
 while(cpt<len(sequenceCalculs)):
  calcul=[]
  copierCalcul(sequenceCalculs[cpt],calcul)
  sequence.append(calcul)
  cpt=cpt+1
 
def copierSequenceNombres(sequenceNombres,sequence):
 """
 Copie d'une séquence de nombres dans une séquence réceptacle

 Requis : 
 -sequenceNombres --> une séquence de nombres
 ex : [1,2,5,9]
 
 -sequence --> une séquence
 ex : []

 Fourni : 
 
 >>> copierSequenceNombres([1,2], [])
 
 """
 sequence.clear()
 cpt=0
 while(cpt<len(sequenceNombres)):
  sequence.append(sequenceNombres[cpt])
  cpt=cpt+1

def listerCalculsElaborablesAvecDeuxDesNombresDuneCollection(collectionNombres):
 """
 Énumération des calculs élaborables avec deux des nombres d'une collection de nombres

 Requis : 
 -collectionNombres --> une collection de nombres
 ex : [1,2,3,4,5,6]

 Fourni : 
 -une collection de calculs
 ex: [[1,2,"+"],[1,2,"x"], ... ,[6,1,"+"],[6,1,"-"],[6,1,"*"],[6,1,"/"], ... ,[6,5,"+"],[6,5,"-"],[6,5,"*"]]

 >>> listerCalculsElaborablesAvecDeuxDesNombresDuneCollection([1,1])
 [[1, 1, '+'], [1, 1, '-'], [1, 1, '*'], [1, 1, '/'], [1, 1, '+'], [1, 1, '-'], [1, 1, '*'], [1, 1, '/']]
 """
 res=[]
 cpt=0
 while (cpt<len(collectionNombres)):
  operande1=collectionNombres[cpt]
  nombresRestants = []
  copierSequenceNombres(collectionNombres, nombresRestants)
  nombresRestants.remove(operande1)
  cpt2=0
  while (cpt2<len(nombresRestants)):
   operande2=nombresRestants[cpt2]
   #addition
   res.append([operande1,operande2,"+"])
   #soustraction
   if(operande1>operande2 or operande1==operande2):
    res.append([operande1,operande2,"-"])
   #multiplication  
   res.append([operande1,operande2,"*"])
   #division
   if(operande2!=0):
    if(operande1>operande2 or operande1==operande2):
     if(operande1%operande2 == 0) :
      res.append([operande1,operande2,"/"])
   cpt2 = cpt2 + 1
  cpt = cpt + 1
 return res 

def realiserCalcul(calcul):
 """
 Réalisation d'un calcul

 Requis : 
 -calcul --> un calcul
 ex : [1,2,'+']

 Fourni : 
 -un nombre
 ex : 3

 >>> realiserCalcul([1,2,'+'])
 3
 """
 res = -1
 operande1, operande2, operateur = calcul
 if(operateur=='+') : return operande1+operande2
 if(calcul[2]=='-') : return operande1-operande2
 if(calcul[2]=='*') : return operande1*operande2
 if(calcul[2]=='/') : return int(operande1/operande2)  
 return res  

def listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux, sequenceCalculs):
 """
 Énumération des nombres disponibles après avoir réalisé une séquence de calculs

 Requis : 
 -collectionNombresInitiaux --> une collection de nombres
 ex : [1,2,3,4,5,6]
 -sequenceCalculs --> une séquence de calculs
 ex : [[1,2,"+"],[3,3,"+"]]
 
 Fourni : 
 -une collection de nombres
 ex: [4, 5, 6, 6]

 >>> listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs([1,2,3,4,5,6], [[1,2,"+"],[3,3,"+"]])
 [4, 5, 6, 6]
 """
 res = []
 copierSequenceNombres(collectionNombresInitiaux, res)
 cpt=0
 while(cpt<len(sequenceCalculs)):
  calcul=sequenceCalculs[cpt]
  res.remove(calcul[0])
  res.remove(calcul[1])
  res.append(realiserCalcul(calcul))
  cpt=cpt+1
 return res  


# ==========================
# INDIQUER LES SÉQUENCES SOLUTIONS
# ==========================

def listerSequencesSolutions(sequence, collectionNombresInitiaux, resultatCible):
 """
 Énumération des séquences de calculs élaborables en agrandissant une séquence élaborée avec une collection de nombres initiaux dont le dernier calcul a pour résultat un résultat choisi

 Requis :
 -sequence --> une sequence de calculs
 ex : [[1,1,"+"],[1,2,"+"]]
 -collectionNombresInitiaux --> une collection de nombres
 ex : [1,2,3,4,5,6]
 -resultatCible --> un nombre
 ex : 2, 3 
 
 Fourni : 
 -une collection de sequences de calculs
 ex: [[[1,1,"+"],[1,2,"+"]], [[1,1,"+"],[2,1,"+"]], [[1,1,"/"],[1,1,"+"],[1,2,"+"]]]

 >>> listerSequencesSolutions([], [1,2,3], 3)
 [[[1, 2, '+']], [[1, 3, '*']], [[2, 1, '+']], [[2, 1, '-'], [3, 1, '*']], [[2, 1, '-'], [3, 1, '/']], [[2, 1, '-'], [1, 3, '*']], [[3, 1, '*']], [[3, 1, '/']]]
 """
 res = []
 collectionNombresDisponibles = listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux,sequence)
 extensions = listerCalculsElaborablesAvecDeuxDesNombresDuneCollection(collectionNombresDisponibles)
 cpt = 0
 while(cpt<len(extensions)):
  sequenceAgrandie = []
  copierSequenceCalculs(sequence,sequenceAgrandie)
  sequenceAgrandie.append(extensions[cpt])
  estSolution = realiserCalcul(sequenceAgrandie[len(sequenceAgrandie)-1]) == resultatCible
  estExtensible = len(listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux,sequenceAgrandie))>1
  if(estSolution == True) :
   res.append(sequenceAgrandie)
  if(estExtensible == True): 
   res.extend(listerSequencesSolutions(sequenceAgrandie, collectionNombresInitiaux, resultatCible))
  
  cpt=cpt+1
 
 return res  

# ==========================
# INDIQUER UNE SÉQUENCE SOLUTION
# ==========================

def indiquerUneSequenceSolutionParExtensionDuneSequence(sequence, collectionNombresInitiaux, resultatCible):
 """
 Indication d'une séquence de calculs élaborable en agrandissant une séquence élaborée avec une collection de nombres initiaux dont le dernier calcul a pour résultat un résultat choisi

 Requis :
 -sequence --> une sequence de calculs
 ex : [[1,1,"+"],[1,2,"+"]]
 -collectionNombresInitiaux --> une collection de nombres
 ex : [1,2,3,4,5,6]
 -resultatCible --> un nombre
 ex : 2, 3 
 
 Fourni : 
 -une sequence de calcul
 ex: [[[1,1,"+"],[1,2,"+"]], [[1,1,"+"],[2,1,"+"]], [[1,1,"/"],[1,1,"+"],[1,2,"+"]]]

 >>> indiquerUneSequenceSolutionParExtensionDuneSequence([[1, 1, '+']], [1,1,1], 3)
 [[1, 1, '+'], [1, 2, '+']]
 """
 res = []
 collectionNombresDisponibles = listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux,sequence)
 extensions = listerCalculsElaborablesAvecDeuxDesNombresDuneCollection(collectionNombresDisponibles)
 cpt = 0
 while(cpt<len(extensions)):
  sequenceAgrandie=sequence
  sequenceAgrandie.append(extensions[cpt])
  
  estSolution = realiserCalcul(sequenceAgrandie[len(sequenceAgrandie)-1]) == resultatCible
  estExtensible =len(sequenceAgrandie)<5
  
  if(estSolution == True) :
   res=sequenceAgrandie
   return res
  if(estExtensible == True and len(res)==0): 
   res.extend(indiquerUneSequenceSolutionParExtensionDuneSequence(sequenceAgrandie, collectionNombresInitiaux, resultatCible))
   if(len(res)>0):
    return res
  
  sequenceAgrandie.pop() 
  cpt=cpt+1
 
 return res  

def compterSequencesCalculsElaborablesParExtensionDuneSequence(collectionNombresInitiaux, sequence):
 """
 Comptabilisation des séquences de calculs élaborables avec une collection de nombres initiaux.

 Requis : 
 -collectionNombresInitiaux --> une collection de nombres
 ex : [1,2,3,4,5,6]
 
 Fourni : 
 -une quantité de sequences de calculs
 ex: 1, 10, 12654

 >>> compterSequencesCalculsElaborablesParExtensionDuneSequence([1,1,1],[])
 186
 """
 res = 0
 collectionNombresDisponibles = listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux,sequence)
 extensions = listerCalculsElaborablesAvecDeuxDesNombresDuneCollection(collectionNombresDisponibles)
 cpt = 0
 while(cpt<len(extensions)):
  sequenceAgrandie=sequence
  sequenceAgrandie.append(extensions[cpt])
  res=res+1
  
  estExtensible =len(sequenceAgrandie)<(len(collectionNombresInitiaux)-1)
  if(estExtensible == True): 
   res=res + compterSequencesCalculsElaborablesParExtensionDuneSequence(collectionNombresInitiaux, sequenceAgrandie)
  
  sequenceAgrandie.pop() 
  cpt=cpt+1
 
 return res 


def indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence(sequence, sequenceApprochee, collectionNombresInitiaux, resultatCible):
 """
 Indication d'une séquence de calculs élaborable en agrandissant une séquence élaborée avec une collection de nombres initiaux dont le dernier calcul a pour résultat un résultat choisi ou un résultat à un environ de ce résultat choisi

 Requis :
 -sequence --> une sequence de calculs
 ex : [[1,1,"+"],[1,2,"+"]]
 -sequenceApprochee --> une sequence de calculs
 ex : [[1,1,"+"],[1,2,"+"]]
 -collectionNombresInitiaux --> une collection de nombres
 ex : [1,2,3,4,5,6]
 -resultatCible --> un nombre
 ex : 2, 3 
 
 Fourni : 
 -une sequence de calcul
 ex: [[[1,1,"+"],[1,2,"+"]], [[1,1,"+"],[2,1,"+"]], [[1,1,"/"],[1,1,"+"],[1,2,"+"]]]

 >>> indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([], [], [1,1,1], 3)
 [[1, 1, '+'], [1, 2, '+']]
 """
 res = []
 collectionNombresDisponibles = listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux,sequence)
 extensions = listerCalculsElaborablesAvecDeuxDesNombresDuneCollection(collectionNombresDisponibles)
 cpt = 0
 
 if(len(sequenceApprochee)==0):
  copierSequenceCalculs([extensions[0]],sequenceApprochee)
  res=sequenceApprochee
 
 while(cpt<len(extensions)):
  sequenceAgrandie=sequence
  sequenceAgrandie.append(extensions[cpt]) 
  
  sequenceAgrandieEstExtensible =len(sequenceAgrandie)<(len(collectionNombresInitiaux)-1)
  
  ecartEntreresultatCibleEtSequenceAgrandie = abs(resultatCible - realiserCalcul(sequenceAgrandie[len(sequenceAgrandie)-1]))
  ecartEntreresultatCibleEtSequenceApprochee = abs(resultatCible - realiserCalcul(sequenceApprochee[len(sequenceApprochee)-1]))
  
  #sequenceAgrandieEstPlusProcheQueSequenceApprochee = int(min(ecartEntreresultatCibleEtSequenceAgrandie,  ecartEntreresultatCibleEtSequenceApprochee)) == int(ecartEntreresultatCibleEtSequenceAgrandie)
  sequenceAgrandieEstPlusProcheQueSequenceApprochee = int(ecartEntreresultatCibleEtSequenceAgrandie) < int(ecartEntreresultatCibleEtSequenceApprochee)

  if(sequenceAgrandieEstPlusProcheQueSequenceApprochee == True):
   copierSequenceCalculs(sequenceAgrandie,sequenceApprochee)
  
  if(sequenceAgrandieEstExtensible == True): 
   indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence(sequenceAgrandie, sequenceApprochee, collectionNombresInitiaux, resultatCible)
    
  sequenceAgrandie.pop() 
  cpt=cpt+1
  
 res=sequenceApprochee  
 return res  








# ==========================
# INTERFACE GRAPHIQUE
# ==========================



def fournirUneInterface():
 fenetre = tk.Tk()
 fenetre.title("Approches relatives au jeu le compte est bon")
 fenetre.minsize(500,300)

 tk.Label(fenetre, text="Nombres (séparés par des virgules) :").pack()
 valeurInitialeZoneSaisieCollectionNombresInitiaux = tk.StringVar()
 valeurInitialeZoneSaisieCollectionNombresInitiaux.set("1,2,3")
 zoneSaisieCollectionNombresInitiaux = tk.Entry(fenetre,textvariable=valeurInitialeZoneSaisieCollectionNombresInitiaux, width=30)
 
 zoneSaisieCollectionNombresInitiaux.pack()

 tk.Label(fenetre, text="Résultat cible :").pack()
 valeurInitialeZoneSaisieResultatCible = tk.StringVar()
 valeurInitialeZoneSaisieResultatCible.set("12")
 zoneSaisieResultatCible = tk.Entry(fenetre,textvariable= valeurInitialeZoneSaisieResultatCible, width=30)
 zoneSaisieResultatCible.pack()


 def indiquerSolutionExacteOuApprochee():
        try:
            collectionNombresInitiaux = list(map(int, zoneSaisieCollectionNombresInitiaux.get().split(",")))
            resultatCible = int(zoneSaisieResultatCible.get())
            debut = time.time()
            resultat = indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([], [], collectionNombresInitiaux, resultatCible)
            duree = time.time() - debut
            texteResultat = str(resultat)+"\n"+ "durée : "+str(duree)+" seconde(s)"
            messagebox.showinfo("Résultat",texteResultat)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

 bouton = tk.Button(fenetre, text="Chercher une solution exacte ou approchée", command=indiquerSolutionExacteOuApprochee)
 bouton.pack(pady=5)
 
 def indiquerSolution():
        try:
            collectionNombresInitiaux = list(map(int, zoneSaisieCollectionNombresInitiaux.get().split(",")))
            resultatCible = int(zoneSaisieResultatCible.get())
            debut = time.time()
            resultat = indiquerUneSequenceSolutionParExtensionDuneSequence([], collectionNombresInitiaux, resultatCible)
            duree = time.time() - debut
            texteResultat = str(resultat)+"\n"+ "durée : "+str(duree)+" seconde(s)"
            messagebox.showinfo("Résultat",texteResultat)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

 bouton = tk.Button(fenetre, text="Chercher une solution", command=indiquerSolution)
 bouton.pack(pady=5)
 
 def indiquerSolutions():
        try:
            collectionNombresInitiaux = list(map(int, zoneSaisieCollectionNombresInitiaux.get().split(",")))
            resultatCible = int(zoneSaisieResultatCible.get())
            debut = time.time()
            resultat = listerSequencesSolutions([], collectionNombresInitiaux, resultatCible)
            duree = time.time() - debut
            texteResultat = str(resultat)+"\n"+ "durée : "+str(duree)+" seconde(s)"
            messagebox.showinfo("Résultat",texteResultat)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

 bouton = tk.Button(fenetre, text="Chercher les solutions", command=indiquerSolutions)
 bouton.pack(pady=5)
 
 def compterSequencesCalculsElaborables():
        try:
            collectionNombresInitiaux = list(map(int, zoneSaisieCollectionNombresInitiaux.get().split(",")))
            resultatCible = int(zoneSaisieResultatCible.get())
            debut = time.time()
            resultat = compterSequencesCalculsElaborablesParExtensionDuneSequence(collectionNombresInitiaux, [])
            duree = time.time() - debut
            texteResultat = str(resultat)+"\n"+ "durée : "+str(duree)+" seconde(s)"
            messagebox.showinfo("Résultat",texteResultat)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

 bouton = tk.Button(fenetre, text="Compter les séquences de calculs élaborables", command=compterSequencesCalculsElaborables)
 bouton.pack(pady=5)
 
 
 

 fenetre.mainloop()



# ==========================
# DEMANDES DE RÉALISATIONS D'ALGORITHMES
# ==========================

#utilisation de la méthode indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence(sequence, sequenceApprochee, collectionNombresInitiaux, resultatCible)
collectionNombresInitiaux= [1,1,1,1]
resultatCible = 1080
start = time.time()
res = indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],[],collectionNombresInitiaux, resultatCible)
duree = time.time() - start
print("durée indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],collectionNombresInitiaux, resultatCible) : "+ str(duree) + " seconde(s)")
print("résultat indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],collectionNombresInitiaux, resultatCible) : "+str(res))


fournirUneInterface()








if __name__ == "__main__":
 doctest.testmod()

