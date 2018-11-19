# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:45:39 2018

@author: Eric Bianchi
"""

"""
Creates an image object to be used for holding all 
information related to that image
"""
from bbox import bbox

class image(object):
    
    bbox_list = []
    name = ""
    
     
    def __init__(self, n, bb, h, w):
        self.name = n
        self.bbox_list = bb
        self.height = h
        self.width = w
        
    def rotate(self, degrees):  
        h = self.height
        w = self.width
        newBbox_list = []
        
        if degrees == 90:                    
            for obj in (self.bbox_list):
                xmin = obj.coord[1]
                ymin = w - obj.coord[2] + 1
                xmax = obj.coord[3]
                ymax = w - obj.coord[0] + 1
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
            #adjust the height and width
            h = self.width
            w = self.height
            
        if degrees == 180:
            for obj in (self.bbox_list):            
                xmin = w - obj.coord[2] + 1
                ymin = h - obj.coord[3] + 1
                xmax = w - obj.coord[0] + 1
                ymax = h - obj.coord[1] + 1
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
        if degrees == 270:  
            for obj in (self.bbox_list):            
                xmin = h - obj.coord[3] + 1
                ymin = obj.coord[0]
                xmax = h - obj.coord[1] + 1
                ymax = obj.coord[2] 
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
            #adjust the height and width
            h = self.width
            w = self.height
            
        return image(self.name, newBbox_list, h, w)

    def mirrorObj(self, degrees):
        
        #Placeholder variables\
        h = self.height
        w = self.width
        newBbox_list = []
        
        if degrees == 0:
            for obj in (self.bbox_list):
                xmin = w - obj.coord[2] + 1
                ymin = obj.coord[1]
                xmax= w - obj.coord[0] + 1
                ymax = obj.coord[3]
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
        if degrees == 90:
            for obj in (self.bbox_list):
                xmin = h - obj.coord[3] + 1
                ymin = w - obj.coord[2] 
                xmax = h - obj.coord[1] + 1
                ymax = w - obj.coord[0] 
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
            #adjust the height and width
            h = self.width
            w = self.height
            
        if degrees == 180:
            for obj in (self.bbox_list):
                xmin = obj.coord[0]
                ymin = h - obj.coord[3] + 1
                xmax = obj.coord[2]
                ymax = h - obj.coord[1] + 1
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
        if degrees == 270:
            for obj in (self.bbox_list):
                xmin = obj.coord[1]
                ymin = obj.coord[0]
                xmax = obj.coord[3]
                ymax = obj.coord[2] 
                
                coord = [xmin, ymin, xmax, ymax]
                b = bbox(obj.class_type, coord)
                newBbox_list.append(b)
                
            #adjust the height and width
            h = self.width
            w = self.height
            
        return image(self.name, newBbox_list, h, w)
    
    def setName(self, i, ID):
        self.name = str(i) + "_" + ID + ".jpg"
        
    def toString(self):
        print("[" + self.name + "," + str(self.height) + "," + 
                str(self.width) + "," + str(self.bbox_list[0].coord)+"]")
                