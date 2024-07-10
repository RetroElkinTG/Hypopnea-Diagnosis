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

def find_episodes(disorder_status,min_segment):
    count = 0
    current_episode_length = 0
    episode_array = []

    # Iterate through the array, finding episodes
    for index, item in enumerate(disorder_status):
        if item:
            if current_episode_length == 0:
                # Start a new sequence
                start_index = index
            current_episode_length += 1
        else:
            if current_episode_length >= min_segment:
                count += 1
                episode_array.append([start_index, current_episode_length])
            current_episode_length = 0
    
    # Check the last sequence
    if current_episode_length >= min_segment:
        count += 1
        episode_array.append([start_index, current_episode_length])

    return episode_array
