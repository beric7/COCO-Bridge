# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:41:22 2018
@author: Eric Bianchi
"""

   
from PIL import Image
import os
import shutil
import cv2
import csv

# ============================================================================
Model = "#6-NFS_4c_5000s1e"
# ============================================================================
pwd = "PATH/" + Model + "/Pre-Processing"

# The file path is either going to be Evaluation_Files or Train_Files
# This will decide whether or not the data will be Evaluation or Training since 
# they are separated into multiple parts. 
# FILE_PATH = "Train" or "Evaluation"
# ID = "T" or "E"
FILE_PATH = "Train"
ID = "T"
typToSave = str("JPEG")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Main method
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    
    shutil.rmtree(pwd + '/' + FILE_PATH + '_Output')     
    shutil.rmtree('Data_photo/Finished_Files')   
    
    os.mkdir(pwd + '/' + FILE_PATH + '_Output')    
    os.mkdir('Data_photo/Finished_Files')
    
    removeCon()
    
    copiedDirectory = "Data_photo/" + FILE_PATH + "_Files"
    
    #++++++++++++++++++++++++++++++++++++++++++
    f1 = open('Augmentation_Number_' + FILE_PATH + '.csv')
    csv_f1 = csv.reader(f1)  
    #++++++++++++++++++++++++++++++++++++++++++
    augNum = []
    
    for col in csv_f1:
        augInfo = col[1]
        augNum.append(augInfo)
     
    i = 1
    num_p = 1
    
    for filename in os.listdir(copiedDirectory):
        im1 = Image.open(copiedDirectory + '/' + filename) 
        
        #++++++++++++++++++++++++++++++++++++++++++++
        #Choose to resize the images or not
        #++++++++++++++++++++++++++++++++++++++++++++ 
        w = int(im1.width)
        h = int(im1.height)
        max_dim = max(w,h)
        
        target_dim = 340
        divider = int(max_dim/target_dim)
        
        if (max_dim) > 340:
            w = int(w/divider)
            h = int(h/divider)
            image = im1.resize((w,h))
        else:
             image = im1
                
               
        image.save(copiedDirectory +'/' +  filename, typToSave)
        # directory path
        path = (copiedDirectory + '/' + filename)
        
        #Gets the number of augmentations for each image.
        number = int(augNum[i])
        
        print("Image iteration: " + str(i))
        
        # rotate images
        if (number >= 1):
            rotate(path, 0, "Data_photo/Rotate_0" + '/' + filename, "Data_photo/Rotate_0", i)
            path0 = "Data_photo/Rotate_0" + '/' + "Rotate_0"
            full_file_name = os.path.join("Data_photo/Rotate_0/", "Rotate_0" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Rotate_0" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1    
            
        if (number >= 2):
            rotate(path, 90, "Data_photo/Rotate_90" + '/' + filename, "Data_photo/Rotate_90", i)
            path90 = "Data_photo/Rotate_90" + '/' + "Rotate_90"
            full_file_name = os.path.join("Data_photo/Rotate_90/", "Rotate_90" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Rotate_90" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1
            
        if (number >= 3):
            rotate(path, 180, "Data_photo/Rotate_180" + '/' + filename, "Data_photo/Rotate_180", i)
            path180 = "Data_photo/Rotate_180" + '/' + "Rotate_180"
            full_file_name = os.path.join("Data_photo/Rotate_180/", "Rotate_180" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Rotate_180" + "_" + str(i) + "." + typToSave,
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1

                      
        if (number >= 4):
            rotate(path, 270, "Data_photo/Rotate_270" + '/' + filename, "Data_photo/Rotate_270", i)  
            path270 = "Data_photo/Rotate_270" + '/' + "Rotate_270"
            full_file_name = os.path.join("Data_photo/Rotate_270/", "Rotate_270" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Rotate_270" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1
                      
        # mirror images
        if (number >= 5):
            mirror_image(path0, 0, "Data_photo/Mirror_R0" + '/' + filename, "Data_photo/Mirror_R0", i)
            full_file_name = os.path.join("Data_photo/Mirror_R0/", "Mirror_R0" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Mirror_R0" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1
            
        if (number >= 6):
            mirror_image(path90, 90, "Data_photo/Mirror_R90" + '/' + filename, "Data_photo/Mirror_R90", i)
            full_file_name = os.path.join("Data_photo/Mirror_R90/", "Mirror_R90" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Mirror_R90" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1
            
        if (number >= 7):
            mirror_image(path180, 180, "Data_photo/Mirror_R180" + '/' + filename, "Data_photo/Mirror_R180", i)
            full_file_name = os.path.join("Data_photo/Mirror_R180/", "Mirror_R180" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Mirror_R180" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")
            num_p = num_p + 1
            
        if (number >= 8):
            mirror_image(path270, 270, "Data_photo/Mirror_R270" + '/' + filename, "Data_photo/Mirror_R270", i)     
            full_file_name = os.path.join("Data_photo/Mirror_R270/", "Mirror_R270" + "_" + str(i) + "." + typToSave)
            shutil.copy(full_file_name, pwd + "/" + FILE_PATH + "_Output/")
            os.rename(pwd + "/" + FILE_PATH + "_Output/Mirror_R270" + "_" + str(i) + "." + typToSave, 
                      pwd + "/" + FILE_PATH + "_Output/" + str(num_p) + "_" + ID + "." + "jpg")            
            num_p = num_p + 1      
            
        i = i + 1
        
    # rename the files to a numerical order
    #rename("Data_photo/Output", "Data_photo/Finished_Files")
    
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Rotate an image 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rotate(image_path, degrees_to_rotate, saved_location, src, num):
    """
    Rotate the image
 
    @param image_path: The path to the image to edit
    @param degrees_to_rotate: The number of degrees to rotate the image
    @param saved_location: Path to save the rotated image
    """
    mat = cv2.imread(image_path)
    height = mat.shape[0]
    width = mat.shape[1]
    
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape
    
    rotation_mat = cv2.getRotationMatrix2D(image_center, degrees_to_rotate, 1.)
    
    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])
    
    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)
    
    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))

    cv2.imwrite(saved_location, rotated_mat)

    (head, tail) = os.path.split( saved_location )
    (head, tail) = os.path.split( head )
    
    ID = src + '/' + tail + "_" + str(num) + "." + typToSave
    os.rename(saved_location, ID)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Flip an image 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def mirror_image(image_path, degrees_to_rotate, saved_location, src, num):
    """
    Mirror the image
 
    @param image_path: The path to the image to edit
    @param saved_location: Path to save the flipped image
    """
    
    image_obj = Image.open(image_path + "_" + str(num) + ".JPEG")
    image_obj = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    image_obj.save(saved_location)
    
    (head, tail) = os.path.split( saved_location )
    (head, tail) = os.path.split( head )
    ID = src + '/' + tail + "_" + str(num) + "." + typToSave
    os.rename(saved_location, ID)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Copy and move files 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def copyfiles(src, dest):
    """
    copies the files and moves them to another directory
    
    @param src: source
    @param dest: destination
    """
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)
            
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Rename files
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       
def rename(direc, destination):           
    i = 1
     
    for filename in os.listdir(direc):
        
        # Rename images
        dst = str(i) + "." + typToSave
        src = direc + '/'+ filename
        dst = destination + '/'+ dst
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Remove folder contents
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def removeCon():
    # Remove the existing folders
    shutil.rmtree('Data_photo/Rotate_0')
    shutil.rmtree('Data_photo/Rotate_90')
    shutil.rmtree('Data_photo/Rotate_180')
    shutil.rmtree('Data_photo/Rotate_270') 
    
    shutil.rmtree('Data_photo/Mirror_R0')
    shutil.rmtree('Data_photo/Mirror_R90')
    shutil.rmtree('Data_photo/Mirror_R180')
    shutil.rmtree('Data_photo/Mirror_R270') 
    
    #Make the folders
    os.mkdir('Data_photo/Rotate_0')
    os.mkdir('Data_photo/Rotate_90')
    os.mkdir('Data_photo/Rotate_180')
    os.mkdir('Data_photo/Rotate_270')
    
    os.mkdir('Data_photo/Mirror_R0')
    os.mkdir('Data_photo/Mirror_R90')
    os.mkdir('Data_photo/Mirror_R180')
    os.mkdir('Data_photo/Mirror_R270')
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Call the Main Method
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
if __name__ == '__main__':
    main()
