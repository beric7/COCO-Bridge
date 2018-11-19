# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:38:07 2018
csv info class
@author: Eric Bianchi
"""

"""
Creates a bounding box object
@param xmin: the lower x coord. corner of the bounding box
@param xmax: the upper x coord. corner of the bounding box
@param ymin: the lower y coord. corner of the bounding box
@param ymax: the upper y coord. corner of the bounding box
"""
class csv_info(object):
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    class_type = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, filename, width, height, class_type, xmin, ymin, xmax, ymax):
        self.class_type = class_type
        coord = [(xmin), (ymin), (xmax), (ymax)]  
        self.coord = coord
        self.filename = filename
        self.width = width
        self.height = height
        
    def toString(self):
        print(self.filename + "," + str(self.width) + "," + str(self.height) 
        + "," + self.class_type + "," + str(self.coord[0]) + "," + 
        str(self.coord[1]) + "," + str(self.coord[2])+ "," + str(self.coord[3]))
