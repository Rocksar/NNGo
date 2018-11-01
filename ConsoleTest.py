# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:41:51 2018

@author: Roland
"""

import sys
import re

W=19
N=19

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
            print("boardsize ="+str(N))
        elif command[0] == "clear_board":
            owner_map = W*W*[0]
        elif command[0] == "komi":
            print("6,5")
        elif command[0] == "play":
            print(command[2])
        elif command[0] == "genmove":
            ret ='jouer un coup'
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
gtp_io()
