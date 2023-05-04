#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: minpo jung
# DATE CREATED: 2013.05.01                                
# REVISED DATE: 2013.05.01
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    print('classify_image function started....')
    for key in results_dic:
        try:
            # Get image file path
            image_file_path = images_dir + '/' + key
            
            # Get classifier labels
            classifier_labels = classifier(image_file_path, model)
            
            # Format classifier labels
            classifier_labels = classifier_labels.lower().strip()
            
            # Compare pet image label and classifier label
            pet_image_label = results_dic[key][0]
            match = int(pet_image_label in classifier_labels.split(', '))
            
            # Extend the results_dic with classifier label and the match
            results_dic[key].extend([classifier_labels, match])
        except Exception as e:
            print(f"Error processing file {key}: {str(e)}")
    print('classify_image function ended....')
    print('==================================')
    print()
    return results_dic
    
# Print the content of result_dic
#main code
'''
print('start classify_images.py check')

for key, value in result_dic.items():
    print("Filename: ", key)
    print("Pet label: ", value[0])
    print("Classifier label: ", value[1])
    print("Match (1 = match, 0 = no match): ", value[2])
    print("\n")
print('end classify_images.py check ')
'''