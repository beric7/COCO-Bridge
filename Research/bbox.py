# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:46:33 2018

@author: Eric Bianchi
"""

class bbox(object):
     
    class_type = ""
    coord = []

    # The class "constructor" - It's actually an initializer 
    def __init__(self, class_type, coord):
        self.class_type = class_type
        self.coord = coord
        

