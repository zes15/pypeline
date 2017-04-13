#!/usr/bin/Python

""" BLOCKTYPES """
# E = Baige Block
# C = Brown Block
# A = Blue Block
# B = Bright Blue Block
# D = Gray Block

# neon blocks
# r = red neon block
# w = white neon block
# b = blue neon block
# y = yellow neon block
# o = orange neon block
# g = green neon block

# unbreakables
# n = unbreakable 1
# m = unbreakable 2

# X = Exit Block # TRIGGERS LEVEL CHANGE
# O = blank patrol platform # PLAYER REMOVES THESE BLOCKS WHEN COLLIDING WITH THEM
# Q = Corner patrol platform # THESE BLOCKS ARE PERMANENT FOR EACH LEVEL

""" ENEMIES """
# 1 = Garbage Collector
# 2 = Green Snake
# 3 = Red Snake
# 4 = Blue Snake
# 5 = Purple Snake
# 6 = Red Ghost
# 7 = White Ghost

import classes

""" lists to store levels and enemies """
get_levels = [0] #, get_enemies = [0], [0] # init first index to 0

MAX_PLAYTIME_PER_LEVEL = [0, 8000, 360, 360] # max time allowed before time runs out per level
SPAWN_POINT_LEVEL = [0, (64, 135), (64, 64), (64, 64)] # x,y coordinates for each level spawn
BACKGROUNDS = [0, 'background5.jpg', 'beauty.jpg', 'forest_day.png', 'montanha.png']
    # Get list of backgrounds for the levels
for i in range(1, len(BACKGROUNDS)):
    BACKGROUNDS[i] = classes.SPRITES_DIRECTORY + 'backgrounds/' + BACKGROUNDS[i]

level_1 = [

"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn          Xo                                                                                                           B",
"nn          Xo                                                                                                            B",
"nn          Xo                                                                                                         B",
"nn         nnn                                                                                                          B",
"nn        n                     7                                                                                     B",
"nn       n                         7                                                                                     B",
"nn  n                                                                                                                     B",
"nn  n                                                                                                                    B",
"nn  nnQ  2   Q     n   Q   2   Q nQ 2  QnQ    2  Qn   7      Q                                                           B",
"nn   nnnnnnnnnn   nnnnn   nnnnn  nnnnn   nnnnnnn   nnnnnnnnnn                                                           B",
"nn                                                             n                                                          B",
"nn                                                              n                                                         B",
"nn                                                               n          7                                             B",
"nn      Q                        1                          Q     n                                                       B",
"nn      nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn      n                                                      B",
"nn                                                                  n                                                     B",
"nn                                                                   n         7                                          B",
"nn                                                                    n                                                   B",
"nn                                                                     n                                                  B",
"nn                                                                      n                                                 B",
"nn                                                                       n                                                B",
"nn                                                                        n                                               B",
"nn                nnnnnn                                                   n                                              B",
"nn                                                                          D                                          B",
"nn              n            n                                               D n                                      B",
"nn              nQ    2     Qn            Q  2                2  Q            nn                                        B",
"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnB"]

# add enemies/levels to list
get_levels.append(level_1)

level_2 = [
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                                                                                                        					B",
"nn                                    7                                                                                   					B",
"nn                                     7                                                                               			   		B",
"nn                                                                                                                       				 	B",
"nn                                                                                                                        			     	B",
"nn                                                                                                                        				 	B",
"nn            7                                                                                                          				 	B",
"nn                                           DDDDDDDDDDDDDDDD          7                                               				    B",
"nn                                D          D              D                                                             					B",
"nn                                D          D            7 D                                                            					 B",
"nn    	               7           D                                                                 Q  2   Q             					B",
"nn                            7   D          D              D     7   Q        1  Q       7            nnnnnn          					 B",
"nn             O    2   2 Q       D     7   7DO      2     QD          QDDDDDDDDDD              n                      					 B",
"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn     nnnnnnnnnnnnnnnnnnnn          nnnnnnnnnnnnnnnnnnnnnnnnnnnnB"
"nn                                                                        nn                                 n                              B",
"nn                                                  7                      n                                 n                              B",
"nn                                   7                      7              n                                 n          			   		 B",
"nn                                                                         nQ                               Qn                              B",
"nn                                                                         nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn                              B",
"nn                                                                                                                         				 B",
"nn                                                                                                                        					 B",
"nn                                                                                                                        				     B",
"nn                                                                                                                          				 B",
"nn                                                                                                                          				 B",
"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnB"]
# add enemies/levels to list
get_levels.append(level_2)
'''
level_3 = [
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                        B",
"nn                                                                                                                       B",
"nn                                                                                                                       B",
"nn                                                                                                                        B",
"nn                                                                                                                      B",
"nn             6                                                                                                       B",
"nn            7                                                                                                          B",
"nn         7                                                                                                              B",
"nn                                                                                      Xnn                             B",
"nn               nnnnnn                                                          Xnn                                    B",
"nn    	                                                                                 Xnn                             B",
"nn            n            n                                                                        Xnn                  B",
"nn            nQ    2     Qn            Q  2                2  Q                            Xnn                          B",
"nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnB"]

# add enemies/levels to list

get_levels.append(level_3)
'''
