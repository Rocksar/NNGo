# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:51:00 2018

@author: Roland
"""
import tensorflow as tf
from tensorflow import keras
import numpy as np
import sys
import re
import matplotlib.pyplot as plt
from math import ceil

    
model=keras.models.load_model("C:/PythonWorkSpace/Neural_Network_Go/NN07092018/49_50game_model_07092018.h5")

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
#C="W"

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
    c=(2,1)[text[0]=="b"]
    if len(text)>4:
        if ord(text[2])>ord('i'):
            case=ord(text[2])-ord('a')+(20-int(text[3])*10-int(text[4]))*21
        else:
            case=ord(text[2])+1-ord('a')+(20-int(text[3])*10-int(text[4]))*21
#        print(case)
    elif ord(text[2])>ord('i'):
        case=ord(text[2])-ord('a')+(20-(int(text[3])))*21
    else:
        case=ord(text[2])+1-ord('a')+(20-(int(text[3])))*21
    if Board[case]not in [1,2]:
        Board[case]=c
        update(c)
    return(Board)
        
        
def parse_Board(color):
    matricevide=np.zeros(shape=(W,H), order='F')
    matricenoir=np.zeros(shape=(W,H), order='F')
    matriceblanc=np.zeros(shape=(W,H), order='F')
    for i in range(0,len(Board)):
        if Board[i]==0:
            matricevide[(int(i/21)-1)][(i%21)-1]=1
        elif Board[i]==1:
            matricenoir[(int(i/21)-1)][(i%21)-1]=1
        elif Board[i]==2:
            matriceblanc[(int(i/21)-1)][(i%21)-1]=1

    array=np.zeros(shape=(1,3,W,H), order='F')
    if color=='b':
        array[0][0]=matricevide
        array[0][1]=matricenoir
        array[0][2]=matriceblanc
    else:
        array[0][0]=matricevide
        array[0][2]=matricenoir
        array[0][1]=matriceblanc
#    fig, axs = plt.subplots(1, 3)
#    axs[0].matshow(np.reshape(array[0][0],(19,19)))
#    axs[1].matshow(np.reshape(array[0][1],(19,19)))
#    axs[2].matshow(np.reshape(array[0][2],(19,19)))
#    plt.show()    
  
    return(array)
        
def predict(color):
#    print(parse_Board().shape)
#    predictions=model.predict(parse_Board())
#    print(predictions)
    i=-1
    tmp=np.argsort(model.predict(parse_Board(color))[0])[i]+1
#    while Board[tmp+int(tmp/19)*2+21]!=0:
#        print('Joue sur une case ou une pierre est déja présente')
#        print(tmp)
#        i-=1
#        tmp=np.argsort(model.predict(parse_Board(color))[0])[i]+1
        

#    print(tmp)
#   tmp=1
    if 0<(tmp%19)<10:
#        print(color+' '+chr((tmp%19)-1+ord('a'))+str(19-int(tmp/19)))
#        print (color+' '+chr((tmp%19)-1+ord('a'))+str(20-ceil(tmp/19)))
        return color+' '+chr((tmp%19)-1+ord('a'))+str(20-ceil(tmp/19))
    
    else:
#        print(color+' '+chr((tmp%19)-1+ord('a'))+str(19-int(tmp/19)))
        if tmp%19==0:
            return color+' t'+str(20-ceil(tmp/19))
        else:
            return color+' '+chr((tmp%19)+ord('a'))+str(20-ceil(tmp/19))

def gtp_io():
    """ GTP interface for our program.  We can play only on the board size
    which is configured (N), and we ignore color information and assume
    alternating play! """
    known_commands = ['boardsize', 'clear_board', 'komi', 'play', 'genmove',
                      'final_score', 'quit', 'name', 'version', 'known_command',
                      'list_commands', 'protocol_version']


    while True:
        try:
            line = input().strip()
#            print(line)
        except EOFError:
            break
        if line == '':
            continue
        command = [s.lower() for s in line.split()]
        if re.match('\d+', command[0]):
            cmdid = command[0]
            command = command[1:]
        else:
            cmdid = ''
        
        ret = ''
        if command[0] == "boardsize":
            ret="boardsize ="+str(W)+'*'+str(H)
        elif command[0] == "clear_board":
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
        elif command[0] == "komi":
            ret='6,5'
        elif command[0] == "play":
            Board=play(command[1]+' '+command[2])
            ret=''
        elif command[0] == "genmove":
#            print(Board)
            move=predict(command[1])
#            print(move)
            ret=move[2:]
            plt.show(plt.matshow(np.reshape(model.predict(parse_Board(command[1])),(19,19))))
            play(move)
#            plt.show(plt.matshow(np.reshape(Board,(21,21))))
            
        elif command[0] == "name":
            ret = 'NN nul'
        elif command[0] == "version":
            ret = 'simple go program demo'
        elif command[0] == "list_commands":
            ret = '\n'.join(known_commands)
        elif command[0] == "known_command":
            ret = 'true' if command[1] in known_commands else 'false'
        elif command[0] == "protocol_version":
            ret = '2'
        elif command[0] == "quit":
            print('=%s \n\n' % (cmdid,), end='')
            break
        else:
            print('Warning: Ignoring unknown command - %s' % (line,), file=sys.stderr)
            ret = None

#        print(owner_map)
        if ret is not None:
            print('=%s %s\n\n' % (cmdid, ret,), end='')
        else:
            print('?%s ???\n\n' % (cmdid,), end='')
        sys.stdout.flush()
if __name__ == "__main__":
    
    if sys.argv[1] == "gtp":
        gtp_io()
    else:
        print('Unknown action', file=sys.stderr)

#
#plt.show(plt.matshow(np.reshape(Board,(21,21))))
#plt.show(plt.matshow(np.reshape(play("b t19"),(21,21))))
#plt.show(plt.matshow(np.reshape(play(predict('w')),(21,21))))

