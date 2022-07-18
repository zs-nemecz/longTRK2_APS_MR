# todo
# define tests for: checking matche between trial pairs; encoding and recognition block matching, number of trials/block
# create classes for experiment, blocks and trials
# create pandas dataframe and save csv

import pandas as pd
import os.path as op
import numpy as np
from numpy.random import randint, shuffle

n_baseline = 16
max_n_trials = (16 * 2 * 3 * 3) + n_baseline # 16*2 images in each 3 types (ERP, LLP, OLP) in 3 blocks
print(max_n_trials)
n_blocks = 4
n_block_trials = int(max_n_trials/n_blocks)
n_OLP = (max_n_trials - n_baseline)/3 # a third of the trials excluding BL are OLP
n_LLP = n_OLP # number of trials per trial type should be the same
n_ERP = n_OLP
print(n_OLP, n_LLP, n_ERP)
n_bl_per_block = int(n_baseline/n_blocks)
delay_types = [1,2,3,4,5,6] # number of delay types must be divisible by the (total number of trials/block) - (BL/block)
lure_types = ['OLP', 'LLP']
block_order = ['OBJ', 'OBJ', 'LOC', 'LOC']

n_lures_per_block = int(((n_OLP + n_LLP)/n_blocks)/2)
print(n_lures_per_block)
n_erp_per_block = int((n_ERP/n_blocks)/2)
print(n_erp_per_block)
max_n_delay_type = int((n_block_trials-n_bl_per_block)/(2*len(delay_types)))
print(max_n_delay_type)
delay_array = np.empty((0), int)
stimtype_array = np.empty((0), str)
trial_type_array = np.empty((0), str)
trial_order_array = np.empty((0), str)

for bt in block_order:
    repeat = True
    trial_type = np.array([bt] * n_block_trials)
    while repeat:
        # placeholder arrays for stimuli type and delays
        stim_types = np.array(['xxx'] * n_block_trials)
        delays = np.array([-1] * n_block_trials)
        order = np.array([0] * n_block_trials)
        # first, add baseline trials to a random position
        for bl in range(n_bl_per_block):
            bl_index = randint(0, n_block_trials-1)
            delays[bl_index]=0
            stim_types[bl_index] = 'BL'

        #shuffle delay and stim types and assign in a loop
        delay_type_list = delay_types * max_n_delay_type
        shuffle(delay_type_list)
        if bt == 'LOC':
            lure_type = 'LLP'
        else:
            lure_type = 'OLP'
        stim_type_list = n_lures_per_block * [lure_type] + n_erp_per_block * ['ERP']
        shuffle(stim_type_list)
        for i, delay in enumerate(delays):
            for d, dtype in enumerate(delay_type_list):
                    if (i+dtype+1) < len(delays):
                        if (delays[i]==-1) and (delays[i+dtype+1]==-1):
                            delays[i] = delay_type_list[d]
                            stim_types[i] = stim_type_list[-1]
                            order[i] = 1
                            delays[i+delay_type_list[d]+1] = 0
                            stim_types[i+delay_type_list[d]+1] = stim_type_list[-1]
                            order[i+delay_type_list[d]+1] = 2
                            delay_type_list.pop(d)
                            stim_type_list.pop()

        # check for unassigned slots - repeat if necessary
        if -1 in delays:
            repeat = True
        else:
            repeat = False
            stimtype_array = np.append(stimtype_array, stim_types)
            delay_array = np.append(delay_array, delays)
            trial_type_array = np.append(trial_type_array, trial_type)
            trial_order_array = np.append(trial_order_array, order)

# Step 2: read existing stimuli file and edit contents
encoding_fname = 'StimuliTable-Encoding_4-blocks_48-pairs_cont-loc_12345-delays.xlsx'
encoding_table = pd.read_excel(encoding_fname)
encoding_table['StimType'] = stimtype_array
encoding_table['Delay'] = delay_array
encoding_table['TrialType'] = trial_type_array
encoding_table['Order'] = trial_order_array
fname_out = 'StimuliTable-Encoding_4-blocks_48-pairs_cont-loc_12345-delays.xlsx'
encoding_table.to_excel(fname_out, index=False)
