### Packages
import pandas as pd
import random as r
import matplotlib.pyplot as plt
import matplotlib.patches
import numpy as np
from math import sin, cos, radians, pi, sqrt

### Class, function
class Trial ():

    def __init__(self, num):
        self.trialnum = num #the number of the trial
        self.lures = [200, 350] #you can specify the distances a lure can get
        self.foils = [450, None] #it calculates possible foil distances based on target x and y
        self.target_x, self.target_y, self.lure1_coord_x, self.lure1_coord_y, self.lure2_coord_x, self.lure2_coord_y, self.foil_coord_x, self.foil_coord_y = self.coord_maker()

    #destination_maker selects an x and a y coordinate based on a distance randomly chosen from the possible distances (lures or foils)
    def coord_maker(self):
        #making target coordinates
        target_x = np.random.uniform(0, grid_x)
        target_y = np.random.uniform(0, grid_y)

        #create random lure1
        lure_1_x, lure_1_y = meteorites([target_x, target_y],  self.lures[0],  self.lures[1])

        # create for foils
        foil_x, foil_y = meteorites([target_x, target_y], self.foils[0], self.foils[1])
        while (foil_x > grid_x or foil_x < 0) or (foil_y > grid_y or foil_y < 0):
            foil_x, foil_y = meteorites([target_x, target_y], self.foils[0], self.foils[1])

        #create foils
        lure_2_x, lure_2_y = meteorites([target_x, target_y], self.lures[0], self.lures[1])
        while (lure_2_x > grid_x or lure_2_x < 0) or (lure_2_y > grid_y or lure_2_y < 0):
            lure_2_x, lure_2_y = meteorites([target_x, target_y], self.lures[0], self.lures[1])

        #check to not be out of bounds or foil is too close to lure1 or lure 1 and lure 2 is same
        while (lure_1_x > grid_x or lure_1_x < 0) or (lure_1_y > grid_y or lure_1_y < 0) or \
                ((foil_x - lure_1_x) ** 2 + (foil_y - lure_1_y) ** 2 < self.foils[0] ** 2) or \
                (lure_1_x == lure_2_x and lure_1_y == lure_2_y):
            lure_1_x, lure_1_y = meteorites([target_x, target_y], self.lures[0], self.lures[1])


        return target_x, target_y, lure_1_x, lure_1_y, lure_2_x, lure_2_y, foil_x, foil_y


#function to make a ring for choosing random lures, foils
def meteorites(origo = [100,200], lower_bound=150, higher_bound=350):
    angle = np.random.uniform(0, 2 * pi)  # in radians
    if higher_bound == None:
        higher_bound = sqrt(grid_x ** 2 + grid_y ** 2)
    distance = sqrt(np.random.uniform(lower_bound**2, higher_bound**2))
    return origo[0] + distance * cos(angle), origo[1] + distance * sin(angle)


def pix_to_norm (coord, xy):
    coord2 = coord
    if xy == "x":
        coord2 -= grid_x/2
        coord_new = coord2 / (screen_len // 2)
    else:
        coord2 -= grid_y/2
        coord_new = coord2 / (screen_height // 2)

    return coord_new

### Code
plotting = 0
#Pixel-values:
base = 25
grid_len = 150
grid_whole_x = 1100
grid_whole_y = 800
grid_x = 750
grid_y = 450
screen_height = 1080
screen_len = 1920
TrialNum = 249 #trials + 1 baseline

#preparing stimulus list
stim_fname = "StimuliTable-Encoding_4-blocks_48-pairs_cont-loc_12345-delays.xlsx"
stim_table = pd.read_excel(stim_fname)

#making BL trial
trial_bl = Trial(253)

#make new coordinates for each trial pairs
for trial in stim_table.index:
    print(trial)
    
    #Skip where the order is second, as they are manipulated locations
    if int(stim_table.at[trial, "Order"]) == 2:
        continue

    #get the delay value for placing the same coordinates to delays
    delay_val = int(stim_table.at[trial,"Delay"]) + 1

    #making Trial only for non-BL trials, BLs will be trial_bl
    if stim_table.at[trial, "StimType"] == "BL":
        trial_curr = trial_bl
    else:
        # making a Trial type object
        trial_curr = Trial(trial)

    if plotting:
        fname_str = "képek_cont/Figure_"
        #matplotlib.patches.Rectangle(xy = (0,0), width=grid_x, height=grid_y)
        ax = plt.gca()
        ax.cla()
        ax.set_xlim((0,grid_x))
        ax.set_ylim((0, grid_y))
        ax.plot(trial_curr.target_x, trial_curr.target_y, 'o', color = 'red')
        ax.plot(trial_curr.lure1_coord_x, trial_curr.lure1_coord_y, 'v', color = 'green')
        ax.plot(trial_curr.lure2_coord_x, trial_curr.lure2_coord_y, 'h', color = 'blue')
        ax.plot(trial_curr.foil_coord_x, trial_curr.foil_coord_y, 'D', color = 'yellow')
        circle_targ_1 = plt.Circle((trial_curr.target_x, trial_curr.target_y), trial_curr.lures[0], color = 'green', fill=False)
        circle_targ_2 = plt.Circle((trial_curr.target_x, trial_curr.target_y), trial_curr.lures[1], color = 'green', fill=False)
        circle_targ_3 = plt.Circle((trial_curr.target_x, trial_curr.target_y), trial_curr.foils[0], color = 'yellow', fill=False)
        circle_lure_1 = plt.Circle((trial_curr.lure1_coord_x, trial_curr.lure1_coord_y), trial_curr.foils[0], color ='yellow', fill=False)
        ax.add_artist(circle_targ_1)
        ax.add_artist(circle_targ_2)
        ax.add_artist(circle_targ_3)
        ax.add_artist(circle_lure_1)

        #plt.show()
        plt.savefig(fname_str + str(trial+1))

    #choosing target coordinates
    stim_table.at[trial, "Xcoordinate"] = pix_to_norm(trial_curr.target_x, "x")
    stim_table.at[trial, "Ycoordinate"] = pix_to_norm(trial_curr.target_y, "y")

    #assigning them to table
    stim_table.at[trial, "Xcoordinate_lure1"] = pix_to_norm(trial_curr.lure1_coord_x, "x")
    stim_table.at[trial, "Ycoordinate_lure1"] = pix_to_norm(trial_curr.lure1_coord_y, "y")
    stim_table.at[trial, "Xcoordinate_lure2"] = pix_to_norm(trial_curr.lure2_coord_x, "x")
    stim_table.at[trial, "Ycoordinate_lure2"] = pix_to_norm(trial_curr.lure2_coord_y, "y")
    stim_table.at[trial, "Xcoordinate_foil"] = pix_to_norm(trial_curr.foil_coord_x, "x")
    stim_table.at[trial, "Ycoordinate_foil"] = pix_to_norm(trial_curr.foil_coord_y, "y")

    #assigning to delayed pairs
    stim_table.at[trial + delay_val, "Xcoordinate"] = pix_to_norm(trial_curr.target_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate"] = pix_to_norm(trial_curr.target_y, "y")
    stim_table.at[trial + delay_val, "Xcoordinate_lure1"] = pix_to_norm(trial_curr.lure1_coord_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate_lure1"] = pix_to_norm(trial_curr.lure1_coord_y, "y")
    stim_table.at[trial + delay_val, "Xcoordinate_lure2"] = pix_to_norm(trial_curr.lure2_coord_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate_lure2"] = pix_to_norm(trial_curr.lure2_coord_y, "y")
    stim_table.at[trial + delay_val, "Xcoordinate_foil"] = pix_to_norm(trial_curr.foil_coord_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate_foil"] = pix_to_norm(trial_curr.foil_coord_y, "y")


# #print for fun
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#      print(stim_table)
#
#export to excel
stim_new_filename = stim_fname.split(".")[0] + "_new." + stim_fname.split(".")[1]
stim_table.to_excel(stim_new_filename, index=False)

