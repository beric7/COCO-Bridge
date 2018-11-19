# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:47:27 2018

@author: Eric Bianchi
"""

"""
Creates an object to be used for augmentation
"""
class im_aug(object):

    num = 0
    
    def __init__(self, image, num):
        self.num = num
        self.image = image  
    