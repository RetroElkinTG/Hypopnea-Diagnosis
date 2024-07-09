#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (24T2) 

You can use this file to test your find_episodes().

This file containing seven test cases which you can choose by
adjusting the variable test_num in Line 22. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_episodes as epi 

# %% Constants 
LEN_PER_EPISODE = 2
ORDINAL_ENDINGS = ['first','second','third']

# %% Tests 
test_num = 4

# Default value for min_segment 
min_segment = 2  # default, unless overidden 

if test_num == 0:
    disorder_status = [False] * 3 # no episodes
    expected_answer = []
elif test_num == 1: 
    disorder_status = [True] * 5 # one episode   
    expected_answer = [[0, 5]]
elif test_num == 2: 
    disorder_status = [False, True, True, True, False, False, False] # one episode   
    expected_answer = [[1, 3]]
elif test_num == 3: 
    disorder_status = [False, True, True, True, False, 
                       True, True, True, True, False] # two episodes   
    expected_answer = [[1, 3],[5,4]]
elif test_num == 4: 
    disorder_status = [True, True, False, False, True, 
                       True, True, True, True, False]  
                      # two episodes, one episode at the start 
    expected_answer = [[0, 2],[4,5]]    
elif test_num == 5: 
    disorder_status = [True, True, False, False, True, 
                       True, True, True, True, False,  
                       False, True, True]  
                      # three episodes, one episode at the start 
                      # one in the middle, one at the end 
    expected_answer = [[0, 2],[4,5],[11,2]]   
elif test_num == 6: 
    disorder_status = [True, True, False, False, True, 
                       True, True, True, True, False,  
                       False, True, True]  
                      # three episodes, one episode at the start 
                      # one in the middle, one at the end 
    min_segment = 3                  
    expected_answer = [[4,5]] 


# %% 
your_answer = epi.find_episodes(disorder_status,min_segment)
print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if len(your_answer) != len(expected_answer):
    print('We are expecting',len(expected_answer),'episodes')
    print('but your answer has ',len(your_answer),'episodes')
else:
    if len(your_answer) > 0:
        for k in range(len(expected_answer)):
            your_episode_info = your_answer[k]
            if len(your_episode_info) != LEN_PER_EPISODE:
                print('We expect each episode to be specified by')
                print('two elements')
            else: 
                print('Checking the episode indexed by',k,':')
                
                expected_episode_info = expected_answer[k]
                
                if your_episode_info[0] == expected_episode_info[0]:
                    print('Your start time is correct')
                else:
                    print('Your start time is',your_episode_info[0])
                    print('The expected start time is',expected_episode_info[0])
                    print('Your start time is NOT correct')                
                    
                if your_episode_info[1] == expected_episode_info[1]:
                    print('Your duration is correct')
                else:
                    print('Your duration is',your_episode_info[1])
                    print('The expected duration is',expected_episode_info[1])
                    print('Your duration is NOT correct') 
    else:
        print('Your answer is an empty list, which is correct!')
