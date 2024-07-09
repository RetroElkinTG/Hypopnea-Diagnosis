#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (24T2) 

You can use this file to test your run_diagnostic().
For this file, the algorithmic parameters are valid, and 
there are sufficient flow rate data for diagnosis. 

Data is digitised from the picture in the following paper: 
Jennifer Accardo and Jennifer Reesman, "Can you hear me snore?". 
Journal of Clinical Sleep Medicine, Vol. 9, Number 11. 
http://jcsm.aasm.org/ViewAbstract.aspx?pid=29203
"""

# %% import function 
import matplotlib.pyplot as plt
import run_diagnostic as diag  

# %% read flow_rate from file
with open('test_2_data.txt','r') as f:
    data_str = f.read().splitlines()

# Data type conversion: from str to float     
flow_rate = [float(x) for x in data_str]    

# %% Parameters for the diagnostic algorithm 
segment_len = 10 # Number of data points in a segment 
interval = [-2.6,3.1] # Use to determine whether a segment has the symptom
threshold = 0.95 # Use to determine whether a segment has the symptom
min_segment = 3 # Minimum number of segments to form an episode 

# %% Expected answer 
expected_answer = [[8, 5], [15, 4]]

# %% Call run_diagnostic()
episodes = diag.run_diagnostic(flow_rate,segment_len,interval,threshold,min_segment)    

print('The episodes returned by your code are',episodes)
print('The expected episodes are',expected_answer)

# %%  Plotting
x_values = range(len(flow_rate))    
x_min_max = [min(x_values),max(x_values)]

fig1 = plt.figure()         # create a new figure
plt.plot(x_values,flow_rate,'-')  
plt.plot(x_min_max,[interval[0]]*2,'r--',
         x_min_max,[interval[1]]*2,'r--')

plt.xlabel('index')    # label for x-axis 
plt.ylabel('flow rate')   # label for y-axis
plt.title('Data for testing') # title of the graph 
plt.show()  # to display the graph 
