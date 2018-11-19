# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:36:27 2018

@author: Eric Bianchi
"""

import os
import csv
import sys

sys.path.insert(0, "C://Users/Eric Bianchi/Documents/Virginia Tech/Graduate School/Research/Python_Package")
from eval_con import eval_con

def metricsEval(Model):
    # module level variables ##############################################################################################
    pwd = "C://Users/Eric Bianchi/Documents/Virginia Tech/Graduate School/Research/" + Model + "/Pre-Processing"
    #######################################################################################################################
    #++++++++++++++++++++++++++++++++++++++++++
    f = open(pwd + '/training_data/Bbox_info_CSV_output_Evaluation.csv')
    csv_f = csv.reader(f)  
    #++++++++++++++++++++++++++++++++++++++++++
    a = 0
    evalList = []
    for col in csv_f:
        if a >= 1:       
            # name, class, xmin, ymin, xmax, ymax
            info = eval_con(str(col[0]), str(col[3]), str(col[4]), str(col[5]), str(col[6]), str(col[7]))
            evalList.append(info)
        a = a + 1
        
    a = True
    repeat = ""
    eval_obj = []
    i = 0
    while i < len(evalList):
        if a == False:
            i = i + 1
        name = evalList[i].name
        filename = os.getcwd() +"/Metrics_Eval_txt/" + evalList[i].name + ".txt"
        f = open(filename,"w+")
        f.close()
        while (name == repeat or a == True) and (i < len(evalList)):
            
            #x_min = evalList[i].xmin
            #aka = evalList[i].name
            #bring back to default
            a = False
            
            if i < len(evalList) - 1:
                repeat = evalList[i+1].name  
                                
            eval_obj.append(evalList[i])          
            print(eval_obj[i].toString())           
            with open(filename, "a+") as fd:
                fd.write(eval_obj[i].toString() + "\n")  
                
            if repeat == name:    
                i = i + 1
                
            
    fd.close()
