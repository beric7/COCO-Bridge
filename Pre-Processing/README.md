# Reference Pre-ProcessingFileStructure.PNG

Your Pre-Processing folder should look exactly like this, with the exception of the inference graph folder and __init__.py. The inference graph is generated after running export_inference_graph.py

The ssd_inception_v2_coco_2017_11_17 folder is what you download from the model zoo. The configuration files are also included. 

The "Evaluation_Output" folder has all of the evaluation images which will be used to test/evaluate the model. The "Train_Output" folder has all of the training images which will be used to train the model. Both of these folders should auot-populate upon running the code in the "Toolkit" fodler.

The "training_data" folder will hold the bounding box CSV files initially. Through the code in the "Toolkit" folder, an additional CSV file for the evaluation and training will be generated to distinguish from the old CSV file. The reason we would want to create new CSV files is if one wanted to augment their data through re-scaling, rotations, mirroring, etc. Upon running the generate_tfrecords.py the folder will include tf.records. These records are what is used in training. During training the this folder is populated with model checkpoints. After training, an inference graph may be made using these checkpoints.
