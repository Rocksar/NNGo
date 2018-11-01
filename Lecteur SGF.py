# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:50:15 2018

@author: Roland
"""

import glob
import numpy as np
import matplotlib.pyplot as plt
import random

def lecture(text):

    #Initialisation
    
    
    Board=     [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    flag=      [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,
                3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    
    W=19
    H=19
    
    
    def reset_flag():
        for i in range(0,len(flag)):
            if flag[i]==1 :
                flag[i]=0
    
    def reset_flag_partial(c):
        for i in range(0,len(flag)):
            if flag[i]==1 and Board[i]!=c:
                flag[i]=0
                
            
        
    def groupe(x):
        liste=[x]
        lib=0
        i=0
        flag[x]=1
        while i<len(liste):
            p=liste[i]
            for d in [1,W+2,-1,-W-2]:
                if flag[p+d]!=1:
                    if Board[p+d]==Board[p]:
                        liste.append(p+d)
                    if Board[p+d]==0:
                        lib+=1
                flag[p+d]=1
            i+=1
            
        reset_flag_partial(Board[x])
            
        return(liste,lib)
                
    
    def delete(groupe):
        for i in groupe:
            Board[i]=0
            flag[i]=0
    
    def update(c):
        for i in range (0,len(Board)):
            if flag[i]!=1:
                if Board[i] not in [0,3] and Board[i]!=c:
                    eval=groupe(i)
                    #print(eval)
                    if eval[1]==0:
                        delete(eval[0])
        for i in range (0,len(Board)):
            if flag[i]!=1:
                if Board[i] not in [0,3]:
                    eval=groupe(i)
                    #print(eval)
                    if eval[1]==0:
                        delete(eval[0])
        reset_flag()
                        
    
    
    def play(text):
        c=(2,1)[text[0]=="B"]
        case=ord(text[2])+1-ord('a')+(ord(text[3])+1-ord('a'))*21
        print(text)
        print(case)
#        plt.show(plt.matshow(np.reshape(Board,(21,21))))
        if Board[case] not in [1,2]:
            Board[case]=c
            update(c)
        else :
            raise ValueError("Joue sur une case ou une pierre est déja présente")
            
        return text[0]
            
    
        
    def parser(fichier):
        file=open(fichier,'r')
        file=file.read()
        file=file.split(";")
        print(file)
        tmp=0
        handicap=file[1].split('\n')
        print(handicap)
        for i in handicap:
            if 'HA[' in i:
                tmp=int(i[3])
                print("good")
                print(tmp)
            if 'AB[' in i:
                print (i)
                play(i[1:])
            if len(i)!=0:    
                if i[0]=='[' and len(i)==4:
                    print(i)
                    play("B"+i)
#        while tmp!=0:
#            try:
#                print(handicap[-(1+tmp)])
#                play("B"+handicap[-(1+tmp)][-4:])
#                tmp-=1
#            except:
#                print(handicap[-(2+tmp)])
#                play("B"+handicap[-(2+tmp)][-4:])
#                tmp-=1
            
                
                
        file[-1]=file[-1][:5]
        #print(file[2:])
        for i in file:
            if len(i)<5:
                print("ok")
                file.remove(i)
        return file[1:-1]
    
    def extraire_data(couleur):
        matricevide=[0]*(W*H)
        matricenoir=[0]*(W*H)
        matriceblanc=[0]*(W*H)
        #print(len(matricevide))
        for i in range(0,len(Board)):
            if Board[i]==0:
                matricevide[(int(i/21)-1)*19+(i%21)-1]=1
            elif Board[i]==1:
                matricenoir[(int(i/21)-1)*19+(i%21)-1]=1
            elif Board[i]==2:
                matriceblanc[(int(i/21)-1)*19+(i%21)-1]=1
        if couleur=="B":
            return(matricevide,matriceblanc,matricenoir)
        else:
            return(matricevide,matricenoir,matriceblanc)
    
    def extraire_resultat(i):
       
        text=partie[i]
        return ord(text[2])-ord('a')+(ord(text[3])-ord('a'))*19
    print(text)
    partie=parser(text)
    print(partie)
    
    tmp=0
    played=[]
    reponse=[]
    for i in partie[:-1]:
        couleur=play(i)
        data=np.array(extraire_data(couleur[0]))
        resultat=np.array(extraire_resultat(tmp+1))
        played.append(data)
        reponse.append(resultat)
        
#        print(np.array(played).shape)
#        print(np.array(reponse).shape)
#        print(tmp)
#        input()
        tmp+=1
    print(text)
#    played=np.array(played)
#    reponse=np.array(reponse)
    
#    print(played.shape)
    
    r=random.randint(0,7)
    step=9
    playedcopy=[]
    reponsecopy=[]
    for i in range(r,len(played),step):
           playedcopy.append(played[i])
           reponsecopy.append(reponse[i])
    
#    print(playedcopy.shape)
    
    
    
    np.save("C:/PythonWorkSpace/Neural_Network_Go/train2015/"+str(tempo),playedcopy)
    np.save("C:/PythonWorkSpace/Neural_Network_Go/train2015/"+str(tempo)+'out',reponsecopy)
    

tempo=0
#lecture("C:/PythonWorkSpace/Neural_Network_Go/kgs-19-2011-2/2011-01-02-36.sgf")



for i in glob.glob("C:/PythonWorkSpace/Neural_Network_Go/kgs-19-2015/*"):
    print(i)
    lecture(i)
    tempo+=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    