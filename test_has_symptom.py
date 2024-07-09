#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (24T2) 

You can use this file to test the function has_symptom()

This file containing three test cases which you can choose by
adjusting the variable test_num in Line 20. 

You can also use this file to come out with additional tests. 

"""
# %% import 
import has_symptom as sym  
    
# %% The test cases 

# Choose the test number by changing the variable test_num  
test_num = 2

if test_num == 0:
    data_segment = [-10.2,-7.2,-5.4,-1.2,1.7,4.5,10.1]
    interval = [-4.5,7]
    threshold = 0.9
    expected_answer = False 
elif test_num == 1:
    data_segment = [-10,-7,-5,-1,1,4,10,9,5,1]
    interval = [-10,9.2]
    threshold = 0.9
    expected_answer = True 
elif test_num == 2:
    data_segment = [-10,-7,-5,-1,1,4,10,9,5,1]
    interval = [-10,9.2]
    threshold = 0.900001
    expected_answer = False 

#%% Run the function has_symptom()

your_output = sym.has_symptom(data_segment,interval,threshold)

if your_output == expected_answer:
    print('Your function output matches the expected output')
else:
    print('Your function output does NOT matche the expected output')    
