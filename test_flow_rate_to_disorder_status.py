#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (24T2) 

You can use this file to test your flow_rate_to_disorder_status().

This file containing two cases which you can choose by
adjusting the variable test_num in Line 20. 

You can use this file to come out with additional tests. 

"""
# %% import 
import flow_rate_to_disorder_status as status 
    
# %% Test cases 

# Choose the test number by changing the variable test_num  
test_num = 0

if test_num == 0:
    flow_rate = [-2.1, -3.1, 1.0, -2.3, 4.4,  5.1,  
                  1.7, -9.2, 0.2,  9.2, 0.2, -1.6,
                  1.7, -2.2, 4.4,  9.2, 0.2, -0.6] 
    segment_len = 6 
    interval = [-5.5,6.1]
    threshold = 0.7
    expected_answer = [True, False, True] 
    expected_len = 3 
elif test_num == 1:
    flow_rate = [ 9.9, -7.1, 9.4,  7.6, 3.2, 
                  1.7, -2.2, 9.4,  2.2, 0.2,  
                 -2.1, -3.1, 1.0, -2.3, 4.4,
                  2.7, -9.2, 9.4,  9.2, 0.2]
    segment_len = 5 
    interval = [-6.5,7.1]
    threshold = 0.8
    expected_answer = [False, True, True, False] 
    expected_len = 4 

#%% Run the function flow_rate_to_disorder_status()

your_output = status.flow_rate_to_disorder_status(flow_rate,segment_len,interval,threshold)

if len(your_output) != expected_len:
    print('We expect a list with length',expected_len)
    print('but the length of your list is',len(your_output))
else: # your_output has the correct length 
    compare_lists = [ele_your == ele_exp for 
                     ele_your, ele_exp in zip(your_output,expected_answer)]
    
    if all(compare_lists):
        print('Your function output matches the expected output')
    else:
        print('Your function output does NOT matche the expected output') 
        
        
