#!/bin/bash
#PBS -l nodes=1:ppn=32
#PBS -l walltime=03:00:00
#PBS -W group_list=cascades
#PBS -q v100_normal_q
#PBS -A InfraEval



module load Anaconda/5.1.0 cuda/9.0.176 cudnn/7.1

source activate objDetector

export PYTHONPATH=$PYTHONPATH:/home/beric7/new_code_obj_detector/tensorflow/models/research:/home/beric7/new_code_obj_detector/tensorflow/models/research/slim

cd $PBS_O_WORKDIR


python ~/No_Augmentation_NFsouthern/No_Aug_NFsouthern_5000s1e/3_train.py
