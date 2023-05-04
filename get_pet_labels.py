#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: minpo jung
# DATE CREATED: 2013.04.30                         
# REVISED DATE: 2013.04.30
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 2" for the get_pet_labels function 
#       Please be certain to replace None in the return statement with 
#       results_dic dictionary that you create with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    #in_files = listdir('pet_images/')    
    results_dic = dict()   
    
    for file in in_files:        
        if file[0] != ".":            
            pet_label = ""
            
            file_parts = file.split("_")
            for word in file_parts:                
                if word.isalpha():
                    pet_label += word.lower() + " "
            
            pet_label = pet_label.strip()

            
            if file not in results_dic:
                results_dic[file] = [pet_label]
            else:
                print("Warning: Duplicate files exist in directory", file)

    # Replace None with the results_dic dictionary that you created with this
    # function    
    return results_dic

print('this file is get_pet_labels.py')
r = get_pet_labels('./pet_images')
# Print the content of result_dic
for key, value in r.items():
    print("Filename: ", key, "\tPet label: ", value[0])
print('this file is get_pet_labels.py ended....======================')