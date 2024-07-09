#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 24T2 Assignment 1 

Template file for has_symptom().     
"""

def has_symptom(data_segment, interval, threshold):
    minimum = interval[0]
    maximum = interval[1]
    count = 0

    # Iterate through each item and check if its within threshold
    for index in data_segment:
        if index >= minimum and index <= maximum:
            count += 1

    pvi = count / len(data_segment) # percentage_of_values_in_interval
    if pvi < threshold:
        return False
    else:
        return True
