#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (24T2) 

You can use this file to test your run_diagnostic().
For this file, the expected output is expected to be the
string 'Corrupted input' or 'Not enough data'. 

"""

# %% import function 
import run_diagnostic as diag  

# %% Flow rate 
flow_rate_all = [-4.5,  0.5,  4.5, -0.1,  -4.3,
                 -4.1,  0.1,  4.1,  0.4,  -4.9,
                 -1.3,  0.2,  1.1,  0.4,   1.1,
                 -1.7,  0.3,  1.3,  0.8,  -2.6,
                 -1.5, -0.2,  1.2,  0.6,  -4.1,
                 -4.1,  0.1,  4.1,  0.4,  -4.9,    
                 -1.2, -0.1,  1.2,  0.7,  -1.9,
                 -3.9,  0.1,  2.9,  0.5,  -2.2, 
                 -2.0,  0.5,  1.7,  4.6,   4.7, 
                 -3.4,  0.2]
             
# %% Parameters for diagnostic algorithm

test_num = 1

if test_num == 0: # Expected output: 'Not enough data'
    # flow_rate has 19 data points but minimum required is 20
    # expected answer is 'Not enough data'
    flow_rate = flow_rate_all[0:19]
    segment_len = 5 # Number of data points in a segment 
    interval = [-2.6,3.1] # Use to determine whether a segment has the symptom
    threshold = 0.70 # Use to determine whether a segment has the symptom
    min_segment = 4 # Minimum number of segments to form an episode 
    
    expected_answer = 'Not enough data'

elif test_num == 1: # Expected output: 'Corrupted input'
    # The variable segment_len is not an integer
    # expected answer is 'Corrupted input'    
    flow_rate = flow_rate_all
    segment_len = 4.1 # Number of data points in a segment 
    interval = [-2.6,3.1] # Use to determine whether a segment has the symptom
    threshold = 0.70 # Use to determine whether a segment has the symptom
    min_segment = 4 # Minimum number of segments to form an episode 

    expected_answer = 'Corrupted input'

elif test_num == 2: # Expected output: 'Corrupted input'
    # The variable interval is invalid because interval[1] < interval[0]
    # expected answer is 'Corrupted input'    
    flow_rate = flow_rate_all
    segment_len = 4 # Number of data points in a segment 
    interval = [3.1,-10] # Use to determine whether a segment has the symptom
    threshold = 0.70 # Use to determine whether a segment has the symptom
    min_segment = 4 # Minimum number of segments to form an episode 

    expected_answer = 'Corrupted input'

elif test_num == 3: # Expected output: 'Corrupted input'
    # The variable threshold is not valid. 
    # Note that there are also insufficient data but you do
    # not need to check that. 
    flow_rate = flow_rate_all[0:15]
    segment_len = 4 # Number of data points in a segment 
    interval = [-2.6,3.1] # Use to determine whether a segment has the symptom
    threshold = -0.05 # Use to determine whether a segment has the symptom
    min_segment = 4 # Minimum number of segments to form an episode 

    expected_answer = 'Corrupted input'

# %% Run run_diagnostic()
    
episodes = diag.run_diagnostic(flow_rate,segment_len,interval,threshold,min_segment)    

# Checking whether the output is a string 
# and if so, is it the correct string 
if type(episodes) != str:
    print('Error: The output is not a string.')
else: 
    if episodes.lower() == expected_answer.lower():
        print('Your output is correct')
    else:
        print('The expected answer is',expected_answer)
        print('Your answer is',episodes)
        print('Your answer does NOT match the expected answer')

