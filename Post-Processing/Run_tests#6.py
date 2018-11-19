# -*- coding: utf-8 -*-
"""
The vast majority of this code was developed by:
    
@author https://github.com/Cartucho/mAP

"""


"""
Created on Thu Oct 18 01:22:09 2018

This code was altered by:
    
@author: Eric Bianchi,

to serve his specific needs.

"""

import sys
sys.path.insert(0, "C://Users/Eric Bianchi/Documents/Virginia Tech/Graduate School/Research/Python_Package")
from test import main
from Metrics_Eval_Build import metricsEval
from mAP_main import mAP_Results

# ============================================================================
Model = "#6-NFS_4c_5000s1e"
# ============================================================================
# module level variables ######################################################
NUM_CLASSES = 4
###############################################################################
metricsEval(Model)
main(NUM_CLASSES, Model, 0.01, "1%")
#main(NUM_CLASSES, Model, 0.25, "25%")
#main(NUM_CLASSES, Model, 0.50, "50%")
#main(NUM_CLASSES, Model, 0.75, "75%")

mAP_Results(0.35, Model, "1%")
mAP_Results(0.35, Model, "25%")
mAP_Results(0.35, Model, "50%")
mAP_Results(0.35, Model, "75%")

mAP_Results(0.50, Model, "10%")
mAP_Results(0.50, Model, "25%")
mAP_Results(0.50, Model, "50%")
mAP_Results(0.50, Model, "75%")
    
mAP_Results(0.75, Model, "10%")
mAP_Results(0.75, Model, "25%")
mAP_Results(0.75, Model, "50%")
mAP_Results(0.75, Model, "75%")
