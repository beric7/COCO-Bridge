# Reference Pre-ProcessingFileStructure.PNG

Your Pre-Processing folder should look exactly like this, with the exception of the inference graph folder and __init__.py. The inference graph is generated after running export_inference_graph.py

The ssd_inception_v2_coco_2017_11_17 folder is what you download from the model zoo. The configuration files are also included. 

The "Evaluation_Output" folder has all of the evaluation images which will be used to test/evaluate the model. The "Train_Output" folder has all of the training images which will be used to train the model. Both of these folders should auot-populate upon running the code in the "Toolkit" fodler.
