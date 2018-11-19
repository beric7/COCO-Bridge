# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:38:42 2018

@author: Eric Bianchi
"""

class class_list(object):

    # The class "constructor" - It's actually an initializer 
    def __init__(self, ID):
        if ID == 1:
            self.ID = "Gusset Plate Connection"
        elif ID == 2:
            self.ID = "Out of Plane Stiffener"
        elif ID == 3:
            self.ID = "Cover Plate Termination"
        elif ID == 4:
            self.ID = "Bearing"
            


            
