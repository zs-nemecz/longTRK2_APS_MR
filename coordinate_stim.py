### Packages
import pandas as pd
import random as r

### Class, function
class Trial ():

    def __init__(self, num, combo):
        self.trialnum = num #the number of the trial
        self.target_x = combo[0] #Trial() takes a list as arguement that give it the two target coordinates, x and y
        self.target_y = combo[1]
        self.lure_foil_dist = 4
        self.lures = [1,2] #you can specify the distances a lure can get
        self.foils = self.foil_calc() #it calculates possible foil distances based on target x and y
        self.lure1_coord_x, self.lure1_coord_y, self.lure2_coord_x, self.lure2_coord_y, self.foil_coord_x, self.foil_coord_y = self.lure_foil_coords()

    #destination_maker selects an x and a y coordinate based on a distance randomly chosen from the possible distances (lures or foils)
    def destination_maker (self, destinations):
        direction_matrix = [[1,-1], [-1,1], [1,1], [-1,-1]] #these are the possible combinations of "directions" -> minus goes left/up; plus goes right/down
        destination = r.choice(destinations) #randomly chosen distance
        permutation_matrix = Trial.permutation_maker(destination) #it makes all the possible permutations of distances (e.g. 6 can be 1,5 or 3,3, etc...)

        #it then combines the direction possibilities with the distance permutations and gets every location that is &destination away from target
        sum_versions = []
        for direction_type in direction_matrix:
            sum_version = [permutation*direction for permutations in permutation_matrix for permutation, direction in zip(permutations, direction_type)]
            sum_version = [sum_version[x:x+2] for x in range(0, len(sum_version),2)]
            for sum_ele in sum_version:
                sum_versions.append(sum_ele)

        #it then randomly chooses a location, that is in bound, and returns the x and y coordinates
        while len(sum_versions) > 0:
            chosen_version = sum_versions.pop(r.randrange(len(sum_versions)))
            new_x = self.target_x + chosen_version[0]
            new_y = self.target_y + chosen_version[1]
            if new_x > 6 or new_x < 1 or new_y > 4 or new_y < 1:
                continue
            else:
                break

        return new_x, new_y

    #makes permutations for a single distance value in two coordinate values. (E.g.: 6 could be 1,5 or 2,4, or 3,3, etc..)
    @staticmethod
    def permutation_maker (step_num):
        permutations = []
        for n in range(step_num):
            permutation = [n, step_num-n]
            permutation_reverse = [step_num-n, n]
            if permutation not in permutations:
                permutations.append(permutation)
            if permutation_reverse not in permutations:
                permutations.append(permutation_reverse)

        return permutations

    #calculates possible foil distance based on target x and target y. (E.g.: 3,3 can only have a foild of 5 distance, while 1,1 could have one 8 steps away)
    def foil_calc (self):
        possibilities = [5]
        if (self.target_x == 3 or self.target_x == 4) and (self.target_y == 4 or self.target_y == 1):
                possibilities.append(6)

        if self.target_x == 2 or self.target_x == 5:
            possibilities.append(6)
            if self.target_y == 4 or self.target_y == 1:
                possibilities.append(7)

        if self.target_x == 1 or self.target_x == 6:
            possibilities.append(6)
            possibilities.append(7)
            if self.target_y == 4 or self.target_y == 1:
                possibilities.append(8)

        return possibilities


    def lure_foil_coords (self):
        # making foils
        foil_coord_x, foil_coord_y = self.destination_maker(self.foils)
        
        lure1_coord_x, lure1_coord_y = self.destination_maker(self.lures)
        
        dist = abs(lure1_coord_x-foil_coord_x) + abs(lure1_coord_y-foil_coord_y)
        while dist < self.lure_foil_dist:
            print('Finding new lure 1')
            lure1_coord_x, lure1_coord_y = self.destination_maker(self.lures)
            dist = abs(lure1_coord_x-foil_coord_x) + abs(lure1_coord_y-foil_coord_y)

        lure2_coord_x, lure2_coord_y = self.destination_maker(self.lures)
        
        lure_conflict = abs(lure2_coord_x-foil_coord_x) + abs(lure2_coord_y-foil_coord_y) < 2
        while lure_conflict: 
            print('Lure 2 dist: ', dist)
            print('Lure conflict: ', lure_conflict)
            print('Finding new lure 2')
            lure2_coord_x, lure2_coord_y = self.destination_maker(self.lures)
            lure_conflict = abs(lure2_coord_x-foil_coord_x) + abs(lure2_coord_y-foil_coord_y) < 2
            dist = abs(lure2_coord_x-foil_coord_x) + abs(lure2_coord_y-foil_coord_y)

        return lure1_coord_x, lure1_coord_y, lure2_coord_x, lure2_coord_y, foil_coord_x, foil_coord_y

#makes pixel-wise coordinate from a value that signifies the location in the grid
def coordinate_maker (base, grid_len, coord, coord_type):
    coordinate = base + coord*grid_len
    if coord_type == "x":
        coordinate -= grid_whole_x//2
    elif coord_type == "y":
        coordinate -= grid_whole_y//2

    #jitter = int(r.uniform(-grid_len/2, grid_len/2)) #for continous lures

    return coordinate

def pix_to_norm (coord, xy):
    if xy == "x":
        coord_new = coord / (screen_len // 2)
    else:
        coord_new = coord / (screen_height // 2)

    return coord_new

### Code
#Pixel-values:
base = 25
grid_len = 150
grid_whole_x = 1100
grid_whole_y = 800
screen_height = 1080
screen_len = 1920

#preparing stimulus list
stim_fname = "StimuliTable-Encoding-6-blocks_48-pairs_grid-loc_123456-delays.xlsx"
stim_table = pd.read_excel(stim_fname)

#making a dictionary of possible x-y coordinate combinations
combo_dicts = {}
i = 0
for x in range(1,7):
    for y in range(1,5):
        combo_dicts[i] = [x,y]
        i +=1

#making evenly distributed list with 0-23 values, for choosing combinations from dict
random_combos = list(range(0,24))*7
print(len(random_combos))
r.shuffle(random_combos) #shuffle to randomize

#make a trial for BL - this will not change in the loop
random_bl = random_combos.pop(r.randint(0,len(random_combos)-1))
bl_combo = combo_dicts[random_bl]
trial_bl = Trial(299, bl_combo)

#make new coordinates for each trial pairs
for trial in stim_table.index:
    #Skip where the order is second, as they are manipulated locations
    if int(stim_table.at[trial, "Order"]) == 2:
        continue

    #get the delay value for placing the same coordinates to delays
    delay_val = int(stim_table.at[trial,"Delay"]) + 1
    #choosing a random combination of x and y coordinates
    random_combo = random_combos.pop(r.randint(0,len(random_combos)-1))
    combo = combo_dicts[random_combo]

    #making Trial only for non-BL trials, BLs will be trial_bl
    if stim_table.at[trial, "StimType"] == "BL":
        trial_curr = trial_bl
    else:
        #making a Trial type object
        trial_curr = Trial(trial, combo)

    trial_x = coordinate_maker(base, grid_len, trial_curr.target_x, "x")
    trial_y = coordinate_maker(base, grid_len, trial_curr.target_y, "y")
    lure1_x = coordinate_maker(base, grid_len, trial_curr.lure1_coord_x, "x")
    lure1_y = coordinate_maker(base, grid_len, trial_curr.lure1_coord_y, "y")
    lure2_x = coordinate_maker(base, grid_len, trial_curr.lure2_coord_x, "x")
    lure2_y = coordinate_maker(base, grid_len, trial_curr.lure2_coord_y, "y")
    foil_x = coordinate_maker(base, grid_len, trial_curr.foil_coord_x, "x")
    foil_y = coordinate_maker(base, grid_len, trial_curr.foil_coord_y, "y")

    #choosing target coordinates
    stim_table.at[trial, "Xcoordinate"] = pix_to_norm(trial_x, "x")
    stim_table.at[trial, "Ycoordinate"] = pix_to_norm(trial_y, "y")

    #assigning them to table
    stim_table.at[trial, "Xcoordinate_lure1"] = pix_to_norm(lure1_x, "x")
    stim_table.at[trial, "Ycoordinate_lure1"] = pix_to_norm(lure1_y, "y")
    stim_table.at[trial, "Xcoordinate_lure2"] = pix_to_norm(lure2_x, "x")
    stim_table.at[trial, "Ycoordinate_lure2"] = pix_to_norm(lure2_y, "y")
    stim_table.at[trial, "Xcoordinate_foil"] = pix_to_norm(foil_x, "x")
    stim_table.at[trial, "Ycoordinate_foil"] = pix_to_norm(foil_y, "y")

    #assigning to delayed pairs
    stim_table.at[trial + delay_val, "Xcoordinate"] = pix_to_norm(trial_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate"] = pix_to_norm(trial_y, "y")
    stim_table.at[trial + delay_val, "Xcoordinate_lure1"] = pix_to_norm(lure1_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate_lure1"] = pix_to_norm(lure1_y, "y")
    stim_table.at[trial + delay_val, "Xcoordinate_lure2"] = pix_to_norm(lure2_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate_lure2"] = pix_to_norm(lure2_y, "y")
    stim_table.at[trial + delay_val, "Xcoordinate_foil"] = pix_to_norm(foil_x, "x")
    stim_table.at[trial + delay_val, "Ycoordinate_foil"] = pix_to_norm(foil_y, "y")


#print for fun
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
     print(stim_table)

#export to excel
stim_new_filename = stim_fname.split(".")[0] + "_new." + stim_fname.split(".")[1]
stim_table.to_excel(stim_fname, index=False)
