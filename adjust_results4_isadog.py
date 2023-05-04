#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog_hints.py
#                                                                             
# PROGRAMMER: minpo jung
# DATE CREATED: 2023.05.01                        
# REVISED DATE: 2023.05.01

def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()

    with open(dogfile, "r") as infile:
        line = infile.readline()

        while line != "":
            line = line.rstrip()  # Removing the newline character from the variable line

            if line not in dognames_dic:  # Adds dogname(line) to dogsnames_dic if it doesn't already exist
                dognames_dic[line] = 1

            line = infile.readline()

    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))  # Appends (1,0) because only pet label is a dog
        else:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))  # Appends (0,1) because only Classifier label is a dog
            else:
                results_dic[key].extend((0, 0))  # Appends (0,0) because both labels aren't dogs

    print("==== adust_results4_isadog.py started ==============")
    print()
    print("result_dic's value")
    print(results_dic)
    print("==== adust_results4_isadog.py ended ==============")
    