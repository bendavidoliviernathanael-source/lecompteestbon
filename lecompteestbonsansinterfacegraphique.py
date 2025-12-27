#!/usr/bin/python3
from math import *
import doctest
import time

# ==========================
# SÉQUENCES DE NOMBRES, CALCULS ET SÉQUENCES DE CALCULS
# ==========================

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


def obtenirUneDescriptionDuneSolution(solution, collectionNombresInitiaux, resultatCible):
 """
 Production d'une description d'une solution

 Requis :
 -solution --> une sequence de calculs
 ex : [[1,1,"+"],[1,2,"+"]]
 -collectionNombresInitiaux --> une collection de nombres
 ex : [1,1,1]
 
 Fourni : 
 -une chaîne de caractères décrivant la solution
 ex: "[[1,1,"+"],[1,2,"+"]]"

 >>> obtenirUneDescriptionDuneSolution([[1,1,"+"],[1,2,"+"]], [1,1,1],4)
 "résultat cible : 4 nombres disponibles : [1, 1, 1] sequence de calculs : []\\nrésultat cible : 4 calcul ajouté : 1+1=2 nombres disponibles : [1, 2] sequence de calculs : [[1, 1, '+']]\\nrésultat cible : 4 calcul ajouté : 1+2=3 nombres disponibles : [3] sequence de calculs : [[1, 1, '+'], [1, 2, '+']]\\n"
 """ 
 res=""
 res=res+"résultat cible : "+str(resultatCible)+" nombres disponibles : "+str(collectionNombresInitiaux)+" sequence de calculs : []\n"
 sequenceCalculs=[]
 cpt=0
 while(cpt<len(solution)):
  calcul=[]
  copierCalcul(solution[cpt], calcul)
  sequenceCalculs.append(calcul)
  collectionNombres = listerNombresDisponiblesApresUneRealisationDuneSequenceDeCalculs(collectionNombresInitiaux, sequenceCalculs)
  res=res+"résultat cible : "+str(resultatCible)+" calcul ajouté : "+str(calcul[0])+calcul[2]+str(calcul[1])+"="+str(realiserCalcul(calcul))+" nombres disponibles : "+str(collectionNombres)+" sequence de calculs : "+str(sequenceCalculs) + "\n"  
  cpt=cpt+1
 return res


# ==========================
# CHERCHER DES SOLUTIONS
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
  estExtensible =len(sequenceAgrandie)<(len(collectionNombresInitiaux)-1)
  
  if(estSolution == True) :
   res=sequenceAgrandie
   return res
  if(estExtensible == True): 
   indiquerUneSequenceSolutionParExtensionDuneSequence(sequenceAgrandie, collectionNombresInitiaux, resultatCible)
  
  sequenceAgrandie.pop() 
  cpt=cpt+1
 
 return res  


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
  sequenceAgrandie=sequence
  sequenceAgrandie.append(extensions[cpt])

  estSolution = realiserCalcul(sequenceAgrandie[len(sequenceAgrandie)-1]) == resultatCible
  estExtensible =len(sequenceAgrandie)<(len(collectionNombresInitiaux)-1)
  if(estSolution == True) :
   solution=[]
   copierSequenceCalculs(sequenceAgrandie,solution)
   res.append(solution)
  if(estExtensible == True): 
   res.extend(listerSequencesSolutions(sequenceAgrandie, collectionNombresInitiaux, resultatCible))
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
  
  estExtensible =len(sequenceAgrandie)<(len(collectionNombresInitiaux)-1)
  
  ecartEntreresultatCibleEtSequenceAgrandie = abs(resultatCible - realiserCalcul(sequenceAgrandie[len(sequenceAgrandie)-1]))
  ecartEntreresultatCibleEtSequenceApprochee = abs(resultatCible - realiserCalcul(sequenceApprochee[len(sequenceApprochee)-1]))
  
  #sequenceAgrandieEstPlusProcheQueSequenceApprochee = int(min(ecartEntreresultatCibleEtSequenceAgrandie,  ecartEntreresultatCibleEtSequenceApprochee)) == int(ecartEntreresultatCibleEtSequenceAgrandie)
  sequenceAgrandieEstPlusProcheQueSequenceApprochee = int(ecartEntreresultatCibleEtSequenceAgrandie) < int(ecartEntreresultatCibleEtSequenceApprochee)

  if(sequenceAgrandieEstPlusProcheQueSequenceApprochee == True):
   copierSequenceCalculs(sequenceAgrandie,sequenceApprochee)
  
  if(estExtensible == True): 
   indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence(sequenceAgrandie, sequenceApprochee, collectionNombresInitiaux, resultatCible)
    
  sequenceAgrandie.pop() 
  cpt=cpt+1
  
 res=sequenceApprochee  
 return res  













# ==========================
# DEMANDES DE RÉALISATIONS D'ALGORITHMES
# ==========================

#utilisation de la méthode indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence(sequence, sequenceApprochee, collectionNombresInitiaux, resultatCible)
# collectionNombresInitiaux= [1,1,1,1]
# resultatCible = 1080
# start = time.time()
# res = indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],[],collectionNombresInitiaux, resultatCible)
# duree = time.time() - start
# print("durée indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],collectionNombresInitiaux, resultatCible) : "+ str(duree) + " seconde(s)")
# print("résultat indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],collectionNombresInitiaux, resultatCible) : "+str(res))
# print(obtenirUneDescriptionDuneSolution(res, collectionNombresInitiaux,resultatCible))

# collectionNombresInitiaux= [1,2,3,4,5,6]
# resultatCible = 1080
# start = time.time()
# res = indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],[],collectionNombresInitiaux, resultatCible)
# duree = time.time() - start
# print("durée indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],collectionNombresInitiaux, resultatCible) : "+ str(duree) + " seconde(s)")
# print("résultat indiquerUneSequenceSolutionApprocheeOuExacteParExtensionDuneSequence([],collectionNombresInitiaux, resultatCible) : "+str(res))
# print(obtenirUneDescriptionDuneSolution(res, collectionNombresInitiaux,resultatCible))


# collectionNombresInitiaux= [1,2,3,4,5,6]
# resultatCible = 1080
# start = time.time()
# res = listerSequencesSolutions([], collectionNombresInitiaux, resultatCible)
# duree = time.time() - start
# print("durée listerSequencesSolutions([], collectionNombresInitiaux, resultatCible) : "+ str(duree) + " seconde(s)")


collectionNombresInitiaux= [1,2,3,4,5,6]
resultatCible = 1081
start = time.time()
res = indiquerUneSequenceSolutionParExtensionDuneSequence([], collectionNombresInitiaux, resultatCible)
duree = time.time() - start
print("durée indiquerUneSequenceSolutionParExtensionDuneSequence([], collectionNombresInitiaux, resultatCible) : "+ str(duree) + " seconde(s)")
print("résultat indiquerUneSequenceSolutionParExtensionDuneSequence([], collectionNombresInitiaux, resultatCible) : "+str(res))





if __name__ == "__main__":
 doctest.testmod()

