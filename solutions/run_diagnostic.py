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
import find_episodes as epi
import flow_rate_to_disorder_status as status

# %% 
def run_diagnostic(flow_rate,segment_len,interval,threshold,min_segment):
    # Check inputs
    if not isinstance(flow_rate, list):
        return 'Corrupted input'
    elif not isinstance(segment_len, int):
        return 'Corrupted input'
    elif not isinstance(interval, list):
        return 'Corrupted input'
    elif not isinstance(threshold, float):
        return 'Corrupted input'
    elif not isinstance(min_segment, int):
        return 'Corrupted input'
    elif threshold < 0 or threshold > 1:
        return 'Corrupted input'
    elif interval[1] < interval[0]:
        return 'Corrupted input'
    elif len(flow_rate) < 20:
        return 'Not enough data'
    else:
        data_segments = status.flow_rate_to_disorder_status(flow_rate, segment_len, interval, threshold)
        episodes = epi.find_episodes(data_segments, min_segment)
        return episodes
