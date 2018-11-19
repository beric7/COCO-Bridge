# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 19:13:59 2018
Make a list of augmented images
@author: Eric Bianchi
"""

import csv
import sys

# ============================================================================
Model = "#6-NFS_4c_5000s1e"
# ============================================================================

sys.path.insert(0, "C://Users/Eric Bianchi/Documents/Virginia Tech/Graduate School/Research/Python_Package")

from csv_info import csv_info
from image import image
from bbox import bbox
from im_aug import im_aug
    
# The file path is either going to be Evaluation_Files or Train_Files
# This will decide whether or not the data will be Evaluation or Training since 
# they are separated into multiple parts.

pwd = "C://Users/Eric Bianchi/Documents/Virginia Tech/Graduate School/Research/" + Model + "/Pre-Processing"
# output .csv file names/locations
TRAINING_DATA_DIR = pwd + "/" + "training_data"
TRAIN_CSV_FILE_LOC = TRAINING_DATA_DIR + "/" + "train_labels.csv"
EVAL_CSV_FILE_LOC = TRAINING_DATA_DIR + "/" + "eval_labels.csv"

# "Train" or "Evaluation"
FILE_PATH = "Evaluation"

# "T" or "E"
ID = "E"
 

#++++++++++++++++++++++++++++++++++++++++++
f = open(EVAL_CSV_FILE_LOC)
csv_f = csv.reader(f)  
#++++++++++++++++++++++++++++++++++++++++++
imList = []
infoList = []
i = 0
for col in csv_f:
    if i >= 1:       
        info = csv_info(col[0],int(col[1]),int(col[2]),col[3],int(col[4]),
                        int(col[5]),int(col[6]),int(col[7]))
        infoList.append(info)
    i = i + 1

a = True
repeat = ""
bboxList = []
im_bboxList = []
i = 0

while i < len(infoList):
    name = infoList[i].filename
    if name == repeat or a == True:
        
        #bring back to default
        cur_im = infoList[i]
        a = False
        repeat = infoList[i].filename
        
        #appending the bounding box list
        cur_bbox = bbox(cur_im.class_type, cur_im.coord)
        im_bboxList.append(cur_bbox)
        i = i + 1 
        
        if i == len(infoList): #edge case
            #appedning the image list
            imList.append(image(cur_im.filename, im_bboxList, cur_im.height, cur_im.width))
    else:
        imList.append(image(cur_im.filename, im_bboxList, cur_im.height, cur_im.width))
        im_bboxList =[]
        a = True

#++++++++++++++++++++++++++++++++++++++++++
f1 = open('Augmentation_Number_' + FILE_PATH + '.csv')
csv_f1 = csv.reader(f1)  
#++++++++++++++++++++++++++++++++++++++++++
augNum = []
augImList = []

for col in csv_f1:
    augInfo = col[1]
    augNum.append(augInfo)
    
i = 1
while i < len(augNum):
    augImList.append(im_aug(imList[i-1], augNum[i]))
    i = i + 1
    
#++++++++++++++++++++++++++++++++++++++++++
# Apply Coordinate Change
#++++++++++++++++++++++++++++++++++++++++++  

print(augImList[0].image.bbox_list[0].class_type)
newAugImList = []

for i in augImList:
    n = int(i.num)
    im = i.image

    if n == 1:
        newAugImList.append(im)
    if n == 2:
        newAugImList.extend([im, im.rotate(90)])
    if n == 3:
        newAugImList.extend([im, im.rotate(90), im.rotate(180)])
    if n == 4:
        newAugImList.extend([im, im.rotate(90), im.rotate(180), im.rotate(270)])
    if n == 5:
        newAugImList.extend([im, im.rotate(90), im.rotate(180), im.rotate(270), 
                             im.mirrorObj(0)])
    if n == 6:
        newAugImList.extend([im, im.rotate(90), im.rotate(180), im.rotate(270), 
                             im.mirrorObj(0), im.mirrorObj(90)])
    if n == 7:
        newAugImList.extend([im, im.rotate(90), im.rotate(180), im.rotate(270), 
                             im.mirrorObj(0), im.mirrorObj(90), im.mirrorObj(180)])
    if n == 8:
        newAugImList.extend([im, im.rotate(90), im.rotate(180), im.rotate(270), 
                             im.mirrorObj(0), im.mirrorObj(90), im.mirrorObj(180),
                             im.mirrorObj(270)])

toCSV = []
i = 1

for im in newAugImList:    
    im.setName(i, ID) 
    i += 1

"""
for im in newAugImList:
    im.toString()
"""

for im in newAugImList:
    for bb in im.bbox_list:
        #csv_info(filename, width, height, class type, xmin, ymin, xmax, ymax)
        
        #++++++++++++++++++++++++++++++++++++++++++++
        #Choose to resize the images or not
        #++++++++++++++++++++++++++++++++++++++++++++ 
        w = im.width
        h = im.height
        max_dim = max(w,h)
        
        target_dim = 340
        
        if (max_dim) > 340:
            reduc = 1/int(max_dim/target_dim)
                          
        toCSV.append(csv_info(im.name, str(int(reduc*im.width)), str(int(reduc*im.height)), bb.class_type, 
                              str(int(reduc*bb.coord[0])), str(int(reduc*bb.coord[1])),
                              str(int(reduc*bb.coord[2])), str(int(reduc*bb.coord[3]))))
i = 0

with open(TRAINING_DATA_DIR + '/Bbox_info_CSV_output_' + FILE_PATH + '.csv', 'w', newline='') as f:
    fieldnames = ['filename', 'width', 'height', 'class', 'xmin', 
                  'ymin', 'xmax', 'ymax']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for obj in toCSV:
        thewriter.writerow({'filename': obj.filename, 'width': obj.width, 
                        'height': obj.height, 'class': obj.class_type, 
                        'xmin': obj.coord[0], 'ymin': obj.coord[1],
                        'xmax': obj.coord[2], 'ymax': obj.coord[3]})


  
   
    