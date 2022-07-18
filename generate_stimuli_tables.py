# This script takes the structure of the experiment provided by the
# StimuliTable-Encoding and StimuliTable-Recognition, and creates a specified
# number of stimuli tables with the images selected randomly.

import pandas as pd
import trk_module as trk
import os.path as op

n_files = 5 # define number of stimuli files to be created
encoding_fname = 'StimuliTable-Encoding_4-blocks_48-pairs_cont-loc_12345-delays.xlsx'
recognition_fname = 'StimuliTable-Recognition_4-blocks_48-pairs_cont-loc_12345-delays.xlsx'
encoding_table = pd.read_excel(encoding_fname)
recognition_table = pd.read_excel(recognition_fname)

n_encoding_images, n_all_images = trk.get_exp_parameters(encoding_table, recognition_table)

for i in range(n_files):
    outpath = 'stimuli_tables'
    encoding_trials_fname = 'encoding_trials_{}.csv'.format(str(i))
    regognition_trials_fname = 'recognition_trials_{}.csv'.format(str(i))
    images, foil_images = trk.select_images(n_encoding_images, n_all_images)
    encoding_trials = trk.set_encoding_trials(encoding_table, images)
    encoding_trials.to_csv(op.join(outpath, encoding_trials_fname), index=False)

    recognition_trials = trk.set_recognition_trials(recognition_table, encoding_trials, foil_images)
    recognition_trials.to_csv(op.join(outpath, regognition_trials_fname), index=False)
