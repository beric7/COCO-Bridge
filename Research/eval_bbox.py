# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:49:47 2018

@author: Eric Bianchi
"""

class eval_bbox(object):
     
    class_type = ""
    coord = []

    # The class "constructor" - It's actually an initializer 
    def __init__(self, ID, class_type, score, xmin, ymin, xmax, ymax):
        self.class_type = class_type
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.score = score
        self.ID = ID
    
    def toString(self):
        return(self.class_type + "," + str(self.score) + "," + str(self.xmin) + "," + 
               str(self.ymin) + "," + str(self.xmax) + "," + str(self.ymax))
        