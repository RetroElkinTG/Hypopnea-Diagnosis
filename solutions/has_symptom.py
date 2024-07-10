#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 24T2 Assignment 1   
"""

"""
Purpose: Run a hypopnea diagnosis
Author: Elkin Franco
Date: 09/07/2024
"""

def has_symptom(data_segment, interval, threshold):
    count = 0

    # Iterate through each item and check if its within threshold
    for index in data_segment:
        if index >= interval[0] and index <= interval[1]:
            count += 1

    # Check if percentage of values in interval meets the threshold
    pvi = count / len(data_segment) 
    if pvi >= threshold:
        return True
    else:
        return False
