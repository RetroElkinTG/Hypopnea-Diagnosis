#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (24T2) 

You can use this file to test your run_diagnostic().
For this file, the algorithmic parameters are valid, and 
there are sufficient flow rate data for diagnosis. 

This test file uses made-up flow rate data.
"""

# %% import  
import matplotlib.pyplot as plt
import run_diagnostic as diag  

# %% Input data 
# Flow rate 
flow_rate = [-4.5,  0.5,  4.5, -0.1,  -4.3,
             -4.1,  0.1,  4.1,  0.4,  -4.9,
             -1.3,  0.2,  1.1,  0.4,   1.1,
             -1.7,  0.3,  3.1,  0.8,  -2.6,
             -1.5, -0.2,  1.2,  0.6,  -4.1,
             -4.1,  0.1,  4.1,  0.4,  -4.9,    
             -1.2, -0.1,  1.2,  0.7,  -1.9,
             -3.9,  0.1,  2.9,  0.5,  -2.2, 
             -2.0,  0.5,  1.7,  4.6,   4.7, 
             -3.4,  0.2]
             
# Parameters for the diagnostic algorithm
segment_len = 5 # Number of data points in a segment 
interval = [-2.6,3.1] # Use to determine whether a segment has the symptom
threshold = 0.8 # Use to determine whether a segment has the symptom
min_segment = 2 # Minimum number of segments to form an episode 

# %% Expected answer 
expected_answer = [[2, 3], [6, 2]] # if min_segment is 2
# expected_answer = [[2, 3]] # if min_segment is 3

# %% Run run_diagnostic()
episodes = diag.run_diagnostic(flow_rate,segment_len,interval,threshold,min_segment)    

print('The episodes returned by your code are:',episodes)
print('The expected episodes are:',expected_answer)

# %%  Plotting
x_values = range(len(flow_rate))    
x_min_max = [min(x_values),max(x_values)]

fig1 = plt.figure()         # create a new figure
plt.plot(x_values,flow_rate,'-')  
plt.plot(x_min_max,[interval[0]]*2,'r--',
         x_min_max,[interval[1]]*2,'r--')
plt.fill([10,24,24,10],[-2.6,-2.6,3.1,3.1],'m',alpha=0.2)
plt.fill([30,39,39,30],[-2.6,-2.6,3.1,3.1],'m',alpha=0.2)
plt.xlabel('index')    # label for x-axis 
plt.ylabel('flow rate')   # label for y-axis
plt.title('Data for testing') # title of the graph 
plt.show()  # to display the graph 
fig1.savefig('flowrate_1.png')
