import pandas as pd
import numpy as np
import random
fname ='StimuliTable-Encoding-3run-40-520-12345.xlsx'
stim_table = pd.read_excel(fname)
#stim_table[stim_table.columns[-1]].str.strip()
print(stim_table)
coord = pd.read_excel('coordinate_table_discrete_1.xlsx')
i = 0
for row in range(len(stim_table)):
    if stim_table['Order'][row] == 0: # baseline (BL) trials: always take the first location, no need for lures and foil
        stim_table.at[row, 'Xcoordinate'] = coord.at[0, 'Xcoordinate']
        stim_table.at[row, 'Ycoordinate'] = coord.at[0, 'Ycoordinate']
    elif stim_table['Order'][row] == 1:
        delay = stim_table['Delay'][row] + 1
        stim_table.at[row, 'Xcoordinate'] = coord.at[i, 'Xcoordinate']
        stim_table.at[row, 'Ycoordinate'] = coord.at[i, 'Ycoordinate']
        stim_table.at[row+delay, 'Xcoordinate'] = coord.at[i,'Xcoordinate']
        stim_table.at[row+delay,'Ycoordinate'] = coord.at[i, 'Ycoordinate']

        stim_table.at[row, 'Xcoordinate_lure1']= coord.at[i, 'Xcoordinate_lure1']
        stim_table.at[row, 'Ycoordinate_lure1'] = coord.at[i, 'Ycoordinate_lure1']
        stim_table.at[row+delay, 'Xcoordinate_lure1'] = coord.at[i, 'Xcoordinate_lure1']
        stim_table.at[row+delay, 'Ycoordinate_lure1']= coord.at[i, 'Ycoordinate_lure1']


        stim_table.at[row, 'Xcoordinate_lure2']= coord.at[i, 'Xcoordinate_lure2']
        stim_table.at[row, 'Ycoordinate_lure2'] = coord.at[i, 'Ycoordinate_lure2']
        stim_table.at[row+delay, 'Xcoordinate_lure2'] = coord.at[i, 'Xcoordinate_lure2']
        stim_table.at[row+delay, 'Ycoordinate_lure2'] = coord.at[i, 'Ycoordinate_lure2']


        stim_table.at[row, 'Xcoordinate_foil'] = coord.at[i, 'Xcoordinate_foil']
        stim_table.at[row, 'Ycoordinate_foil'] = coord.at[i, 'Ycoordinate_foil']
        stim_table.at[row+delay, 'Xcoordinate_foil'] = coord.at[i, 'Xcoordinate_foil']
        stim_table.at[row+delay, 'Ycoordinate_foil'] = coord.at[i, 'Ycoordinate_foil']

        i +=1

stim_table.to_excel('StimuliTable-Encoding-3run-40-discrete-8-12345_new_coord.xlsx')
