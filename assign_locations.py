# this script assigns lure and foil locations to original coordniates
import pandas as pd
import numpy as np
import random

def assign_index(raw_i,max_i):
    '''assign index based on direction'''
    if raw_i < 0:
        index = max_i + raw_i
    elif raw_i > max_i:
        index = raw_i - max_i
    else:
        index = raw_i
    return index

orig = 'original_coordinates_8.csv'
coord = pd.read_csv(orig, sep=',', lineterminator='\n')
indeces = np.arange(0, len(coord))
coord = coord[['Xcoordinate', 'Ycoordinate']]
# print(coord)
# coord.to_csv('original_coordinates_8.csv', index = False)

min_distance = 1
max_distance = 1
min_foil_distance = 3
max_foil_distance = 4

lure1_distance=np.random.randint(min_distance,max_distance + 1,size=indeces.shape)
lure2_distance=np.random.randint(min_distance,max_distance + 1,size=indeces.shape)
foil_distance = np.random.randint(min_foil_distance,max_foil_distance + 1,size=indeces.shape)
lure1_signs =[(-1)**random.randint(0,1) for i in lure1_distance]
lure2_signs = [lure_sign * -1 for lure_sign in lure1_signs] # put the second lure on the other side of the original location
lure1_distance = lure1_distance*lure1_signs
lure2_distance = lure2_distance*lure2_signs
foil_distance = foil_distance*lure2_signs # multiply with lure 2 sign, to make sure that the foil is always far enough from lure 1 

lure1_indexes = []
lure2_indexes = []
foil_indexes = []

xcoordinate_lure1=[]
ycoordinate_lure1=[]
xcoordinate_lure2=[]
ycoordinate_lure2=[]
xcoordinate_foil = []
ycoordinate_foil = []

#assign positions based on distance
max_i = len(coord.index)-1
for i in range(len(coord.index)):
    lure1_index = indeces[i] + lure1_distance[i]
    lure1_index = assign_index(lure1_index, max_i)
    lure1_indexes.append(lure1_index)
    xcoordinate_lure1.append(coord['Xcoordinate'][lure1_index])
    ycoordinate_lure1.append(coord['Ycoordinate'][lure1_index])

    lure2_index = indeces[i] + lure2_distance[i]
    lure2_index = assign_index(lure2_index, max_i)
    lure2_indexes.append(lure2_index)
    xcoordinate_lure2.append(coord['Xcoordinate'][lure2_index])
    ycoordinate_lure2.append(coord['Ycoordinate'][lure2_index])

    foil_index = indeces[i] + foil_distance[i]
    foil_index = assign_index(foil_index, max_i)
    foil_indexes.append(foil_index)
    xcoordinate_foil.append(coord['Xcoordinate'][foil_index])
    ycoordinate_foil.append(coord['Ycoordinate'][foil_index])

data = {'Xcoordinate_lure1': xcoordinate_lure1,
        'Ycoordinate_lure1': ycoordinate_lure1,
        'Xcoordinate_lure2': xcoordinate_lure2,
        'Ycoordinate_lure2': ycoordinate_lure2,
        'Xcoordinate_foil': xcoordinate_foil,
        'Ycoordinate_foil': ycoordinate_foil,
        'Lure1_Distance': lure1_distance,
        'Lure2_Distance': lure2_distance,
        'Foil_Distance':foil_distance,
        }

cols = ['Xcoordinate_lure1', 'Ycoordinate_lure1', 'Xcoordinate_lure2', 'Ycoordinate_lure2', \
        'Xcoordinate_foil', 'Ycoordinate_foil', 'Lure1_Distance', 'Lure2_Distance', 'Foil_Distance']
new_coord = pd.DataFrame (data, columns = cols)

# create new dataframe containing both original, lure and foil locations
df = pd.concat([coord, new_coord], axis = 1, sort = False)
#shuffle rows
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('coordinate_table_discrete_1.csv', index = False)
print(df)
