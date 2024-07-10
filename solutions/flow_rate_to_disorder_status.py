#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 24T2 Assignment 1    
"""

"""
Purpose: Run a hypopnea diagnosis
Author: Elkin Franco
Date: 10/07/2024
"""

# %% Import 
import has_symptom as sym 

# %% 
def flow_rate_to_disorder_status(flow_rate,segment_len,interval,threshold):

    # Split array into sets
    split_array = [flow_rate[i:i + segment_len] for i in range(0, len(flow_rate), segment_len)]

    # Remove last array element if uneven
    last_item_index = len(split_array) - 1
    if len(split_array[last_item_index]) != segment_len:
        split_array.pop()

    # Create a boolean array of detected symptoms
    boolean_array = []
    for index in split_array:
        symptom = sym.has_symptom(index, interval, threshold)
        boolean_array.append(symptom)

    return boolean_array
