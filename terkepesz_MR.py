#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on July 19, 2022, at 11:49
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'miniTRK'  # from the Builder filename that created this script
expInfo = {'online ID': '', 'MR ID': '', 'Session': 'OBJ/LOC', 'Stimuli Table': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['online ID'],'APS', expInfo['Session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Zsuzsa\\HCCCL\\TerKepEsz_Tasks\\computer_based_tasks\\longTRK_Phase2\\longTRK2_APS_MR\\terkepesz_MR.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='NLL LCD', color=[0.114,0.310,0.380], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "experiment_setup"
experiment_setupClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
import os
os.system('color')
from termcolor import colored, cprint
import colorama
colorama.init()
win.mouseVisible = False
cprint('State: Experiment Setup', 'blue', 'on_white')
print('Mouse disabled on screen. Keep CMD window active!')
trial_table = expInfo['Stimuli Table']

enc_table = 'stimuli_tables/encoding_trials_'+ trial_table + '.csv'
rec_table = 'stimuli_tables/recognition_trials_'+ trial_table + '.csv'

session = expInfo['Session']
if session == 'OBJ':
    task_name='Képszemle'
    block_name_selection=[0, 76]
    print('Session selected: OBJ')
elif session == 'LOC':
    task_name='Berendezés'
    block_name_selection=[152,228]
    print('Session selected: LOC')
else:
    block_name_selection=[0,76]
    print('Invalid Session! Will use OBJ.')
 
instruction_text = ''
if session == 'OBJ':
    instruction_text = "A Képválogatás alatt azt döntse el, beválogatja-e a képet a kiállításra.\
                        \n\n\t\tJobb mutatóujj - Igen\n\t\tBal mutatóujj - Nem\
                        \n-----------------------------------------------------------------------\
                        \nA Képfelismerés allatt azt döntse el, látta-e már pontosan ugyanezt a képet a Képválogatás alatt.\
                        \n\n\t\tJobb mutatóujj - Új\
                        \n\t\tBal mutatóujj - Régi"
elif session == 'LOC':
    instruction_text = "A Helyválasztás alatt azt döntse el, maradhat-e a kép a bemutatott helyen.\
                        \n\n\t\tJobb mutatóujj - Igen\n\t\tBal mutatóujj - Nem\
                        \n-----------------------------------------------------------------------\
                        \nA Helyfelismerés allatt azt döntse el, pontosan ezen a helyen látta-e a képet a Helyválasztás alatt.\
                        \n\n\t\tJobb mutatóujj - Új\n\t\tBal mutatóujj - Régi"
welcome_image = visual.ImageStim(
    win=win,
    name='welcome_image', units='pix', 
    image='stimuli/terkepesz.png', mask=None,
    ori=0, pos=(0, -100), size=(309,665),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='TérKépÉsz Feladatok',
    font='Arial',
    units='pix', pos=(0, 350), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "general_instructions"
general_instructionsClock = core.Clock()
general_instructions_key = keyboard.Keyboard()
general_instructions_4_continue = visual.TextStim(win=win, name='general_instructions_4_continue',
    text='A gyakorláshoz nyomja le a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
general_instructions_text = visual.TextStim(win=win, name='general_instructions_text',
    text='',
    font='Arial',
    pos=(0, -0.01), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "start_practice"
start_practiceClock = core.Clock()
start_practice_text = visual.TextStim(win=win, name='start_practice_text',
    text='Kezdődik a gyakorlás...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_block_start"
practice_block_startClock = core.Clock()
if session == 'OBJ':
    practice_start = 0
elif session == 'LOC':
    practice_start = 3
else:
    print('Invalid session! Will go with OBJ')
    practice_start = 0
step = 1

practice_block_text = visual.TextStim(win=win, name='practice_block_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "enc_fx_practice"
enc_fx_practiceClock = core.Clock()
enc_fx_interior_practice = visual.ImageStim(
    win=win,
    name='enc_fx_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_fx_cross_practice = visual.TextStim(win=win, name='enc_fx_cross_practice',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
enc_fx_key_practice = keyboard.Keyboard()
enc_fx_text_block_practice = visual.TextStim(win=win, name='enc_fx_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_fx_instructions_text_practice = visual.TextStim(win=win, name='enc_fx_instructions_text_practice',
    text='[BAL MUTATÓUJJ - Nem marad]      [JOBB MUTATÓUJJ - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "enc_trial_practice"
enc_trial_practiceClock = core.Clock()
enc_trial_interior_practice = visual.ImageStim(
    win=win,
    name='enc_trial_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enc_trial_main_image_practice = visual.ImageStim(
    win=win,
    name='enc_trial_main_image_practice', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_trial_key_practice = keyboard.Keyboard()
enc_trial_text_block_practice = visual.TextStim(win=win, name='enc_trial_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
enc_trial_instructions_text_practice = visual.TextStim(win=win, name='enc_trial_instructions_text_practice',
    text='[BAL MUTATÓUJJ - Nem marad]      [JOBB MUTATÓUJJ - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "enc_practice_feedback"
enc_practice_feedbackClock = core.Clock()
enc_practice_feedback_interior = visual.ImageStim(
    win=win,
    name='enc_practice_feedback_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_practice_feedback_image = visual.ImageStim(
    win=win,
    name='enc_practice_feedback_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enc_practice_feedback_text = visual.TextStim(win=win, name='enc_practice_feedback_text',
    text='',
    font='Arial',
    units='norm', pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
enc_practice_feedback_block = visual.TextStim(win=win, name='enc_practice_feedback_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recognition_title"
recognition_titleClock = core.Clock()
start_recognition_text = visual.TextStim(win=win, name='start_recognition_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rec_fx_practice"
rec_fx_practiceClock = core.Clock()
rec_fx_interior_practice = visual.ImageStim(
    win=win,
    name='rec_fx_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_fx_cross_practice = visual.TextStim(win=win, name='rec_fx_cross_practice',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_fx_key_practice = keyboard.Keyboard()
rec_fx_text_block_practice = visual.TextStim(win=win, name='rec_fx_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
rec_fx_instructions_text_practice = visual.TextStim(win=win, name='rec_fx_instructions_text_practice',
    text='[BAL MUTATÓUJJ - Régi]      [JOBB MUTATÓUJJ - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "rec_trial_practice"
rec_trial_practiceClock = core.Clock()
rec_trial_interior_practice = visual.ImageStim(
    win=win,
    name='rec_trial_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_trial_main_image_practice = visual.ImageStim(
    win=win,
    name='rec_trial_main_image_practice', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_trial_key_practice = keyboard.Keyboard()
rec_trial_text_block_practice = visual.TextStim(win=win, name='rec_trial_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_trial_instructions_text_practice = visual.TextStim(win=win, name='rec_trial_instructions_text_practice',
    text='[BAL MUTATÓUJJ - Régi]      [JOBB MUTATÓUJJ - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_practice_feedback"
rec_practice_feedbackClock = core.Clock()
rec_practice_feedback_text = visual.TextStim(win=win, name='rec_practice_feedback_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_practice"
end_practiceClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text='Ez volt a gyakorlás.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=0.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
end_practice_key = keyboard.Keyboard()
end_practice_continue = visual.TextStim(win=win, name='end_practice_continue',
    text='A folytatáshoz nyomja le a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
coming_up_next_text = visual.TextStim(win=win, name='coming_up_next_text',
    text='',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "wait_for_last_scan"
wait_for_last_scanClock = core.Clock()
wait_for_last_scan_text = visual.TextStim(win=win, name='wait_for_last_scan_text',
    text='A vizsgálatvezető előkészíti a szkennert.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wait_for_last_scan_continue = keyboard.Keyboard()

# Initialize components for Routine "start_MR"
start_MRClock = core.Clock()
trigger_key = 's'
def get_trigger_time(*args):
    trigger = globalClock.getTime() - args[0]
    thisExp.addData('trigger', trigger)
    thisExp.nextEntry()
start_MR_text = visual.TextStim(win=win, name='start_MR_text',
    text='A vizsgálatvezető indítja a szkennert.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MR_trigger = keyboard.Keyboard()

# Initialize components for Routine "start_run"
start_runClock = core.Clock()
run_counter = 0
start_enc_run_text = visual.TextStim(win=win, name='start_enc_run_text',
    text='Kezdődik a feladat...',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "encoding_title"
encoding_titleClock = core.Clock()
encoding_title_text = visual.TextStim(win=win, name='encoding_title_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "init_blocks"
init_blocksClock = core.Clock()
if session=='OBJ':
    rec_end = 0;
elif session=='LOC':
    rec_end = 72;
else:
    rec_end = 0;
if session=='OBJ':
    enc_end = 0;
elif session=='LOC':
    enc_end = 152;
else:
    enc_end = 0;

# Initialize components for Routine "encoding_baseline"
encoding_baselineClock = core.Clock()
encoding_baseline_interior = visual.ImageStim(
    win=win,
    name='encoding_baseline_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
encoding_baseline_text_block = visual.TextStim(win=win, name='encoding_baseline_text_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
encoding_baseline_instructions_text = visual.TextStim(win=win, name='encoding_baseline_instructions_text',
    text='[BAL MUTATÓUJJ - Nem marad]      [JOBB MUTATÓUJJ - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
baseline_enc_fx_cross = visual.TextStim(win=win, name='baseline_enc_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "enc_fx"
enc_fxClock = core.Clock()
enc_fx_interior = visual.ImageStim(
    win=win,
    name='enc_fx_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_fx_cross = visual.TextStim(win=win, name='enc_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
enc_fx_key = keyboard.Keyboard()
enc_fx_text_block = visual.TextStim(win=win, name='enc_fx_text_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_fx_instructions_text = visual.TextStim(win=win, name='enc_fx_instructions_text',
    text='[BAL MUTATÓUJJ - Nem marad]      [JOBB MUTATÓUJJ - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "enc_trial"
enc_trialClock = core.Clock()
enc_trial_interior = visual.ImageStim(
    win=win,
    name='enc_trial_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enc_trial_main_image = visual.ImageStim(
    win=win,
    name='enc_trial_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_trial_key = keyboard.Keyboard()
enc_trial_text_block = visual.TextStim(win=win, name='enc_trial_text_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
enc_trial_instructions_text = visual.TextStim(win=win, name='enc_trial_instructions_text',
    text='[BAL MUTATÓUJJ - Nem marad]      [JOBB MUTATÓUJJ - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "encoding_baseline_end"
encoding_baseline_endClock = core.Clock()
encoding_baseline_interior_2 = visual.ImageStim(
    win=win,
    name='encoding_baseline_interior_2', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
encoding_baseline_text_block_2 = visual.TextStim(win=win, name='encoding_baseline_text_block_2',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
encoding_baseline_instructions_text_2 = visual.TextStim(win=win, name='encoding_baseline_instructions_text_2',
    text='[BAL MUTATÓUJJ - Nem marad]      [JOBB MUTATÓUJJ - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
baseline_end_cross = visual.TextStim(win=win, name='baseline_end_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "filler_task"
filler_taskClock = core.Clock()
problem1 = '14 + 26 = ?'
solution1 = 'Bal mutatóujj: 48                Jobb mutatóujj: 40'
correct1= 'b'

problem2 = '3 * 15 = ?'
solution2 = 'Bal mutatóujj: 74                Jobb mutatóujj: 45'
correct2= 'b'

problem3 = '120 / 10 = ?'
solution3 = 'Bal mutatóujj: 12                Jobb mutatóujj: 16'
correct3= 'c'

problem4 = '21 + 15 = ?'
solution4 = 'Bal mutatóujj: 42                Jobb mutatóujj: 36'
correct4= 'c'

problem5 = '6 * 8 = ?'
solution5 = 'Bal mutatóujj: 48\t\t\tJobb mutatóujj: 38'
correct5= 'b'

problem6 = '105 / 5 = ?'
solution6 = 'Bal mutatóujj: 21                Jobb mutatóujj: 28'
correct6= 'c'

math_problems = [problem1, problem2, problem3, problem4, problem5, problem6]

math_solutions = [solution1,solution2,solution3,solution4,solution5, solution6]

math_correct = [correct1,correct2,correct3,correct4,correct5,correct6]


i = 0
math_problem = visual.TextStim(win=win, name='math_problem',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
math_solution = visual.TextStim(win=win, name='math_solution',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
filler_task_resp = keyboard.Keyboard()

# Initialize components for Routine "wait_for_last_scan_rec"
wait_for_last_scan_recClock = core.Clock()
wait_for_last_scan_text_2 = visual.TextStim(win=win, name='wait_for_last_scan_text_2',
    text='Szünet...\n\nA vizsgálatvezető előkészíti a szkennert.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_for_last_scan_continue_2 = keyboard.Keyboard()

# Initialize components for Routine "start_MR_rec"
start_MR_recClock = core.Clock()
start_MR_text_2 = visual.TextStim(win=win, name='start_MR_text_2',
    text='A vizsgálatvezető indítja a szkennert.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MR_trigger_2 = keyboard.Keyboard()

# Initialize components for Routine "start_rec_run"
start_rec_runClock = core.Clock()
start_rec_run_text = visual.TextStim(win=win, name='start_rec_run_text',
    text='Kezdődik a feladat...',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "recognition_title"
recognition_titleClock = core.Clock()
start_recognition_text = visual.TextStim(win=win, name='start_recognition_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "recognition_baseline"
recognition_baselineClock = core.Clock()
recognition_baseline_interior = visual.ImageStim(
    win=win,
    name='recognition_baseline_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
recognition_baseline_text_block = visual.TextStim(win=win, name='recognition_baseline_text_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
recognition_baseline_instructions_text = visual.TextStim(win=win, name='recognition_baseline_instructions_text',
    text='[BAL MUTATÓUJJ - Régi]      [JOBB MUTATÓUJJ - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
baseline_rec_fx_cross = visual.TextStim(win=win, name='baseline_rec_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_fx"
rec_fxClock = core.Clock()
rec_fx_interior = visual.ImageStim(
    win=win,
    name='rec_fx_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_fx_cross = visual.TextStim(win=win, name='rec_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_fx_key = keyboard.Keyboard()
rec_fx_text_block = visual.TextStim(win=win, name='rec_fx_text_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
rec_fx_instructions_text = visual.TextStim(win=win, name='rec_fx_instructions_text',
    text='[BAL MUTATÓUJJ - Régi]      [JOBB MUTATÓUJJ - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "rec_trial"
rec_trialClock = core.Clock()
rec_trial_interior = visual.ImageStim(
    win=win,
    name='rec_trial_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_trial_main_image = visual.ImageStim(
    win=win,
    name='rec_trial_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_trial_key = keyboard.Keyboard()
rec_trial_text_block = visual.TextStim(win=win, name='rec_trial_text_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_trial_instructions_text = visual.TextStim(win=win, name='rec_trial_instructions_text',
    text='[BAL MUTATÓUJJ - Régi]      [JOBB MUTATÓUJJ - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recognition_baseline_end"
recognition_baseline_endClock = core.Clock()
recognition_baseline_interior_2 = visual.ImageStim(
    win=win,
    name='recognition_baseline_interior_2', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
recognition_baseline_text_block_2 = visual.TextStim(win=win, name='recognition_baseline_text_block_2',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
recognition_baseline_instructions_text_2 = visual.TextStim(win=win, name='recognition_baseline_instructions_text_2',
    text='[BAL MUTATÓUJJ - Régi]      [JOBB MUTATÓUJJ - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
baseline_rec_fx_cross_2 = visual.TextStim(win=win, name='baseline_rec_fx_cross_2',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "end_run"
end_runClock = core.Clock()
end_run_text_comp = visual.TextStim(win=win, name='end_run_text_comp',
    text='',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_run_key = keyboard.Keyboard()

# Initialize components for Routine "end_session"
end_sessionClock = core.Clock()
inter_task_break_text = visual.TextStim(win=win, name='inter_task_break_text',
    text='Vége a feladatnak.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
inter_task_break_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "experiment_setup"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
logging.setDefaultClock(globalClock)
# keep track of which components have finished
experiment_setupComponents = [welcome_image, welcome_text]
for thisComponent in experiment_setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
experiment_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "experiment_setup"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = experiment_setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=experiment_setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_image* updates
    if welcome_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_image.frameNStart = frameN  # exact frame index
        welcome_image.tStart = t  # local t and not account for scr refresh
        welcome_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_image, 'tStartRefresh')  # time at next scr refresh
        welcome_image.setAutoDraw(True)
    if welcome_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_image.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_image.tStop = t  # not accounting for scr refresh
            welcome_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_image, 'tStopRefresh')  # time at next scr refresh
            welcome_image.setAutoDraw(False)
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_text, 'tStopRefresh')  # time at next scr refresh
            welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "experiment_setup"-------
for thisComponent in experiment_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_image.started', welcome_image.tStartRefresh)
thisExp.addData('welcome_image.stopped', welcome_image.tStopRefresh)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)

# ------Prepare to start Routine "general_instructions"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
general_instructions_key.keys = []
general_instructions_key.rt = []
_general_instructions_key_allKeys = []
general_instructions_text.setText(instruction_text)
cprint('On Screen: General instructions...', 'blue', 'on_white')
cprint('Waiting for participant\'s response (d)', 'yellow')
# keep track of which components have finished
general_instructionsComponents = [general_instructions_key, general_instructions_4_continue, general_instructions_text]
for thisComponent in general_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
general_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "general_instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = general_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=general_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *general_instructions_key* updates
    waitOnFlip = False
    if general_instructions_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_key.frameNStart = frameN  # exact frame index
        general_instructions_key.tStart = t  # local t and not account for scr refresh
        general_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_key, 'tStartRefresh')  # time at next scr refresh
        general_instructions_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(general_instructions_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(general_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if general_instructions_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_key.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_key.tStop = t  # not accounting for scr refresh
            general_instructions_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_key, 'tStopRefresh')  # time at next scr refresh
            general_instructions_key.status = FINISHED
    if general_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = general_instructions_key.getKeys(keyList=['d'], waitRelease=False)
        _general_instructions_key_allKeys.extend(theseKeys)
        if len(_general_instructions_key_allKeys):
            general_instructions_key.keys = _general_instructions_key_allKeys[-1].name  # just the last key pressed
            general_instructions_key.rt = _general_instructions_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *general_instructions_4_continue* updates
    if general_instructions_4_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_4_continue.frameNStart = frameN  # exact frame index
        general_instructions_4_continue.tStart = t  # local t and not account for scr refresh
        general_instructions_4_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_4_continue, 'tStartRefresh')  # time at next scr refresh
        general_instructions_4_continue.setAutoDraw(True)
    if general_instructions_4_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_4_continue.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_4_continue.tStop = t  # not accounting for scr refresh
            general_instructions_4_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_4_continue, 'tStopRefresh')  # time at next scr refresh
            general_instructions_4_continue.setAutoDraw(False)
    
    # *general_instructions_text* updates
    if general_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_text.frameNStart = frameN  # exact frame index
        general_instructions_text.tStart = t  # local t and not account for scr refresh
        general_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_text, 'tStartRefresh')  # time at next scr refresh
        general_instructions_text.setAutoDraw(True)
    if general_instructions_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_text.tStop = t  # not accounting for scr refresh
            general_instructions_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_text, 'tStopRefresh')  # time at next scr refresh
            general_instructions_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "general_instructions"-------
for thisComponent in general_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if general_instructions_key.keys in ['', [], None]:  # No response was made
    general_instructions_key.keys = None
thisExp.addData('general_instructions_key.keys',general_instructions_key.keys)
if general_instructions_key.keys != None:  # we had a response
    thisExp.addData('general_instructions_key.rt', general_instructions_key.rt)
thisExp.addData('general_instructions_key.started', general_instructions_key.tStartRefresh)
thisExp.addData('general_instructions_key.stopped', general_instructions_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('general_instructions_4_continue.started', general_instructions_4_continue.tStartRefresh)
thisExp.addData('general_instructions_4_continue.stopped', general_instructions_4_continue.tStopRefresh)
thisExp.addData('general_instructions_text.started', general_instructions_text.tStartRefresh)
thisExp.addData('general_instructions_text.stopped', general_instructions_text.tStopRefresh)
cprint('key pressed: '+ general_instructions_key.keys, 'green')

# ------Prepare to start Routine "start_practice"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
start_practiceComponents = [start_practice_text]
for thisComponent in start_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_practice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = start_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_practice_text* updates
    if start_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_practice_text.frameNStart = frameN  # exact frame index
        start_practice_text.tStart = t  # local t and not account for scr refresh
        start_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_practice_text, 'tStartRefresh')  # time at next scr refresh
        start_practice_text.setAutoDraw(True)
    if start_practice_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_practice_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            start_practice_text.tStop = t  # not accounting for scr refresh
            start_practice_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_practice_text, 'tStopRefresh')  # time at next scr refresh
            start_practice_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_practice"-------
for thisComponent in start_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_practice_text.started', start_practice_text.tStartRefresh)
thisExp.addData('start_practice_text.stopped', start_practice_text.tStopRefresh)

# ------Prepare to start Routine "practice_block_start"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
practice_end = practice_start + 2
practice_selection = np.arange(practice_start, practice_end, step)
practice_block_text.setText(task_name)
# keep track of which components have finished
practice_block_startComponents = [practice_block_text]
for thisComponent in practice_block_startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_block_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_block_start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practice_block_startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_block_startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_block_text* updates
    if practice_block_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_block_text.frameNStart = frameN  # exact frame index
        practice_block_text.tStart = t  # local t and not account for scr refresh
        practice_block_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_block_text, 'tStartRefresh')  # time at next scr refresh
        practice_block_text.setAutoDraw(True)
    if practice_block_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_block_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            practice_block_text.tStop = t  # not accounting for scr refresh
            practice_block_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_block_text, 'tStopRefresh')  # time at next scr refresh
            practice_block_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_block_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_block_start"-------
for thisComponent in practice_block_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
print('Encoding practice loop starting with following parameters:')
thisExp.addData('practice_block_text.started', practice_block_text.tStartRefresh)
thisExp.addData('practice_block_text.stopped', practice_block_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
enc_full_practice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/encoding_full_practice_trials.csv', selection=practice_selection),
    seed=None, name='enc_full_practice')
thisExp.addLoop(enc_full_practice)  # add the loop to the experiment
thisEnc_full_practice = enc_full_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnc_full_practice.rgb)
if thisEnc_full_practice != None:
    for paramName in thisEnc_full_practice:
        exec('{} = thisEnc_full_practice[paramName]'.format(paramName))

for thisEnc_full_practice in enc_full_practice:
    currentLoop = enc_full_practice
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_full_practice.rgb)
    if thisEnc_full_practice != None:
        for paramName in thisEnc_full_practice:
            exec('{} = thisEnc_full_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "enc_fx_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képválogatás'
    elif TrialType=='LOC':
        block_name='Helyválasztás'
    else:
        block_name='Block Unknown'
    enc_fx_cross_practice.setPos((CurrentX, CurrentY))
    enc_fx_key_practice.keys = []
    enc_fx_key_practice.rt = []
    _enc_fx_key_practice_allKeys = []
    enc_fx_text_block_practice.setText(block_name)
    # keep track of which components have finished
    enc_fx_practiceComponents = [enc_fx_interior_practice, enc_fx_cross_practice, enc_fx_key_practice, enc_fx_text_block_practice, enc_fx_instructions_text_practice]
    for thisComponent in enc_fx_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_fx_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_fx_practice"-------
    while continueRoutine:
        # get current time
        t = enc_fx_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_fx_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_fx_interior_practice* updates
        if enc_fx_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_interior_practice.frameNStart = frameN  # exact frame index
            enc_fx_interior_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_interior_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_interior_practice.setAutoDraw(True)
        if enc_fx_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_interior_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_interior_practice.tStop = t  # not accounting for scr refresh
                enc_fx_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_interior_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_interior_practice.setAutoDraw(False)
        
        # *enc_fx_cross_practice* updates
        if enc_fx_cross_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_cross_practice.frameNStart = frameN  # exact frame index
            enc_fx_cross_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_cross_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_cross_practice.setAutoDraw(True)
        if enc_fx_cross_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_cross_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_cross_practice.tStop = t  # not accounting for scr refresh
                enc_fx_cross_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_cross_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_cross_practice.setAutoDraw(False)
        
        # *enc_fx_key_practice* updates
        waitOnFlip = False
        if enc_fx_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_key_practice.frameNStart = frameN  # exact frame index
            enc_fx_key_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_key_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_fx_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_fx_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_fx_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_key_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_key_practice.tStop = t  # not accounting for scr refresh
                enc_fx_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_key_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_key_practice.status = FINISHED
        if enc_fx_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = enc_fx_key_practice.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
            _enc_fx_key_practice_allKeys.extend(theseKeys)
            if len(_enc_fx_key_practice_allKeys):
                enc_fx_key_practice.keys = _enc_fx_key_practice_allKeys[-1].name  # just the last key pressed
                enc_fx_key_practice.rt = _enc_fx_key_practice_allKeys[-1].rt
        
        # *enc_fx_text_block_practice* updates
        if enc_fx_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_text_block_practice.frameNStart = frameN  # exact frame index
            enc_fx_text_block_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_text_block_practice.setAutoDraw(True)
        if enc_fx_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_text_block_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_text_block_practice.tStop = t  # not accounting for scr refresh
                enc_fx_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_text_block_practice.setAutoDraw(False)
        
        # *enc_fx_instructions_text_practice* updates
        if enc_fx_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_instructions_text_practice.frameNStart = frameN  # exact frame index
            enc_fx_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_instructions_text_practice.setAutoDraw(True)
        if enc_fx_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_instructions_text_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_instructions_text_practice.tStop = t  # not accounting for scr refresh
                enc_fx_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_fx_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_fx_practice"-------
    for thisComponent in enc_fx_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_full_practice.addData('enc_fx_interior_practice.started', enc_fx_interior_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_interior_practice.stopped', enc_fx_interior_practice.tStopRefresh)
    enc_full_practice.addData('enc_fx_cross_practice.started', enc_fx_cross_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_cross_practice.stopped', enc_fx_cross_practice.tStopRefresh)
    # check responses
    if enc_fx_key_practice.keys in ['', [], None]:  # No response was made
        enc_fx_key_practice.keys = None
    enc_full_practice.addData('enc_fx_key_practice.keys',enc_fx_key_practice.keys)
    if enc_fx_key_practice.keys != None:  # we had a response
        enc_full_practice.addData('enc_fx_key_practice.rt', enc_fx_key_practice.rt)
    enc_full_practice.addData('enc_fx_key_practice.started', enc_fx_key_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_key_practice.stopped', enc_fx_key_practice.tStopRefresh)
    enc_full_practice.addData('enc_fx_text_block_practice.started', enc_fx_text_block_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_text_block_practice.stopped', enc_fx_text_block_practice.tStopRefresh)
    enc_full_practice.addData('enc_fx_instructions_text_practice.started', enc_fx_instructions_text_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_instructions_text_practice.stopped', enc_fx_instructions_text_practice.tStopRefresh)
    # the Routine "enc_fx_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "enc_trial_practice"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    enc_trial_main_image_practice.setPos((CurrentX, CurrentY))
    enc_trial_main_image_practice.setSize((0.3125, 0.3125*scr_resolution))
    enc_trial_main_image_practice.setImage(CurrentImage)
    enc_trial_key_practice.keys = []
    enc_trial_key_practice.rt = []
    _enc_trial_key_practice_allKeys = []
    enc_trial_text_block_practice.setText(block_name)
    # keep track of which components have finished
    enc_trial_practiceComponents = [enc_trial_interior_practice, enc_trial_main_image_practice, enc_trial_key_practice, enc_trial_text_block_practice, enc_trial_instructions_text_practice]
    for thisComponent in enc_trial_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_trial_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = enc_trial_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_trial_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_trial_interior_practice* updates
        if enc_trial_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_interior_practice.frameNStart = frameN  # exact frame index
            enc_trial_interior_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_interior_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_interior_practice.setAutoDraw(True)
        if enc_trial_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_interior_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_interior_practice.tStop = t  # not accounting for scr refresh
                enc_trial_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_interior_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_interior_practice.setAutoDraw(False)
        
        # *enc_trial_main_image_practice* updates
        if enc_trial_main_image_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_main_image_practice.frameNStart = frameN  # exact frame index
            enc_trial_main_image_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_main_image_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_main_image_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_main_image_practice.setAutoDraw(True)
        if enc_trial_main_image_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_main_image_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_main_image_practice.tStop = t  # not accounting for scr refresh
                enc_trial_main_image_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_main_image_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_main_image_practice.setAutoDraw(False)
        
        # *enc_trial_key_practice* updates
        waitOnFlip = False
        if enc_trial_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_key_practice.frameNStart = frameN  # exact frame index
            enc_trial_key_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_key_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_trial_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_trial_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_trial_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_key_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_key_practice.tStop = t  # not accounting for scr refresh
                enc_trial_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_key_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_key_practice.status = FINISHED
        if enc_trial_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = enc_trial_key_practice.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
            _enc_trial_key_practice_allKeys.extend(theseKeys)
            if len(_enc_trial_key_practice_allKeys):
                enc_trial_key_practice.keys = _enc_trial_key_practice_allKeys[-1].name  # just the last key pressed
                enc_trial_key_practice.rt = _enc_trial_key_practice_allKeys[-1].rt
        
        # *enc_trial_text_block_practice* updates
        if enc_trial_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_text_block_practice.frameNStart = frameN  # exact frame index
            enc_trial_text_block_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_text_block_practice.setAutoDraw(True)
        if enc_trial_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_text_block_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_text_block_practice.tStop = t  # not accounting for scr refresh
                enc_trial_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_text_block_practice.setAutoDraw(False)
        
        # *enc_trial_instructions_text_practice* updates
        if enc_trial_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_instructions_text_practice.frameNStart = frameN  # exact frame index
            enc_trial_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_instructions_text_practice.setAutoDraw(True)
        if enc_trial_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_instructions_text_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_instructions_text_practice.tStop = t  # not accounting for scr refresh
                enc_trial_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_trial_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_trial_practice"-------
    for thisComponent in enc_trial_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_full_practice.addData('enc_trial_interior_practice.started', enc_trial_interior_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_interior_practice.stopped', enc_trial_interior_practice.tStopRefresh)
    enc_full_practice.addData('enc_trial_main_image_practice.started', enc_trial_main_image_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_main_image_practice.stopped', enc_trial_main_image_practice.tStopRefresh)
    # check responses
    if enc_trial_key_practice.keys in ['', [], None]:  # No response was made
        enc_trial_key_practice.keys = None
    enc_full_practice.addData('enc_trial_key_practice.keys',enc_trial_key_practice.keys)
    if enc_trial_key_practice.keys != None:  # we had a response
        enc_full_practice.addData('enc_trial_key_practice.rt', enc_trial_key_practice.rt)
    enc_full_practice.addData('enc_trial_key_practice.started', enc_trial_key_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_key_practice.stopped', enc_trial_key_practice.tStopRefresh)
    enc_full_practice.addData('enc_trial_text_block_practice.started', enc_trial_text_block_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_text_block_practice.stopped', enc_trial_text_block_practice.tStopRefresh)
    enc_full_practice.addData('enc_trial_instructions_text_practice.started', enc_trial_instructions_text_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_instructions_text_practice.stopped', enc_trial_instructions_text_practice.tStopRefresh)
    
    # ------Prepare to start Routine "enc_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    response = enc_trial_key_practice.keys
    feedback_text = ''
    if response=='b':
        feedback_text = 'Az Ön válasza:\nA kép nem marad.'
    elif response=='c':
        feedback_text = 'Az Ön válasza:\nA kép marad.'
    elif response=='a' or response=='d':
        feedback_text = 'Érvénytelen válasz.\nHasználja a mutatóujját!'
    else:
        feedback_text = 'Nem adott választ.'
    print(feedback_text)
    enc_practice_feedback_image.setPos((CurrentX, CurrentY))
    enc_practice_feedback_image.setSize((0.3125, 0.3125*scr_resolution))
    enc_practice_feedback_image.setImage(CurrentImage)
    enc_practice_feedback_text.setPos((CurrentX, CurrentY - 0.4))
    enc_practice_feedback_text.setText(feedback_text)
    enc_practice_feedback_block.setText(block_name)
    # keep track of which components have finished
    enc_practice_feedbackComponents = [enc_practice_feedback_interior, enc_practice_feedback_image, enc_practice_feedback_text, enc_practice_feedback_block]
    for thisComponent in enc_practice_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_practice_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = enc_practice_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_practice_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_practice_feedback_interior* updates
        if enc_practice_feedback_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_interior.frameNStart = frameN  # exact frame index
            enc_practice_feedback_interior.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_interior, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_interior.setAutoDraw(True)
        if enc_practice_feedback_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_interior.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_interior.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_interior, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_interior.setAutoDraw(False)
        
        # *enc_practice_feedback_image* updates
        if enc_practice_feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_image.frameNStart = frameN  # exact frame index
            enc_practice_feedback_image.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_image, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_image.setAutoDraw(True)
        if enc_practice_feedback_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_image.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_image.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_image, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_image.setAutoDraw(False)
        
        # *enc_practice_feedback_text* updates
        if enc_practice_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_text.frameNStart = frameN  # exact frame index
            enc_practice_feedback_text.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_text, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_text.setAutoDraw(True)
        if enc_practice_feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_text.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_text, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_text.setAutoDraw(False)
        
        # *enc_practice_feedback_block* updates
        if enc_practice_feedback_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_block.frameNStart = frameN  # exact frame index
            enc_practice_feedback_block.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_block, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_block.setAutoDraw(True)
        if enc_practice_feedback_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_block.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_block.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_block, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_block.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_practice_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_practice_feedback"-------
    for thisComponent in enc_practice_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_full_practice.addData('enc_practice_feedback_interior.started', enc_practice_feedback_interior.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_interior.stopped', enc_practice_feedback_interior.tStopRefresh)
    enc_full_practice.addData('enc_practice_feedback_image.started', enc_practice_feedback_image.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_image.stopped', enc_practice_feedback_image.tStopRefresh)
    enc_full_practice.addData('enc_practice_feedback_text.started', enc_practice_feedback_text.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_text.stopped', enc_practice_feedback_text.tStopRefresh)
    enc_full_practice.addData('enc_practice_feedback_block.started', enc_practice_feedback_block.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_block.stopped', enc_practice_feedback_block.tStopRefresh)
# completed 1 repeats of 'enc_full_practice'


# ------Prepare to start Routine "recognition_title"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
block_name = ''
if TrialType=='OBJ':
    block_name='Képfelismerés'
elif TrialType=='LOC':
    block_name='Helyfelismerés'
else:
    block_name='Block Unknown'
start_recognition_text.setText(block_name)
# keep track of which components have finished
recognition_titleComponents = [start_recognition_text]
for thisComponent in recognition_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
recognition_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "recognition_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = recognition_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=recognition_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_recognition_text* updates
    if start_recognition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_recognition_text.frameNStart = frameN  # exact frame index
        start_recognition_text.tStart = t  # local t and not account for scr refresh
        start_recognition_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_recognition_text, 'tStartRefresh')  # time at next scr refresh
        start_recognition_text.setAutoDraw(True)
    if start_recognition_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_recognition_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            start_recognition_text.tStop = t  # not accounting for scr refresh
            start_recognition_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_recognition_text, 'tStopRefresh')  # time at next scr refresh
            start_recognition_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in recognition_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "recognition_title"-------
for thisComponent in recognition_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_recognition_text.started', start_recognition_text.tStartRefresh)
thisExp.addData('start_recognition_text.stopped', start_recognition_text.tStopRefresh)
print('Recognition practice loop starting with following parameters:')

# set up handler to look after randomisation of conditions etc
rec_full_practice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/recognition_full_practice_trials.csv', selection=practice_selection),
    seed=None, name='rec_full_practice')
thisExp.addLoop(rec_full_practice)  # add the loop to the experiment
thisRec_full_practice = rec_full_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRec_full_practice.rgb)
if thisRec_full_practice != None:
    for paramName in thisRec_full_practice:
        exec('{} = thisRec_full_practice[paramName]'.format(paramName))

for thisRec_full_practice in rec_full_practice:
    currentLoop = rec_full_practice
    # abbreviate parameter names if possible (e.g. rgb = thisRec_full_practice.rgb)
    if thisRec_full_practice != None:
        for paramName in thisRec_full_practice:
            exec('{} = thisRec_full_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rec_fx_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képfelismerés'
    elif TrialType=='LOC':
        block_name='Helyfelismerés'
    else:
        block_name='Block Unknown'
    rec_fx_cross_practice.setPos((CurrentX, CurrentY))
    rec_fx_key_practice.keys = []
    rec_fx_key_practice.rt = []
    _rec_fx_key_practice_allKeys = []
    rec_fx_text_block_practice.setText(block_name
)
    # keep track of which components have finished
    rec_fx_practiceComponents = [rec_fx_interior_practice, rec_fx_cross_practice, rec_fx_key_practice, rec_fx_text_block_practice, rec_fx_instructions_text_practice]
    for thisComponent in rec_fx_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rec_fx_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rec_fx_practice"-------
    while continueRoutine:
        # get current time
        t = rec_fx_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rec_fx_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_fx_interior_practice* updates
        if rec_fx_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_interior_practice.frameNStart = frameN  # exact frame index
            rec_fx_interior_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_interior_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_interior_practice.setAutoDraw(True)
        if rec_fx_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_interior_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_interior_practice.tStop = t  # not accounting for scr refresh
                rec_fx_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_interior_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_interior_practice.setAutoDraw(False)
        
        # *rec_fx_cross_practice* updates
        if rec_fx_cross_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_cross_practice.frameNStart = frameN  # exact frame index
            rec_fx_cross_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_cross_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_cross_practice.setAutoDraw(True)
        if rec_fx_cross_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_cross_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_cross_practice.tStop = t  # not accounting for scr refresh
                rec_fx_cross_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_cross_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_cross_practice.setAutoDraw(False)
        
        # *rec_fx_key_practice* updates
        waitOnFlip = False
        if rec_fx_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_key_practice.frameNStart = frameN  # exact frame index
            rec_fx_key_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_key_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rec_fx_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rec_fx_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rec_fx_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_key_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_key_practice.tStop = t  # not accounting for scr refresh
                rec_fx_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_key_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_key_practice.status = FINISHED
        if rec_fx_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = rec_fx_key_practice.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
            _rec_fx_key_practice_allKeys.extend(theseKeys)
            if len(_rec_fx_key_practice_allKeys):
                rec_fx_key_practice.keys = _rec_fx_key_practice_allKeys[-1].name  # just the last key pressed
                rec_fx_key_practice.rt = _rec_fx_key_practice_allKeys[-1].rt
        
        # *rec_fx_text_block_practice* updates
        if rec_fx_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_text_block_practice.frameNStart = frameN  # exact frame index
            rec_fx_text_block_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_text_block_practice.setAutoDraw(True)
        if rec_fx_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_text_block_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_text_block_practice.tStop = t  # not accounting for scr refresh
                rec_fx_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_text_block_practice.setAutoDraw(False)
        
        # *rec_fx_instructions_text_practice* updates
        if rec_fx_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_instructions_text_practice.frameNStart = frameN  # exact frame index
            rec_fx_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_instructions_text_practice.setAutoDraw(True)
        if rec_fx_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_instructions_text_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_instructions_text_practice.tStop = t  # not accounting for scr refresh
                rec_fx_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rec_fx_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rec_fx_practice"-------
    for thisComponent in rec_fx_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_full_practice.addData('rec_fx_interior_practice.started', rec_fx_interior_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_interior_practice.stopped', rec_fx_interior_practice.tStopRefresh)
    rec_full_practice.addData('rec_fx_cross_practice.started', rec_fx_cross_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_cross_practice.stopped', rec_fx_cross_practice.tStopRefresh)
    # check responses
    if rec_fx_key_practice.keys in ['', [], None]:  # No response was made
        rec_fx_key_practice.keys = None
    rec_full_practice.addData('rec_fx_key_practice.keys',rec_fx_key_practice.keys)
    if rec_fx_key_practice.keys != None:  # we had a response
        rec_full_practice.addData('rec_fx_key_practice.rt', rec_fx_key_practice.rt)
    rec_full_practice.addData('rec_fx_key_practice.started', rec_fx_key_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_key_practice.stopped', rec_fx_key_practice.tStopRefresh)
    rec_full_practice.addData('rec_fx_text_block_practice.started', rec_fx_text_block_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_text_block_practice.stopped', rec_fx_text_block_practice.tStopRefresh)
    rec_full_practice.addData('rec_fx_instructions_text_practice.started', rec_fx_instructions_text_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_instructions_text_practice.stopped', rec_fx_instructions_text_practice.tStopRefresh)
    # the Routine "rec_fx_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rec_trial_practice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    rec_trial_main_image_practice.setPos((CurrentX, CurrentY))
    rec_trial_main_image_practice.setSize((0.3125, 0.3125*scr_resolution))
    rec_trial_main_image_practice.setImage(CurrentImage)
    rec_trial_key_practice.keys = []
    rec_trial_key_practice.rt = []
    _rec_trial_key_practice_allKeys = []
    rec_trial_text_block_practice.setText(block_name)
    # keep track of which components have finished
    rec_trial_practiceComponents = [rec_trial_interior_practice, rec_trial_main_image_practice, rec_trial_key_practice, rec_trial_text_block_practice, rec_trial_instructions_text_practice]
    for thisComponent in rec_trial_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rec_trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rec_trial_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rec_trial_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rec_trial_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_trial_interior_practice* updates
        if rec_trial_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_interior_practice.frameNStart = frameN  # exact frame index
            rec_trial_interior_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_interior_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_interior_practice.setAutoDraw(True)
        if rec_trial_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_interior_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_interior_practice.tStop = t  # not accounting for scr refresh
                rec_trial_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_interior_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_interior_practice.setAutoDraw(False)
        
        # *rec_trial_main_image_practice* updates
        if rec_trial_main_image_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_main_image_practice.frameNStart = frameN  # exact frame index
            rec_trial_main_image_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_main_image_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_main_image_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_main_image_practice.setAutoDraw(True)
        if rec_trial_main_image_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_main_image_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_main_image_practice.tStop = t  # not accounting for scr refresh
                rec_trial_main_image_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_main_image_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_main_image_practice.setAutoDraw(False)
        
        # *rec_trial_key_practice* updates
        waitOnFlip = False
        if rec_trial_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_key_practice.frameNStart = frameN  # exact frame index
            rec_trial_key_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_key_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rec_trial_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rec_trial_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rec_trial_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_key_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_key_practice.tStop = t  # not accounting for scr refresh
                rec_trial_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_key_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_key_practice.status = FINISHED
        if rec_trial_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = rec_trial_key_practice.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
            _rec_trial_key_practice_allKeys.extend(theseKeys)
            if len(_rec_trial_key_practice_allKeys):
                rec_trial_key_practice.keys = _rec_trial_key_practice_allKeys[-1].name  # just the last key pressed
                rec_trial_key_practice.rt = _rec_trial_key_practice_allKeys[-1].rt
        
        # *rec_trial_text_block_practice* updates
        if rec_trial_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_text_block_practice.frameNStart = frameN  # exact frame index
            rec_trial_text_block_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_text_block_practice.setAutoDraw(True)
        if rec_trial_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_text_block_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_text_block_practice.tStop = t  # not accounting for scr refresh
                rec_trial_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_text_block_practice.setAutoDraw(False)
        
        # *rec_trial_instructions_text_practice* updates
        if rec_trial_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_instructions_text_practice.frameNStart = frameN  # exact frame index
            rec_trial_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_instructions_text_practice.setAutoDraw(True)
        if rec_trial_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_instructions_text_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_instructions_text_practice.tStop = t  # not accounting for scr refresh
                rec_trial_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rec_trial_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rec_trial_practice"-------
    for thisComponent in rec_trial_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_full_practice.addData('rec_trial_interior_practice.started', rec_trial_interior_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_interior_practice.stopped', rec_trial_interior_practice.tStopRefresh)
    rec_full_practice.addData('rec_trial_main_image_practice.started', rec_trial_main_image_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_main_image_practice.stopped', rec_trial_main_image_practice.tStopRefresh)
    # check responses
    if rec_trial_key_practice.keys in ['', [], None]:  # No response was made
        rec_trial_key_practice.keys = None
    rec_full_practice.addData('rec_trial_key_practice.keys',rec_trial_key_practice.keys)
    if rec_trial_key_practice.keys != None:  # we had a response
        rec_full_practice.addData('rec_trial_key_practice.rt', rec_trial_key_practice.rt)
    rec_full_practice.addData('rec_trial_key_practice.started', rec_trial_key_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_key_practice.stopped', rec_trial_key_practice.tStopRefresh)
    rec_full_practice.addData('rec_trial_text_block_practice.started', rec_trial_text_block_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_text_block_practice.stopped', rec_trial_text_block_practice.tStopRefresh)
    rec_full_practice.addData('rec_trial_instructions_text_practice.started', rec_trial_instructions_text_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_instructions_text_practice.stopped', rec_trial_instructions_text_practice.tStopRefresh)
    
    # ------Prepare to start Routine "rec_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    correct_response = ''
    if StimType == 'FOIL':
        correct_response = 'A helyes válasz: Új'
    elif StimType == 'LURE':
        correct_response = 'A helyes válasz: Új'
    elif StimType == 'TARGET':
        correct_response = 'A helyes válasz: Régi'
    
    response = rec_trial_key_practice.keys
    if response=='b':
        feedback = 'Az Ön válasza: Régi'
    elif response=='c':
        feedback = 'Az Ön válasza: Új'
    elif response=='a' or response=='d':
        feedback = 'Érvénytelen. Használja a mutatóujját!'
    else:
        feedback = 'Nem adott választ.'
        
    feedback_text = correct_response +'\n'+ feedback
    print(feedback_text)
    
    rec_practice_feedback_text.setText(feedback_text)
    # keep track of which components have finished
    rec_practice_feedbackComponents = [rec_practice_feedback_text]
    for thisComponent in rec_practice_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rec_practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rec_practice_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rec_practice_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rec_practice_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_practice_feedback_text* updates
        if rec_practice_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_practice_feedback_text.frameNStart = frameN  # exact frame index
            rec_practice_feedback_text.tStart = t  # local t and not account for scr refresh
            rec_practice_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_practice_feedback_text, 'tStartRefresh')  # time at next scr refresh
            rec_practice_feedback_text.setAutoDraw(True)
        if rec_practice_feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_practice_feedback_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_practice_feedback_text.tStop = t  # not accounting for scr refresh
                rec_practice_feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_practice_feedback_text, 'tStopRefresh')  # time at next scr refresh
                rec_practice_feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rec_practice_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rec_practice_feedback"-------
    for thisComponent in rec_practice_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_full_practice.addData('rec_practice_feedback_text.started', rec_practice_feedback_text.tStartRefresh)
    rec_full_practice.addData('rec_practice_feedback_text.stopped', rec_practice_feedback_text.tStopRefresh)
# completed 1 repeats of 'rec_full_practice'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
cprint('On screen: End of practice.', 'blue', 'on_white')
cprint('Waiting for participant\'s response (d)', 'yellow')
block_counter = 0
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
coming_up_next_text.setText('A feladat következik. A feladat során már nem kap visszajelzést. ')
# keep track of which components have finished
end_practiceComponents = [end_practice_text, end_practice_key, end_practice_continue, coming_up_next_text]
for thisComponent in end_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_practice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_practice_text* updates
    if end_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_text.frameNStart = frameN  # exact frame index
        end_practice_text.tStart = t  # local t and not account for scr refresh
        end_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_text, 'tStartRefresh')  # time at next scr refresh
        end_practice_text.setAutoDraw(True)
    if end_practice_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_practice_text.tStartRefresh + 600.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_text.tStop = t  # not accounting for scr refresh
            end_practice_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_text, 'tStopRefresh')  # time at next scr refresh
            end_practice_text.setAutoDraw(False)
    
    # *end_practice_key* updates
    waitOnFlip = False
    if end_practice_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_key.frameNStart = frameN  # exact frame index
        end_practice_key.tStart = t  # local t and not account for scr refresh
        end_practice_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_key, 'tStartRefresh')  # time at next scr refresh
        end_practice_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_practice_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_practice_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_practice_key.tStartRefresh + 599.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_key.tStop = t  # not accounting for scr refresh
            end_practice_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_key, 'tStopRefresh')  # time at next scr refresh
            end_practice_key.status = FINISHED
    if end_practice_key.status == STARTED and not waitOnFlip:
        theseKeys = end_practice_key.getKeys(keyList=['d', 'right'], waitRelease=False)
        _end_practice_key_allKeys.extend(theseKeys)
        if len(_end_practice_key_allKeys):
            end_practice_key.keys = _end_practice_key_allKeys[-1].name  # just the last key pressed
            end_practice_key.rt = _end_practice_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *end_practice_continue* updates
    if end_practice_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_continue.frameNStart = frameN  # exact frame index
        end_practice_continue.tStart = t  # local t and not account for scr refresh
        end_practice_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_continue, 'tStartRefresh')  # time at next scr refresh
        end_practice_continue.setAutoDraw(True)
    if end_practice_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_practice_continue.tStartRefresh + 599.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_continue.tStop = t  # not accounting for scr refresh
            end_practice_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_continue, 'tStopRefresh')  # time at next scr refresh
            end_practice_continue.setAutoDraw(False)
    
    # *coming_up_next_text* updates
    if coming_up_next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        coming_up_next_text.frameNStart = frameN  # exact frame index
        coming_up_next_text.tStart = t  # local t and not account for scr refresh
        coming_up_next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(coming_up_next_text, 'tStartRefresh')  # time at next scr refresh
        coming_up_next_text.setAutoDraw(True)
    if coming_up_next_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > coming_up_next_text.tStartRefresh + 600.0-frameTolerance:
            # keep track of stop time/frame for later
            coming_up_next_text.tStop = t  # not accounting for scr refresh
            coming_up_next_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(coming_up_next_text, 'tStopRefresh')  # time at next scr refresh
            coming_up_next_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_practice"-------
for thisComponent in end_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
cprint('key pressed: '+ end_practice_key.keys, 'green')
print('Scanner Run loop starting with following parameters:')
thisExp.addData('end_practice_text.started', end_practice_text.tStartRefresh)
thisExp.addData('end_practice_text.stopped', end_practice_text.tStopRefresh)
# check responses
if end_practice_key.keys in ['', [], None]:  # No response was made
    end_practice_key.keys = None
thisExp.addData('end_practice_key.keys',end_practice_key.keys)
if end_practice_key.keys != None:  # we had a response
    thisExp.addData('end_practice_key.rt', end_practice_key.rt)
thisExp.addData('end_practice_key.started', end_practice_key.tStartRefresh)
thisExp.addData('end_practice_key.stopped', end_practice_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('end_practice_continue.started', end_practice_continue.tStartRefresh)
thisExp.addData('end_practice_continue.stopped', end_practice_continue.tStopRefresh)
thisExp.addData('coming_up_next_text.started', coming_up_next_text.tStartRefresh)
thisExp.addData('coming_up_next_text.stopped', coming_up_next_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
run = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(enc_table, selection=block_name_selection),
    seed=None, name='run')
thisExp.addLoop(run)  # add the loop to the experiment
thisRun = run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in run:
    currentLoop = run
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "wait_for_last_scan"-------
    continueRoutine = True
    routineTimer.add(600.000000)
    # update component parameters for each repeat
    cprint('On Screen: A vizsgálatvezető előkészíti a scannert', 'blue', 'on_white')
    cprint('Experimenter: Ready for scanning? Hit SPACE or -> to continue.', 'red')
    wait_for_last_scan_continue.keys = []
    wait_for_last_scan_continue.rt = []
    _wait_for_last_scan_continue_allKeys = []
    # keep track of which components have finished
    wait_for_last_scanComponents = [wait_for_last_scan_text, wait_for_last_scan_continue]
    for thisComponent in wait_for_last_scanComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wait_for_last_scanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wait_for_last_scan"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wait_for_last_scanClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wait_for_last_scanClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_for_last_scan_text* updates
        if wait_for_last_scan_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_for_last_scan_text.frameNStart = frameN  # exact frame index
            wait_for_last_scan_text.tStart = t  # local t and not account for scr refresh
            wait_for_last_scan_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_for_last_scan_text, 'tStartRefresh')  # time at next scr refresh
            wait_for_last_scan_text.setAutoDraw(True)
        if wait_for_last_scan_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_for_last_scan_text.tStartRefresh + 600.0-frameTolerance:
                # keep track of stop time/frame for later
                wait_for_last_scan_text.tStop = t  # not accounting for scr refresh
                wait_for_last_scan_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait_for_last_scan_text, 'tStopRefresh')  # time at next scr refresh
                wait_for_last_scan_text.setAutoDraw(False)
        
        # *wait_for_last_scan_continue* updates
        waitOnFlip = False
        if wait_for_last_scan_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            wait_for_last_scan_continue.frameNStart = frameN  # exact frame index
            wait_for_last_scan_continue.tStart = t  # local t and not account for scr refresh
            wait_for_last_scan_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_for_last_scan_continue, 'tStartRefresh')  # time at next scr refresh
            wait_for_last_scan_continue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wait_for_last_scan_continue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wait_for_last_scan_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wait_for_last_scan_continue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_for_last_scan_continue.tStartRefresh + 599-frameTolerance:
                # keep track of stop time/frame for later
                wait_for_last_scan_continue.tStop = t  # not accounting for scr refresh
                wait_for_last_scan_continue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait_for_last_scan_continue, 'tStopRefresh')  # time at next scr refresh
                wait_for_last_scan_continue.status = FINISHED
        if wait_for_last_scan_continue.status == STARTED and not waitOnFlip:
            theseKeys = wait_for_last_scan_continue.getKeys(keyList=['right', 'space'], waitRelease=False)
            _wait_for_last_scan_continue_allKeys.extend(theseKeys)
            if len(_wait_for_last_scan_continue_allKeys):
                wait_for_last_scan_continue.keys = _wait_for_last_scan_continue_allKeys[-1].name  # just the last key pressed
                wait_for_last_scan_continue.rt = _wait_for_last_scan_continue_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait_for_last_scanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wait_for_last_scan"-------
    for thisComponent in wait_for_last_scanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('wait_for_last_scan_text.started', wait_for_last_scan_text.tStartRefresh)
    run.addData('wait_for_last_scan_text.stopped', wait_for_last_scan_text.tStopRefresh)
    # check responses
    if wait_for_last_scan_continue.keys in ['', [], None]:  # No response was made
        wait_for_last_scan_continue.keys = None
    run.addData('wait_for_last_scan_continue.keys',wait_for_last_scan_continue.keys)
    if wait_for_last_scan_continue.keys != None:  # we had a response
        run.addData('wait_for_last_scan_continue.rt', wait_for_last_scan_continue.rt)
    run.addData('wait_for_last_scan_continue.started', wait_for_last_scan_continue.tStartRefresh)
    run.addData('wait_for_last_scan_continue.stopped', wait_for_last_scan_continue.tStopRefresh)
    
    # ------Prepare to start Routine "start_MR"-------
    continueRoutine = True
    routineTimer.add(1200.000000)
    # update component parameters for each repeat
    cprint('Experimenter: Waiting for trigger. Start scanning...', 'yellow')
    MR_trigger.keys = []
    MR_trigger.rt = []
    _MR_trigger_allKeys = []
    # keep track of which components have finished
    start_MRComponents = [start_MR_text, MR_trigger]
    for thisComponent in start_MRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_MRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_MR"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_MRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_MRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_MR_text* updates
        if start_MR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_MR_text.frameNStart = frameN  # exact frame index
            start_MR_text.tStart = t  # local t and not account for scr refresh
            start_MR_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_MR_text, 'tStartRefresh')  # time at next scr refresh
            start_MR_text.setAutoDraw(True)
        if start_MR_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_MR_text.tStartRefresh + 1200.0-frameTolerance:
                # keep track of stop time/frame for later
                start_MR_text.tStop = t  # not accounting for scr refresh
                start_MR_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_MR_text, 'tStopRefresh')  # time at next scr refresh
                start_MR_text.setAutoDraw(False)
        
        # *MR_trigger* updates
        waitOnFlip = False
        if MR_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MR_trigger.frameNStart = frameN  # exact frame index
            MR_trigger.tStart = t  # local t and not account for scr refresh
            MR_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MR_trigger, 'tStartRefresh')  # time at next scr refresh
            MR_trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MR_trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MR_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MR_trigger.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MR_trigger.tStartRefresh + 1200.0-frameTolerance:
                # keep track of stop time/frame for later
                MR_trigger.tStop = t  # not accounting for scr refresh
                MR_trigger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(MR_trigger, 'tStopRefresh')  # time at next scr refresh
                MR_trigger.status = FINISHED
        if MR_trigger.status == STARTED and not waitOnFlip:
            theseKeys = MR_trigger.getKeys(keyList=['s'], waitRelease=False)
            _MR_trigger_allKeys.extend(theseKeys)
            if len(_MR_trigger_allKeys):
                MR_trigger.keys = _MR_trigger_allKeys[0].name  # just the first key pressed
                MR_trigger.rt = _MR_trigger_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_MRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_MR"-------
    for thisComponent in start_MRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trigger_time = globalClock.getTime()
    thisExp.addData('trigger_time', trigger_time)
    if enc_end==0 or enc_end==152:
        event.globalKeys.add(key=trigger_key, 
                                               func=get_trigger_time, 
                                               func_args=[trigger_time])
    cprint('Trigger recieved.', 'green')
    run.addData('start_MR_text.started', start_MR_text.tStartRefresh)
    run.addData('start_MR_text.stopped', start_MR_text.tStopRefresh)
    # check responses
    if MR_trigger.keys in ['', [], None]:  # No response was made
        MR_trigger.keys = None
    run.addData('MR_trigger.keys',MR_trigger.keys)
    if MR_trigger.keys != None:  # we had a response
        run.addData('MR_trigger.rt', MR_trigger.rt)
    run.addData('MR_trigger.started', MR_trigger.tStartRefresh)
    run.addData('MR_trigger.stopped', MR_trigger.tStopRefresh)
    
    # ------Prepare to start Routine "start_run"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    run_counter = run_counter + 1
    # keep track of which components have finished
    start_runComponents = [start_enc_run_text]
    for thisComponent in start_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_enc_run_text* updates
        if start_enc_run_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_enc_run_text.frameNStart = frameN  # exact frame index
            start_enc_run_text.tStart = t  # local t and not account for scr refresh
            start_enc_run_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_enc_run_text, 'tStartRefresh')  # time at next scr refresh
            start_enc_run_text.setAutoDraw(True)
        if start_enc_run_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_enc_run_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                start_enc_run_text.tStop = t  # not accounting for scr refresh
                start_enc_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_enc_run_text, 'tStopRefresh')  # time at next scr refresh
                start_enc_run_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_run"-------
    for thisComponent in start_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('start_enc_run_text.started', start_enc_run_text.tStartRefresh)
    run.addData('start_enc_run_text.stopped', start_enc_run_text.tStopRefresh)
    
    # ------Prepare to start Routine "encoding_title"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képválasztás'
    elif TrialType=='LOC':
        block_name='Helyválasztás'
    else:
        block_name='Block Unknown'
    encoding_title_text.setText(block_name)
    # keep track of which components have finished
    encoding_titleComponents = [encoding_title_text]
    for thisComponent in encoding_titleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encoding_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "encoding_title"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = encoding_titleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encoding_titleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encoding_title_text* updates
        if encoding_title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_title_text.frameNStart = frameN  # exact frame index
            encoding_title_text.tStart = t  # local t and not account for scr refresh
            encoding_title_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_title_text, 'tStartRefresh')  # time at next scr refresh
            encoding_title_text.setAutoDraw(True)
        if encoding_title_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_title_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                encoding_title_text.tStop = t  # not accounting for scr refresh
                encoding_title_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_title_text, 'tStopRefresh')  # time at next scr refresh
                encoding_title_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encoding_titleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "encoding_title"-------
    for thisComponent in encoding_titleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('encoding_title_text.started', encoding_title_text.tStartRefresh)
    run.addData('encoding_title_text.stopped', encoding_title_text.tStopRefresh)
    
    # ------Prepare to start Routine "init_blocks"-------
    continueRoutine = True
    # update component parameters for each repeat
    rec_start = rec_end
    rec_end = rec_start + 36
    rec_selection = np.arange(rec_start,rec_end, step)
    enc_start = enc_end
    enc_end = enc_start + 76
    enc_selection = np.arange(enc_start, enc_end, step)
    # keep track of which components have finished
    init_blocksComponents = []
    for thisComponent in init_blocksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    init_blocksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "init_blocks"-------
    while continueRoutine:
        # get current time
        t = init_blocksClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=init_blocksClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in init_blocksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "init_blocks"-------
    for thisComponent in init_blocksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "init_blocks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "encoding_baseline"-------
    continueRoutine = True
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képválogatás'
    elif TrialType=='LOC':
        block_name='Helyválasztás'
    else:
        block_name='Block Unknown'
    encoding_baseline_text_block.setText(block_name)
    baseline_enc_fx_cross.setPos((CurrentX, CurrentY))
    cprint('On Screen: Encoding baseline - Start', 'blue', 'on_white')
    enc_missing = 0
    # keep track of which components have finished
    encoding_baselineComponents = [encoding_baseline_interior, encoding_baseline_text_block, encoding_baseline_instructions_text, baseline_enc_fx_cross]
    for thisComponent in encoding_baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encoding_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "encoding_baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = encoding_baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encoding_baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encoding_baseline_interior* updates
        if encoding_baseline_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_baseline_interior.frameNStart = frameN  # exact frame index
            encoding_baseline_interior.tStart = t  # local t and not account for scr refresh
            encoding_baseline_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_baseline_interior, 'tStartRefresh')  # time at next scr refresh
            encoding_baseline_interior.setAutoDraw(True)
        if encoding_baseline_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_baseline_interior.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                encoding_baseline_interior.tStop = t  # not accounting for scr refresh
                encoding_baseline_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_baseline_interior, 'tStopRefresh')  # time at next scr refresh
                encoding_baseline_interior.setAutoDraw(False)
        
        # *encoding_baseline_text_block* updates
        if encoding_baseline_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_baseline_text_block.frameNStart = frameN  # exact frame index
            encoding_baseline_text_block.tStart = t  # local t and not account for scr refresh
            encoding_baseline_text_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_baseline_text_block, 'tStartRefresh')  # time at next scr refresh
            encoding_baseline_text_block.setAutoDraw(True)
        if encoding_baseline_text_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_baseline_text_block.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                encoding_baseline_text_block.tStop = t  # not accounting for scr refresh
                encoding_baseline_text_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_baseline_text_block, 'tStopRefresh')  # time at next scr refresh
                encoding_baseline_text_block.setAutoDraw(False)
        
        # *encoding_baseline_instructions_text* updates
        if encoding_baseline_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_baseline_instructions_text.frameNStart = frameN  # exact frame index
            encoding_baseline_instructions_text.tStart = t  # local t and not account for scr refresh
            encoding_baseline_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_baseline_instructions_text, 'tStartRefresh')  # time at next scr refresh
            encoding_baseline_instructions_text.setAutoDraw(True)
        if encoding_baseline_instructions_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_baseline_instructions_text.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                encoding_baseline_instructions_text.tStop = t  # not accounting for scr refresh
                encoding_baseline_instructions_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_baseline_instructions_text, 'tStopRefresh')  # time at next scr refresh
                encoding_baseline_instructions_text.setAutoDraw(False)
        
        # *baseline_enc_fx_cross* updates
        if baseline_enc_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_enc_fx_cross.frameNStart = frameN  # exact frame index
            baseline_enc_fx_cross.tStart = t  # local t and not account for scr refresh
            baseline_enc_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_enc_fx_cross, 'tStartRefresh')  # time at next scr refresh
            baseline_enc_fx_cross.setAutoDraw(True)
        if baseline_enc_fx_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_enc_fx_cross.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                baseline_enc_fx_cross.tStop = t  # not accounting for scr refresh
                baseline_enc_fx_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baseline_enc_fx_cross, 'tStopRefresh')  # time at next scr refresh
                baseline_enc_fx_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encoding_baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "encoding_baseline"-------
    for thisComponent in encoding_baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('encoding_baseline_interior.started', encoding_baseline_interior.tStartRefresh)
    run.addData('encoding_baseline_interior.stopped', encoding_baseline_interior.tStopRefresh)
    run.addData('encoding_baseline_text_block.started', encoding_baseline_text_block.tStartRefresh)
    run.addData('encoding_baseline_text_block.stopped', encoding_baseline_text_block.tStopRefresh)
    run.addData('encoding_baseline_instructions_text.started', encoding_baseline_instructions_text.tStartRefresh)
    run.addData('encoding_baseline_instructions_text.stopped', encoding_baseline_instructions_text.tStopRefresh)
    run.addData('baseline_enc_fx_cross.started', baseline_enc_fx_cross.tStartRefresh)
    run.addData('baseline_enc_fx_cross.stopped', baseline_enc_fx_cross.tStopRefresh)
    print('Encoding loop starting with parameters:')
    
    # set up handler to look after randomisation of conditions etc
    enc_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(enc_table, selection=enc_selection),
        seed=None, name='enc_trials')
    thisExp.addLoop(enc_trials)  # add the loop to the experiment
    thisEnc_trial = enc_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_trial.rgb)
    if thisEnc_trial != None:
        for paramName in thisEnc_trial:
            exec('{} = thisEnc_trial[paramName]'.format(paramName))
    
    for thisEnc_trial in enc_trials:
        currentLoop = enc_trials
        # abbreviate parameter names if possible (e.g. rgb = thisEnc_trial.rgb)
        if thisEnc_trial != None:
            for paramName in thisEnc_trial:
                exec('{} = thisEnc_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "enc_fx"-------
        continueRoutine = True
        # update component parameters for each repeat
        block_name = ''
        if TrialType=='OBJ':
            block_name='Képválasztás'
        elif TrialType=='LOC':
            block_name='Helyválasztás'
        else:
            block_name='Block Unknown'
        enc_fx_cross.setPos((CurrentX, CurrentY))
        enc_fx_key.keys = []
        enc_fx_key.rt = []
        _enc_fx_key_allKeys = []
        enc_fx_text_block.setText(block_name)
        # keep track of which components have finished
        enc_fxComponents = [enc_fx_interior, enc_fx_cross, enc_fx_key, enc_fx_text_block, enc_fx_instructions_text]
        for thisComponent in enc_fxComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        enc_fxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "enc_fx"-------
        while continueRoutine:
            # get current time
            t = enc_fxClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=enc_fxClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *enc_fx_interior* updates
            if enc_fx_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_interior.frameNStart = frameN  # exact frame index
                enc_fx_interior.tStart = t  # local t and not account for scr refresh
                enc_fx_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_interior, 'tStartRefresh')  # time at next scr refresh
                enc_fx_interior.setAutoDraw(True)
            if enc_fx_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_interior.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_interior.tStop = t  # not accounting for scr refresh
                    enc_fx_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_interior, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_interior.setAutoDraw(False)
            
            # *enc_fx_cross* updates
            if enc_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_cross.frameNStart = frameN  # exact frame index
                enc_fx_cross.tStart = t  # local t and not account for scr refresh
                enc_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_cross, 'tStartRefresh')  # time at next scr refresh
                enc_fx_cross.setAutoDraw(True)
            if enc_fx_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_cross.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_cross.tStop = t  # not accounting for scr refresh
                    enc_fx_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_cross, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_cross.setAutoDraw(False)
            
            # *enc_fx_key* updates
            waitOnFlip = False
            if enc_fx_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_key.frameNStart = frameN  # exact frame index
                enc_fx_key.tStart = t  # local t and not account for scr refresh
                enc_fx_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_key, 'tStartRefresh')  # time at next scr refresh
                enc_fx_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(enc_fx_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(enc_fx_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if enc_fx_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_key.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_key.tStop = t  # not accounting for scr refresh
                    enc_fx_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_key, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_key.status = FINISHED
            if enc_fx_key.status == STARTED and not waitOnFlip:
                theseKeys = enc_fx_key.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
                _enc_fx_key_allKeys.extend(theseKeys)
                if len(_enc_fx_key_allKeys):
                    enc_fx_key.keys = _enc_fx_key_allKeys[-1].name  # just the last key pressed
                    enc_fx_key.rt = _enc_fx_key_allKeys[-1].rt
            
            # *enc_fx_text_block* updates
            if enc_fx_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_text_block.frameNStart = frameN  # exact frame index
                enc_fx_text_block.tStart = t  # local t and not account for scr refresh
                enc_fx_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_text_block, 'tStartRefresh')  # time at next scr refresh
                enc_fx_text_block.setAutoDraw(True)
            if enc_fx_text_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_text_block.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_text_block.tStop = t  # not accounting for scr refresh
                    enc_fx_text_block.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_text_block, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_text_block.setAutoDraw(False)
            
            # *enc_fx_instructions_text* updates
            if enc_fx_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_instructions_text.frameNStart = frameN  # exact frame index
                enc_fx_instructions_text.tStart = t  # local t and not account for scr refresh
                enc_fx_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_instructions_text, 'tStartRefresh')  # time at next scr refresh
                enc_fx_instructions_text.setAutoDraw(True)
            if enc_fx_instructions_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_instructions_text.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_instructions_text.tStop = t  # not accounting for scr refresh
                    enc_fx_instructions_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_instructions_text, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_instructions_text.setAutoDraw(False)
            if enc_trials.thisN == 0 and frameN == 0: # start of the loop
                loop_start_time = globalClock.getTime() - trigger_time
                thisExp.addData('enc_loop_start_time', loop_start_time)
            elif frameN == 1: # the zeroth frame has just been drawn
                fx_start_time = globalClock.getTime() - trigger_time
                # store the data:
                thisExp.addData('enc_fx_start_time', fx_start_time)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in enc_fxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "enc_fx"-------
        for thisComponent in enc_fxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        enc_trials.addData('enc_fx_interior.started', enc_fx_interior.tStartRefresh)
        enc_trials.addData('enc_fx_interior.stopped', enc_fx_interior.tStopRefresh)
        enc_trials.addData('enc_fx_cross.started', enc_fx_cross.tStartRefresh)
        enc_trials.addData('enc_fx_cross.stopped', enc_fx_cross.tStopRefresh)
        # check responses
        if enc_fx_key.keys in ['', [], None]:  # No response was made
            enc_fx_key.keys = None
        enc_trials.addData('enc_fx_key.keys',enc_fx_key.keys)
        if enc_fx_key.keys != None:  # we had a response
            enc_trials.addData('enc_fx_key.rt', enc_fx_key.rt)
        enc_trials.addData('enc_fx_key.started', enc_fx_key.tStartRefresh)
        enc_trials.addData('enc_fx_key.stopped', enc_fx_key.tStopRefresh)
        enc_trials.addData('enc_fx_text_block.started', enc_fx_text_block.tStartRefresh)
        enc_trials.addData('enc_fx_text_block.stopped', enc_fx_text_block.tStopRefresh)
        enc_trials.addData('enc_fx_instructions_text.started', enc_fx_instructions_text.tStartRefresh)
        enc_trials.addData('enc_fx_instructions_text.stopped', enc_fx_instructions_text.tStopRefresh)
        # the Routine "enc_fx" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "enc_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        enc_trial_main_image.setPos((CurrentX, CurrentY))
        enc_trial_main_image.setSize((0.3125, 0.3125*scr_resolution))
        enc_trial_main_image.setImage(CurrentImage)
        enc_trial_key.keys = []
        enc_trial_key.rt = []
        _enc_trial_key_allKeys = []
        enc_trial_text_block.setText(block_name)
        # keep track of which components have finished
        enc_trialComponents = [enc_trial_interior, enc_trial_main_image, enc_trial_key, enc_trial_text_block, enc_trial_instructions_text]
        for thisComponent in enc_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        enc_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "enc_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = enc_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=enc_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *enc_trial_interior* updates
            if enc_trial_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_interior.frameNStart = frameN  # exact frame index
                enc_trial_interior.tStart = t  # local t and not account for scr refresh
                enc_trial_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_interior, 'tStartRefresh')  # time at next scr refresh
                enc_trial_interior.setAutoDraw(True)
            if enc_trial_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_interior.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_interior.tStop = t  # not accounting for scr refresh
                    enc_trial_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_interior, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_interior.setAutoDraw(False)
            
            # *enc_trial_main_image* updates
            if enc_trial_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_main_image.frameNStart = frameN  # exact frame index
                enc_trial_main_image.tStart = t  # local t and not account for scr refresh
                enc_trial_main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_main_image, 'tStartRefresh')  # time at next scr refresh
                enc_trial_main_image.setAutoDraw(True)
            if enc_trial_main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_main_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_main_image.tStop = t  # not accounting for scr refresh
                    enc_trial_main_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_main_image, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_main_image.setAutoDraw(False)
            
            # *enc_trial_key* updates
            waitOnFlip = False
            if enc_trial_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_key.frameNStart = frameN  # exact frame index
                enc_trial_key.tStart = t  # local t and not account for scr refresh
                enc_trial_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_key, 'tStartRefresh')  # time at next scr refresh
                enc_trial_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(enc_trial_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(enc_trial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if enc_trial_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_key.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_key.tStop = t  # not accounting for scr refresh
                    enc_trial_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_key, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_key.status = FINISHED
            if enc_trial_key.status == STARTED and not waitOnFlip:
                theseKeys = enc_trial_key.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
                _enc_trial_key_allKeys.extend(theseKeys)
                if len(_enc_trial_key_allKeys):
                    enc_trial_key.keys = _enc_trial_key_allKeys[-1].name  # just the last key pressed
                    enc_trial_key.rt = _enc_trial_key_allKeys[-1].rt
            
            # *enc_trial_text_block* updates
            if enc_trial_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_text_block.frameNStart = frameN  # exact frame index
                enc_trial_text_block.tStart = t  # local t and not account for scr refresh
                enc_trial_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_text_block, 'tStartRefresh')  # time at next scr refresh
                enc_trial_text_block.setAutoDraw(True)
            if enc_trial_text_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_text_block.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_text_block.tStop = t  # not accounting for scr refresh
                    enc_trial_text_block.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_text_block, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_text_block.setAutoDraw(False)
            
            # *enc_trial_instructions_text* updates
            if enc_trial_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_instructions_text.frameNStart = frameN  # exact frame index
                enc_trial_instructions_text.tStart = t  # local t and not account for scr refresh
                enc_trial_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_instructions_text, 'tStartRefresh')  # time at next scr refresh
                enc_trial_instructions_text.setAutoDraw(True)
            if enc_trial_instructions_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_instructions_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_instructions_text.tStop = t  # not accounting for scr refresh
                    enc_trial_instructions_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_instructions_text, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_instructions_text.setAutoDraw(False)
            if frameN == 0: # start of the trial
                trial_start_time = globalClock.getTime() - trigger_time
                thisExp.addData('enc_trial_start_time', trial_start_time)
            elif frameN == 1: # the zeroth frame has just been drawn
                stimulus_start_time = globalClock.getTime() - trigger_time
                # store the data:
                thisExp.addData('enc_stimulus_start_time', stimulus_start_time)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in enc_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "enc_trial"-------
        for thisComponent in enc_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        enc_trials.addData('enc_trial_interior.started', enc_trial_interior.tStartRefresh)
        enc_trials.addData('enc_trial_interior.stopped', enc_trial_interior.tStopRefresh)
        enc_trials.addData('enc_trial_main_image.started', enc_trial_main_image.tStartRefresh)
        enc_trials.addData('enc_trial_main_image.stopped', enc_trial_main_image.tStopRefresh)
        # check responses
        if enc_trial_key.keys in ['', [], None]:  # No response was made
            enc_trial_key.keys = None
        enc_trials.addData('enc_trial_key.keys',enc_trial_key.keys)
        if enc_trial_key.keys != None:  # we had a response
            enc_trials.addData('enc_trial_key.rt', enc_trial_key.rt)
        enc_trials.addData('enc_trial_key.started', enc_trial_key.tStartRefresh)
        enc_trials.addData('enc_trial_key.stopped', enc_trial_key.tStopRefresh)
        enc_trials.addData('enc_trial_text_block.started', enc_trial_text_block.tStartRefresh)
        enc_trials.addData('enc_trial_text_block.stopped', enc_trial_text_block.tStopRefresh)
        enc_trials.addData('enc_trial_instructions_text.started', enc_trial_instructions_text.tStartRefresh)
        enc_trials.addData('enc_trial_instructions_text.stopped', enc_trial_instructions_text.tStopRefresh)
        response=enc_trial_key.keys
        if response == 'b':
            info_text = '\'Nem marad.\''
        elif response == 'c':
            info_text = '\'Marad.\''
        elif response=='a' or response=='d':
            info_text = 'Invalid!'
        else:
            response='-'
            info_text = '\'Nem adott választ.\''
            enc_missing = enc_missing + 1
        
        print('Button pressed: {}. Response: {}'.format(response, info_text))
        thisExp.nextEntry()
        
    # completed 1 repeats of 'enc_trials'
    
    
    # ------Prepare to start Routine "encoding_baseline_end"-------
    continueRoutine = True
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    encoding_baseline_text_block_2.setText(block_name)
    baseline_end_cross.setPos((CurrentX, CurrentY))
    cprint('# missed: {}'.format(enc_missing), 'yellow')
    miss = (enc_missing/76)*100
    cprint('% missed: {}'.format(miss), 'yellow')
    cprint('On Screen: Encoding Baseline - End', 'blue', 'on_white')
    # keep track of which components have finished
    encoding_baseline_endComponents = [encoding_baseline_interior_2, encoding_baseline_text_block_2, encoding_baseline_instructions_text_2, baseline_end_cross]
    for thisComponent in encoding_baseline_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encoding_baseline_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "encoding_baseline_end"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = encoding_baseline_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encoding_baseline_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encoding_baseline_interior_2* updates
        if encoding_baseline_interior_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_baseline_interior_2.frameNStart = frameN  # exact frame index
            encoding_baseline_interior_2.tStart = t  # local t and not account for scr refresh
            encoding_baseline_interior_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_baseline_interior_2, 'tStartRefresh')  # time at next scr refresh
            encoding_baseline_interior_2.setAutoDraw(True)
        if encoding_baseline_interior_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_baseline_interior_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                encoding_baseline_interior_2.tStop = t  # not accounting for scr refresh
                encoding_baseline_interior_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_baseline_interior_2, 'tStopRefresh')  # time at next scr refresh
                encoding_baseline_interior_2.setAutoDraw(False)
        
        # *encoding_baseline_text_block_2* updates
        if encoding_baseline_text_block_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_baseline_text_block_2.frameNStart = frameN  # exact frame index
            encoding_baseline_text_block_2.tStart = t  # local t and not account for scr refresh
            encoding_baseline_text_block_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_baseline_text_block_2, 'tStartRefresh')  # time at next scr refresh
            encoding_baseline_text_block_2.setAutoDraw(True)
        if encoding_baseline_text_block_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_baseline_text_block_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                encoding_baseline_text_block_2.tStop = t  # not accounting for scr refresh
                encoding_baseline_text_block_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_baseline_text_block_2, 'tStopRefresh')  # time at next scr refresh
                encoding_baseline_text_block_2.setAutoDraw(False)
        
        # *encoding_baseline_instructions_text_2* updates
        if encoding_baseline_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_baseline_instructions_text_2.frameNStart = frameN  # exact frame index
            encoding_baseline_instructions_text_2.tStart = t  # local t and not account for scr refresh
            encoding_baseline_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_baseline_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
            encoding_baseline_instructions_text_2.setAutoDraw(True)
        if encoding_baseline_instructions_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_baseline_instructions_text_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                encoding_baseline_instructions_text_2.tStop = t  # not accounting for scr refresh
                encoding_baseline_instructions_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_baseline_instructions_text_2, 'tStopRefresh')  # time at next scr refresh
                encoding_baseline_instructions_text_2.setAutoDraw(False)
        
        # *baseline_end_cross* updates
        if baseline_end_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_end_cross.frameNStart = frameN  # exact frame index
            baseline_end_cross.tStart = t  # local t and not account for scr refresh
            baseline_end_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_end_cross, 'tStartRefresh')  # time at next scr refresh
            baseline_end_cross.setAutoDraw(True)
        if baseline_end_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_end_cross.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                baseline_end_cross.tStop = t  # not accounting for scr refresh
                baseline_end_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baseline_end_cross, 'tStopRefresh')  # time at next scr refresh
                baseline_end_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encoding_baseline_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "encoding_baseline_end"-------
    for thisComponent in encoding_baseline_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('encoding_baseline_interior_2.started', encoding_baseline_interior_2.tStartRefresh)
    run.addData('encoding_baseline_interior_2.stopped', encoding_baseline_interior_2.tStopRefresh)
    run.addData('encoding_baseline_text_block_2.started', encoding_baseline_text_block_2.tStartRefresh)
    run.addData('encoding_baseline_text_block_2.stopped', encoding_baseline_text_block_2.tStopRefresh)
    run.addData('encoding_baseline_instructions_text_2.started', encoding_baseline_instructions_text_2.tStartRefresh)
    run.addData('encoding_baseline_instructions_text_2.stopped', encoding_baseline_instructions_text_2.tStopRefresh)
    run.addData('baseline_end_cross.started', baseline_end_cross.tStartRefresh)
    run.addData('baseline_end_cross.stopped', baseline_end_cross.tStopRefresh)
    
    # ------Prepare to start Routine "filler_task"-------
    continueRoutine = True
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    cprint('on Screen: Math Exercise', 'blue')
    if session=='OBJ':
        i = run_counter - 1
    elif session=='LOC':
        i = run_counter + 2
    problem = math_problems[i]
    solution = math_solutions[i]
    correct = math_correct[i]
    
    math_problem.setText(problem)
    math_solution.setText(solution)
    filler_task_resp.keys = []
    filler_task_resp.rt = []
    _filler_task_resp_allKeys = []
    # keep track of which components have finished
    filler_taskComponents = [math_problem, math_solution, filler_task_resp]
    for thisComponent in filler_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    filler_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "filler_task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = filler_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=filler_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *math_problem* updates
        if math_problem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_problem.frameNStart = frameN  # exact frame index
            math_problem.tStart = t  # local t and not account for scr refresh
            math_problem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_problem, 'tStartRefresh')  # time at next scr refresh
            math_problem.setAutoDraw(True)
        if math_problem.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_problem.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                math_problem.tStop = t  # not accounting for scr refresh
                math_problem.frameNStop = frameN  # exact frame index
                win.timeOnFlip(math_problem, 'tStopRefresh')  # time at next scr refresh
                math_problem.setAutoDraw(False)
        
        # *math_solution* updates
        if math_solution.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            math_solution.frameNStart = frameN  # exact frame index
            math_solution.tStart = t  # local t and not account for scr refresh
            math_solution.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(math_solution, 'tStartRefresh')  # time at next scr refresh
            math_solution.setAutoDraw(True)
        if math_solution.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > math_solution.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                math_solution.tStop = t  # not accounting for scr refresh
                math_solution.frameNStop = frameN  # exact frame index
                win.timeOnFlip(math_solution, 'tStopRefresh')  # time at next scr refresh
                math_solution.setAutoDraw(False)
        
        # *filler_task_resp* updates
        waitOnFlip = False
        if filler_task_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            filler_task_resp.frameNStart = frameN  # exact frame index
            filler_task_resp.tStart = t  # local t and not account for scr refresh
            filler_task_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filler_task_resp, 'tStartRefresh')  # time at next scr refresh
            filler_task_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(filler_task_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(filler_task_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if filler_task_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > filler_task_resp.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                filler_task_resp.tStop = t  # not accounting for scr refresh
                filler_task_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(filler_task_resp, 'tStopRefresh')  # time at next scr refresh
                filler_task_resp.status = FINISHED
        if filler_task_resp.status == STARTED and not waitOnFlip:
            theseKeys = filler_task_resp.getKeys(keyList=['b', 'c'], waitRelease=False)
            _filler_task_resp_allKeys.extend(theseKeys)
            if len(_filler_task_resp_allKeys):
                filler_task_resp.keys = _filler_task_resp_allKeys[-1].name  # just the last key pressed
                filler_task_resp.rt = _filler_task_resp_allKeys[-1].rt
                # was this correct?
                if (filler_task_resp.keys == str(correct)) or (filler_task_resp.keys == correct):
                    filler_task_resp.corr = 1
                else:
                    filler_task_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in filler_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "filler_task"-------
    for thisComponent in filler_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if filler_task_resp.keys==correct:
        cprint('Correct response', 'green')
    else:
        print('Incorrect response')
    run.addData('math_problem.started', math_problem.tStartRefresh)
    run.addData('math_problem.stopped', math_problem.tStopRefresh)
    run.addData('math_solution.started', math_solution.tStartRefresh)
    run.addData('math_solution.stopped', math_solution.tStopRefresh)
    # check responses
    if filler_task_resp.keys in ['', [], None]:  # No response was made
        filler_task_resp.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           filler_task_resp.corr = 1;  # correct non-response
        else:
           filler_task_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for run (TrialHandler)
    run.addData('filler_task_resp.keys',filler_task_resp.keys)
    run.addData('filler_task_resp.corr', filler_task_resp.corr)
    if filler_task_resp.keys != None:  # we had a response
        run.addData('filler_task_resp.rt', filler_task_resp.rt)
    run.addData('filler_task_resp.started', filler_task_resp.tStartRefresh)
    run.addData('filler_task_resp.stopped', filler_task_resp.tStopRefresh)
    
    # ------Prepare to start Routine "wait_for_last_scan_rec"-------
    continueRoutine = True
    routineTimer.add(600.000000)
    # update component parameters for each repeat
    wait_for_last_scan_continue_2.keys = []
    wait_for_last_scan_continue_2.rt = []
    _wait_for_last_scan_continue_2_allKeys = []
    cprint('On Screen: A vizsgálatvezető előkészíti a scannert', 'blue')
    cprint('Experimenter: Ready for scanning? Hit SPACE or -> to continue.', 'red')
    # keep track of which components have finished
    wait_for_last_scan_recComponents = [wait_for_last_scan_text_2, wait_for_last_scan_continue_2]
    for thisComponent in wait_for_last_scan_recComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wait_for_last_scan_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wait_for_last_scan_rec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wait_for_last_scan_recClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wait_for_last_scan_recClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_for_last_scan_text_2* updates
        if wait_for_last_scan_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_for_last_scan_text_2.frameNStart = frameN  # exact frame index
            wait_for_last_scan_text_2.tStart = t  # local t and not account for scr refresh
            wait_for_last_scan_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_for_last_scan_text_2, 'tStartRefresh')  # time at next scr refresh
            wait_for_last_scan_text_2.setAutoDraw(True)
        if wait_for_last_scan_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_for_last_scan_text_2.tStartRefresh + 600.0-frameTolerance:
                # keep track of stop time/frame for later
                wait_for_last_scan_text_2.tStop = t  # not accounting for scr refresh
                wait_for_last_scan_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait_for_last_scan_text_2, 'tStopRefresh')  # time at next scr refresh
                wait_for_last_scan_text_2.setAutoDraw(False)
        
        # *wait_for_last_scan_continue_2* updates
        waitOnFlip = False
        if wait_for_last_scan_continue_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            wait_for_last_scan_continue_2.frameNStart = frameN  # exact frame index
            wait_for_last_scan_continue_2.tStart = t  # local t and not account for scr refresh
            wait_for_last_scan_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_for_last_scan_continue_2, 'tStartRefresh')  # time at next scr refresh
            wait_for_last_scan_continue_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wait_for_last_scan_continue_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wait_for_last_scan_continue_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wait_for_last_scan_continue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_for_last_scan_continue_2.tStartRefresh + 599-frameTolerance:
                # keep track of stop time/frame for later
                wait_for_last_scan_continue_2.tStop = t  # not accounting for scr refresh
                wait_for_last_scan_continue_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait_for_last_scan_continue_2, 'tStopRefresh')  # time at next scr refresh
                wait_for_last_scan_continue_2.status = FINISHED
        if wait_for_last_scan_continue_2.status == STARTED and not waitOnFlip:
            theseKeys = wait_for_last_scan_continue_2.getKeys(keyList=['right', 'space'], waitRelease=False)
            _wait_for_last_scan_continue_2_allKeys.extend(theseKeys)
            if len(_wait_for_last_scan_continue_2_allKeys):
                wait_for_last_scan_continue_2.keys = _wait_for_last_scan_continue_2_allKeys[-1].name  # just the last key pressed
                wait_for_last_scan_continue_2.rt = _wait_for_last_scan_continue_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait_for_last_scan_recComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wait_for_last_scan_rec"-------
    for thisComponent in wait_for_last_scan_recComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('wait_for_last_scan_text_2.started', wait_for_last_scan_text_2.tStartRefresh)
    run.addData('wait_for_last_scan_text_2.stopped', wait_for_last_scan_text_2.tStopRefresh)
    # check responses
    if wait_for_last_scan_continue_2.keys in ['', [], None]:  # No response was made
        wait_for_last_scan_continue_2.keys = None
    run.addData('wait_for_last_scan_continue_2.keys',wait_for_last_scan_continue_2.keys)
    if wait_for_last_scan_continue_2.keys != None:  # we had a response
        run.addData('wait_for_last_scan_continue_2.rt', wait_for_last_scan_continue_2.rt)
    run.addData('wait_for_last_scan_continue_2.started', wait_for_last_scan_continue_2.tStartRefresh)
    run.addData('wait_for_last_scan_continue_2.stopped', wait_for_last_scan_continue_2.tStopRefresh)
    
    # ------Prepare to start Routine "start_MR_rec"-------
    continueRoutine = True
    routineTimer.add(1200.000000)
    # update component parameters for each repeat
    cprint('Experimenter: Waiting for trigger. Start scanning...', 'yellow')
    MR_trigger_2.keys = []
    MR_trigger_2.rt = []
    _MR_trigger_2_allKeys = []
    # keep track of which components have finished
    start_MR_recComponents = [start_MR_text_2, MR_trigger_2]
    for thisComponent in start_MR_recComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_MR_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_MR_rec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_MR_recClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_MR_recClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_MR_text_2* updates
        if start_MR_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_MR_text_2.frameNStart = frameN  # exact frame index
            start_MR_text_2.tStart = t  # local t and not account for scr refresh
            start_MR_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_MR_text_2, 'tStartRefresh')  # time at next scr refresh
            start_MR_text_2.setAutoDraw(True)
        if start_MR_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_MR_text_2.tStartRefresh + 1200.0-frameTolerance:
                # keep track of stop time/frame for later
                start_MR_text_2.tStop = t  # not accounting for scr refresh
                start_MR_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_MR_text_2, 'tStopRefresh')  # time at next scr refresh
                start_MR_text_2.setAutoDraw(False)
        
        # *MR_trigger_2* updates
        waitOnFlip = False
        if MR_trigger_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MR_trigger_2.frameNStart = frameN  # exact frame index
            MR_trigger_2.tStart = t  # local t and not account for scr refresh
            MR_trigger_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MR_trigger_2, 'tStartRefresh')  # time at next scr refresh
            MR_trigger_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MR_trigger_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MR_trigger_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MR_trigger_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MR_trigger_2.tStartRefresh + 1200.0-frameTolerance:
                # keep track of stop time/frame for later
                MR_trigger_2.tStop = t  # not accounting for scr refresh
                MR_trigger_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(MR_trigger_2, 'tStopRefresh')  # time at next scr refresh
                MR_trigger_2.status = FINISHED
        if MR_trigger_2.status == STARTED and not waitOnFlip:
            theseKeys = MR_trigger_2.getKeys(keyList=['s'], waitRelease=False)
            _MR_trigger_2_allKeys.extend(theseKeys)
            if len(_MR_trigger_2_allKeys):
                MR_trigger_2.keys = _MR_trigger_2_allKeys[0].name  # just the first key pressed
                MR_trigger_2.rt = _MR_trigger_2_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_MR_recComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_MR_rec"-------
    for thisComponent in start_MR_recComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trigger_time = globalClock.getTime()
    thisExp.addData('trigger_time', trigger_time)
    cprint('Trigger recieved.', 'green')
    run.addData('start_MR_text_2.started', start_MR_text_2.tStartRefresh)
    run.addData('start_MR_text_2.stopped', start_MR_text_2.tStopRefresh)
    # check responses
    if MR_trigger_2.keys in ['', [], None]:  # No response was made
        MR_trigger_2.keys = None
    run.addData('MR_trigger_2.keys',MR_trigger_2.keys)
    if MR_trigger_2.keys != None:  # we had a response
        run.addData('MR_trigger_2.rt', MR_trigger_2.rt)
    run.addData('MR_trigger_2.started', MR_trigger_2.tStartRefresh)
    run.addData('MR_trigger_2.stopped', MR_trigger_2.tStopRefresh)
    
    # ------Prepare to start Routine "start_rec_run"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    run_counter = run_counter + 1
    end_run_text = 'Rövid szünet.\n\nA feladat folytatáshoz nyomja le a gombot a jobb hüvelykujjával.'
    
    if run_counter == 4:
        end_run_text = 'Vége a feladatnak. A folytatáshoz nyomja le a gombot a jobb hüvelykujjával.'
     
    # keep track of which components have finished
    start_rec_runComponents = [start_rec_run_text]
    for thisComponent in start_rec_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_rec_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_rec_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_rec_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_rec_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_rec_run_text* updates
        if start_rec_run_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_rec_run_text.frameNStart = frameN  # exact frame index
            start_rec_run_text.tStart = t  # local t and not account for scr refresh
            start_rec_run_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_rec_run_text, 'tStartRefresh')  # time at next scr refresh
            start_rec_run_text.setAutoDraw(True)
        if start_rec_run_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_rec_run_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                start_rec_run_text.tStop = t  # not accounting for scr refresh
                start_rec_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_rec_run_text, 'tStopRefresh')  # time at next scr refresh
                start_rec_run_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_rec_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_rec_run"-------
    for thisComponent in start_rec_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('start_rec_run_text.started', start_rec_run_text.tStartRefresh)
    run.addData('start_rec_run_text.stopped', start_rec_run_text.tStopRefresh)
    
    # ------Prepare to start Routine "recognition_title"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képfelismerés'
    elif TrialType=='LOC':
        block_name='Helyfelismerés'
    else:
        block_name='Block Unknown'
    start_recognition_text.setText(block_name)
    # keep track of which components have finished
    recognition_titleComponents = [start_recognition_text]
    for thisComponent in recognition_titleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recognition_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "recognition_title"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recognition_titleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recognition_titleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_recognition_text* updates
        if start_recognition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_recognition_text.frameNStart = frameN  # exact frame index
            start_recognition_text.tStart = t  # local t and not account for scr refresh
            start_recognition_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_recognition_text, 'tStartRefresh')  # time at next scr refresh
            start_recognition_text.setAutoDraw(True)
        if start_recognition_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_recognition_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                start_recognition_text.tStop = t  # not accounting for scr refresh
                start_recognition_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_recognition_text, 'tStopRefresh')  # time at next scr refresh
                start_recognition_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recognition_titleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recognition_title"-------
    for thisComponent in recognition_titleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('start_recognition_text.started', start_recognition_text.tStartRefresh)
    run.addData('start_recognition_text.stopped', start_recognition_text.tStopRefresh)
    print('Recognition practice loop starting with following parameters:')
    
    # ------Prepare to start Routine "recognition_baseline"-------
    continueRoutine = True
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képfelismerés'
    elif TrialType=='LOC':
        block_name='Helyfelismerés'
    else:
        block_name='Block Unknown'
    recognition_baseline_text_block.setText(block_name
)
    baseline_rec_fx_cross.setPos((CurrentX, CurrentY))
    cprint('On Screen: Recognition baseline - Start', 'blue', 'on_white')
    rec_missing = 0
    hits = 0
    # keep track of which components have finished
    recognition_baselineComponents = [recognition_baseline_interior, recognition_baseline_text_block, recognition_baseline_instructions_text, baseline_rec_fx_cross]
    for thisComponent in recognition_baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recognition_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "recognition_baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recognition_baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recognition_baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recognition_baseline_interior* updates
        if recognition_baseline_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_baseline_interior.frameNStart = frameN  # exact frame index
            recognition_baseline_interior.tStart = t  # local t and not account for scr refresh
            recognition_baseline_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_baseline_interior, 'tStartRefresh')  # time at next scr refresh
            recognition_baseline_interior.setAutoDraw(True)
        if recognition_baseline_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recognition_baseline_interior.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                recognition_baseline_interior.tStop = t  # not accounting for scr refresh
                recognition_baseline_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(recognition_baseline_interior, 'tStopRefresh')  # time at next scr refresh
                recognition_baseline_interior.setAutoDraw(False)
        
        # *recognition_baseline_text_block* updates
        if recognition_baseline_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_baseline_text_block.frameNStart = frameN  # exact frame index
            recognition_baseline_text_block.tStart = t  # local t and not account for scr refresh
            recognition_baseline_text_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_baseline_text_block, 'tStartRefresh')  # time at next scr refresh
            recognition_baseline_text_block.setAutoDraw(True)
        if recognition_baseline_text_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recognition_baseline_text_block.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                recognition_baseline_text_block.tStop = t  # not accounting for scr refresh
                recognition_baseline_text_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(recognition_baseline_text_block, 'tStopRefresh')  # time at next scr refresh
                recognition_baseline_text_block.setAutoDraw(False)
        
        # *recognition_baseline_instructions_text* updates
        if recognition_baseline_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_baseline_instructions_text.frameNStart = frameN  # exact frame index
            recognition_baseline_instructions_text.tStart = t  # local t and not account for scr refresh
            recognition_baseline_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_baseline_instructions_text, 'tStartRefresh')  # time at next scr refresh
            recognition_baseline_instructions_text.setAutoDraw(True)
        if recognition_baseline_instructions_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recognition_baseline_instructions_text.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                recognition_baseline_instructions_text.tStop = t  # not accounting for scr refresh
                recognition_baseline_instructions_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(recognition_baseline_instructions_text, 'tStopRefresh')  # time at next scr refresh
                recognition_baseline_instructions_text.setAutoDraw(False)
        
        # *baseline_rec_fx_cross* updates
        if baseline_rec_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_rec_fx_cross.frameNStart = frameN  # exact frame index
            baseline_rec_fx_cross.tStart = t  # local t and not account for scr refresh
            baseline_rec_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_rec_fx_cross, 'tStartRefresh')  # time at next scr refresh
            baseline_rec_fx_cross.setAutoDraw(True)
        if baseline_rec_fx_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_rec_fx_cross.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                baseline_rec_fx_cross.tStop = t  # not accounting for scr refresh
                baseline_rec_fx_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baseline_rec_fx_cross, 'tStopRefresh')  # time at next scr refresh
                baseline_rec_fx_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recognition_baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recognition_baseline"-------
    for thisComponent in recognition_baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('recognition_baseline_interior.started', recognition_baseline_interior.tStartRefresh)
    run.addData('recognition_baseline_interior.stopped', recognition_baseline_interior.tStopRefresh)
    run.addData('recognition_baseline_text_block.started', recognition_baseline_text_block.tStartRefresh)
    run.addData('recognition_baseline_text_block.stopped', recognition_baseline_text_block.tStopRefresh)
    run.addData('recognition_baseline_instructions_text.started', recognition_baseline_instructions_text.tStartRefresh)
    run.addData('recognition_baseline_instructions_text.stopped', recognition_baseline_instructions_text.tStopRefresh)
    run.addData('baseline_rec_fx_cross.started', baseline_rec_fx_cross.tStartRefresh)
    run.addData('baseline_rec_fx_cross.stopped', baseline_rec_fx_cross.tStopRefresh)
    print('Recognition loop starting with parameters:')
    
    # set up handler to look after randomisation of conditions etc
    rec_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(rec_table, selection=rec_selection),
        seed=None, name='rec_trials')
    thisExp.addLoop(rec_trials)  # add the loop to the experiment
    thisRec_trial = rec_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRec_trial.rgb)
    if thisRec_trial != None:
        for paramName in thisRec_trial:
            exec('{} = thisRec_trial[paramName]'.format(paramName))
    
    for thisRec_trial in rec_trials:
        currentLoop = rec_trials
        # abbreviate parameter names if possible (e.g. rgb = thisRec_trial.rgb)
        if thisRec_trial != None:
            for paramName in thisRec_trial:
                exec('{} = thisRec_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rec_fx"-------
        continueRoutine = True
        # update component parameters for each repeat
        block_name = ''
        if TrialType=='OBJ':
            block_name='Képfelismerés'
        elif TrialType=='LOC':
            block_name='Helyfelismerés'
        else:
            block_name='Block Unknown'
        rec_fx_cross.setPos((CurrentX, CurrentY))
        rec_fx_key.keys = []
        rec_fx_key.rt = []
        _rec_fx_key_allKeys = []
        rec_fx_text_block.setText(block_name
)
        # keep track of which components have finished
        rec_fxComponents = [rec_fx_interior, rec_fx_cross, rec_fx_key, rec_fx_text_block, rec_fx_instructions_text]
        for thisComponent in rec_fxComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rec_fxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rec_fx"-------
        while continueRoutine:
            # get current time
            t = rec_fxClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rec_fxClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rec_fx_interior* updates
            if rec_fx_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_interior.frameNStart = frameN  # exact frame index
                rec_fx_interior.tStart = t  # local t and not account for scr refresh
                rec_fx_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_interior, 'tStartRefresh')  # time at next scr refresh
                rec_fx_interior.setAutoDraw(True)
            if rec_fx_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_interior.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_interior.tStop = t  # not accounting for scr refresh
                    rec_fx_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_interior, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_interior.setAutoDraw(False)
            
            # *rec_fx_cross* updates
            if rec_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_cross.frameNStart = frameN  # exact frame index
                rec_fx_cross.tStart = t  # local t and not account for scr refresh
                rec_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_cross, 'tStartRefresh')  # time at next scr refresh
                rec_fx_cross.setAutoDraw(True)
            if rec_fx_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_cross.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_cross.tStop = t  # not accounting for scr refresh
                    rec_fx_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_cross, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_cross.setAutoDraw(False)
            
            # *rec_fx_key* updates
            waitOnFlip = False
            if rec_fx_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_key.frameNStart = frameN  # exact frame index
                rec_fx_key.tStart = t  # local t and not account for scr refresh
                rec_fx_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_key, 'tStartRefresh')  # time at next scr refresh
                rec_fx_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rec_fx_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rec_fx_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rec_fx_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_key.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_key.tStop = t  # not accounting for scr refresh
                    rec_fx_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_key, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_key.status = FINISHED
            if rec_fx_key.status == STARTED and not waitOnFlip:
                theseKeys = rec_fx_key.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
                _rec_fx_key_allKeys.extend(theseKeys)
                if len(_rec_fx_key_allKeys):
                    rec_fx_key.keys = _rec_fx_key_allKeys[-1].name  # just the last key pressed
                    rec_fx_key.rt = _rec_fx_key_allKeys[-1].rt
            
            # *rec_fx_text_block* updates
            if rec_fx_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_text_block.frameNStart = frameN  # exact frame index
                rec_fx_text_block.tStart = t  # local t and not account for scr refresh
                rec_fx_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_text_block, 'tStartRefresh')  # time at next scr refresh
                rec_fx_text_block.setAutoDraw(True)
            if rec_fx_text_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_text_block.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_text_block.tStop = t  # not accounting for scr refresh
                    rec_fx_text_block.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_text_block, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_text_block.setAutoDraw(False)
            
            # *rec_fx_instructions_text* updates
            if rec_fx_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_instructions_text.frameNStart = frameN  # exact frame index
                rec_fx_instructions_text.tStart = t  # local t and not account for scr refresh
                rec_fx_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_instructions_text, 'tStartRefresh')  # time at next scr refresh
                rec_fx_instructions_text.setAutoDraw(True)
            if rec_fx_instructions_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_instructions_text.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_instructions_text.tStop = t  # not accounting for scr refresh
                    rec_fx_instructions_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_instructions_text, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_instructions_text.setAutoDraw(False)
            if rec_trials.thisN == 0 and frameN == 0: # start of the loop
                loop_start_time = globalClock.getTime() - trigger_time
                thisExp.addData('rec_loop_start_time', loop_start_time)
            elif frameN == 1: # the zeroth frame has just been drawn
                fx_start_time = globalClock.getTime() - trigger_time
                # store the data:
                thisExp.addData('rec_fx_start_time', fx_start_time)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_fxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rec_fx"-------
        for thisComponent in rec_fxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rec_trials.addData('rec_fx_interior.started', rec_fx_interior.tStartRefresh)
        rec_trials.addData('rec_fx_interior.stopped', rec_fx_interior.tStopRefresh)
        rec_trials.addData('rec_fx_cross.started', rec_fx_cross.tStartRefresh)
        rec_trials.addData('rec_fx_cross.stopped', rec_fx_cross.tStopRefresh)
        # check responses
        if rec_fx_key.keys in ['', [], None]:  # No response was made
            rec_fx_key.keys = None
        rec_trials.addData('rec_fx_key.keys',rec_fx_key.keys)
        if rec_fx_key.keys != None:  # we had a response
            rec_trials.addData('rec_fx_key.rt', rec_fx_key.rt)
        rec_trials.addData('rec_fx_key.started', rec_fx_key.tStartRefresh)
        rec_trials.addData('rec_fx_key.stopped', rec_fx_key.tStopRefresh)
        rec_trials.addData('rec_fx_text_block.started', rec_fx_text_block.tStartRefresh)
        rec_trials.addData('rec_fx_text_block.stopped', rec_fx_text_block.tStopRefresh)
        rec_trials.addData('rec_fx_instructions_text.started', rec_fx_instructions_text.tStartRefresh)
        rec_trials.addData('rec_fx_instructions_text.stopped', rec_fx_instructions_text.tStopRefresh)
        # the Routine "rec_fx" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rec_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        rec_trial_main_image.setPos((CurrentX, CurrentY))
        rec_trial_main_image.setSize((0.3125, 0.3125*scr_resolution))
        rec_trial_main_image.setImage(CurrentImage)
        rec_trial_key.keys = []
        rec_trial_key.rt = []
        _rec_trial_key_allKeys = []
        rec_trial_text_block.setText(block_name)
        # keep track of which components have finished
        rec_trialComponents = [rec_trial_interior, rec_trial_main_image, rec_trial_key, rec_trial_text_block, rec_trial_instructions_text]
        for thisComponent in rec_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rec_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rec_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rec_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rec_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rec_trial_interior* updates
            if rec_trial_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_interior.frameNStart = frameN  # exact frame index
                rec_trial_interior.tStart = t  # local t and not account for scr refresh
                rec_trial_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_interior, 'tStartRefresh')  # time at next scr refresh
                rec_trial_interior.setAutoDraw(True)
            if rec_trial_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_interior.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_interior.tStop = t  # not accounting for scr refresh
                    rec_trial_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_interior, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_interior.setAutoDraw(False)
            
            # *rec_trial_main_image* updates
            if rec_trial_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_main_image.frameNStart = frameN  # exact frame index
                rec_trial_main_image.tStart = t  # local t and not account for scr refresh
                rec_trial_main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_main_image, 'tStartRefresh')  # time at next scr refresh
                rec_trial_main_image.setAutoDraw(True)
            if rec_trial_main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_main_image.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_main_image.tStop = t  # not accounting for scr refresh
                    rec_trial_main_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_main_image, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_main_image.setAutoDraw(False)
            
            # *rec_trial_key* updates
            waitOnFlip = False
            if rec_trial_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_key.frameNStart = frameN  # exact frame index
                rec_trial_key.tStart = t  # local t and not account for scr refresh
                rec_trial_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_key, 'tStartRefresh')  # time at next scr refresh
                rec_trial_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rec_trial_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rec_trial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rec_trial_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_key.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_key.tStop = t  # not accounting for scr refresh
                    rec_trial_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_key, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_key.status = FINISHED
            if rec_trial_key.status == STARTED and not waitOnFlip:
                theseKeys = rec_trial_key.getKeys(keyList=['b', 'c', 'a', 'd'], waitRelease=False)
                _rec_trial_key_allKeys.extend(theseKeys)
                if len(_rec_trial_key_allKeys):
                    rec_trial_key.keys = _rec_trial_key_allKeys[-1].name  # just the last key pressed
                    rec_trial_key.rt = _rec_trial_key_allKeys[-1].rt
            
            # *rec_trial_text_block* updates
            if rec_trial_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_text_block.frameNStart = frameN  # exact frame index
                rec_trial_text_block.tStart = t  # local t and not account for scr refresh
                rec_trial_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_text_block, 'tStartRefresh')  # time at next scr refresh
                rec_trial_text_block.setAutoDraw(True)
            if rec_trial_text_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_text_block.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_text_block.tStop = t  # not accounting for scr refresh
                    rec_trial_text_block.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_text_block, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_text_block.setAutoDraw(False)
            
            # *rec_trial_instructions_text* updates
            if rec_trial_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_instructions_text.frameNStart = frameN  # exact frame index
                rec_trial_instructions_text.tStart = t  # local t and not account for scr refresh
                rec_trial_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_instructions_text, 'tStartRefresh')  # time at next scr refresh
                rec_trial_instructions_text.setAutoDraw(True)
            if rec_trial_instructions_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_instructions_text.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_instructions_text.tStop = t  # not accounting for scr refresh
                    rec_trial_instructions_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_instructions_text, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_instructions_text.setAutoDraw(False)
            if frameN == 0: # start of the trial
                trial_start_time = globalClock.getTime() - trigger_time
                thisExp.addData('rec_trial_start_time', trial_start_time)
            elif frameN == 1: # the zeroth frame has just been drawn
                stimulus_start_time = globalClock.getTime() - trigger_time
                # store the data:
                thisExp.addData('rec_stimulus_start_time', stimulus_start_time)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rec_trial"-------
        for thisComponent in rec_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rec_trials.addData('rec_trial_interior.started', rec_trial_interior.tStartRefresh)
        rec_trials.addData('rec_trial_interior.stopped', rec_trial_interior.tStopRefresh)
        rec_trials.addData('rec_trial_main_image.started', rec_trial_main_image.tStartRefresh)
        rec_trials.addData('rec_trial_main_image.stopped', rec_trial_main_image.tStopRefresh)
        # check responses
        if rec_trial_key.keys in ['', [], None]:  # No response was made
            rec_trial_key.keys = None
        rec_trials.addData('rec_trial_key.keys',rec_trial_key.keys)
        if rec_trial_key.keys != None:  # we had a response
            rec_trials.addData('rec_trial_key.rt', rec_trial_key.rt)
        rec_trials.addData('rec_trial_key.started', rec_trial_key.tStartRefresh)
        rec_trials.addData('rec_trial_key.stopped', rec_trial_key.tStopRefresh)
        rec_trials.addData('rec_trial_text_block.started', rec_trial_text_block.tStartRefresh)
        rec_trials.addData('rec_trial_text_block.stopped', rec_trial_text_block.tStopRefresh)
        rec_trials.addData('rec_trial_instructions_text.started', rec_trial_instructions_text.tStartRefresh)
        rec_trials.addData('rec_trial_instructions_text.stopped', rec_trial_instructions_text.tStopRefresh)
        response = rec_trial_key.keys
        if response=='b':
            response_text = 'B - OLD'
            if StimType == 'TARGET':
                hits = hits + 1
        elif response=='c':
            response_text = 'C - NEW'
        elif response == 'a' or response=='d':
            response_text = 'INVALID!'
        else:
            response_text = 'Missing'
            rec_missing = rec_missing + 1
            
        info_text = 'Stimulus Type: {}. Response: {}'.format(StimType, response_text)
        print(info_text)
        
        
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'rec_trials'
    
    
    # ------Prepare to start Routine "recognition_baseline_end"-------
    continueRoutine = True
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    recognition_baseline_text_block_2.setText(block_name
)
    baseline_rec_fx_cross_2.setPos((CurrentX, CurrentY))
    cprint('# missed: {}'.format(rec_missing), 'yellow')
    miss = (rec_missing/36)*100
    cprint('% missed: {}'.format(miss), 'yellow')
    cprint('# hits: {}'.format(hits), 'yellow')
    hr = (hits/12)*100
    cprint('hit rate: {}'.format(hr), 'yellow')
    cprint('\n On Screen: Recognition Baseline - End', 'blue', 'on_white')
    # keep track of which components have finished
    recognition_baseline_endComponents = [recognition_baseline_interior_2, recognition_baseline_text_block_2, recognition_baseline_instructions_text_2, baseline_rec_fx_cross_2]
    for thisComponent in recognition_baseline_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    recognition_baseline_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "recognition_baseline_end"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recognition_baseline_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=recognition_baseline_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recognition_baseline_interior_2* updates
        if recognition_baseline_interior_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_baseline_interior_2.frameNStart = frameN  # exact frame index
            recognition_baseline_interior_2.tStart = t  # local t and not account for scr refresh
            recognition_baseline_interior_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_baseline_interior_2, 'tStartRefresh')  # time at next scr refresh
            recognition_baseline_interior_2.setAutoDraw(True)
        if recognition_baseline_interior_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recognition_baseline_interior_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                recognition_baseline_interior_2.tStop = t  # not accounting for scr refresh
                recognition_baseline_interior_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(recognition_baseline_interior_2, 'tStopRefresh')  # time at next scr refresh
                recognition_baseline_interior_2.setAutoDraw(False)
        
        # *recognition_baseline_text_block_2* updates
        if recognition_baseline_text_block_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_baseline_text_block_2.frameNStart = frameN  # exact frame index
            recognition_baseline_text_block_2.tStart = t  # local t and not account for scr refresh
            recognition_baseline_text_block_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_baseline_text_block_2, 'tStartRefresh')  # time at next scr refresh
            recognition_baseline_text_block_2.setAutoDraw(True)
        if recognition_baseline_text_block_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recognition_baseline_text_block_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                recognition_baseline_text_block_2.tStop = t  # not accounting for scr refresh
                recognition_baseline_text_block_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(recognition_baseline_text_block_2, 'tStopRefresh')  # time at next scr refresh
                recognition_baseline_text_block_2.setAutoDraw(False)
        
        # *recognition_baseline_instructions_text_2* updates
        if recognition_baseline_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recognition_baseline_instructions_text_2.frameNStart = frameN  # exact frame index
            recognition_baseline_instructions_text_2.tStart = t  # local t and not account for scr refresh
            recognition_baseline_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recognition_baseline_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
            recognition_baseline_instructions_text_2.setAutoDraw(True)
        if recognition_baseline_instructions_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recognition_baseline_instructions_text_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                recognition_baseline_instructions_text_2.tStop = t  # not accounting for scr refresh
                recognition_baseline_instructions_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(recognition_baseline_instructions_text_2, 'tStopRefresh')  # time at next scr refresh
                recognition_baseline_instructions_text_2.setAutoDraw(False)
        
        # *baseline_rec_fx_cross_2* updates
        if baseline_rec_fx_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_rec_fx_cross_2.frameNStart = frameN  # exact frame index
            baseline_rec_fx_cross_2.tStart = t  # local t and not account for scr refresh
            baseline_rec_fx_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_rec_fx_cross_2, 'tStartRefresh')  # time at next scr refresh
            baseline_rec_fx_cross_2.setAutoDraw(True)
        if baseline_rec_fx_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_rec_fx_cross_2.tStartRefresh + 25-frameTolerance:
                # keep track of stop time/frame for later
                baseline_rec_fx_cross_2.tStop = t  # not accounting for scr refresh
                baseline_rec_fx_cross_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(baseline_rec_fx_cross_2, 'tStopRefresh')  # time at next scr refresh
                baseline_rec_fx_cross_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recognition_baseline_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "recognition_baseline_end"-------
    for thisComponent in recognition_baseline_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('recognition_baseline_interior_2.started', recognition_baseline_interior_2.tStartRefresh)
    run.addData('recognition_baseline_interior_2.stopped', recognition_baseline_interior_2.tStopRefresh)
    run.addData('recognition_baseline_text_block_2.started', recognition_baseline_text_block_2.tStartRefresh)
    run.addData('recognition_baseline_text_block_2.stopped', recognition_baseline_text_block_2.tStopRefresh)
    run.addData('recognition_baseline_instructions_text_2.started', recognition_baseline_instructions_text_2.tStartRefresh)
    run.addData('recognition_baseline_instructions_text_2.stopped', recognition_baseline_instructions_text_2.tStopRefresh)
    run.addData('baseline_rec_fx_cross_2.started', baseline_rec_fx_cross_2.tStartRefresh)
    run.addData('baseline_rec_fx_cross_2.stopped', baseline_rec_fx_cross_2.tStopRefresh)
    
    # ------Prepare to start Routine "end_run"-------
    continueRoutine = True
    routineTimer.add(1201.000000)
    # update component parameters for each repeat
    end_run_text_comp.setText(end_run_text)
    end_run_key.keys = []
    end_run_key.rt = []
    _end_run_key_allKeys = []
    print('\nOn screen: End run. Text:')
    print(end_run_text)
    cprint('Waiting for participant\'s response (d)', 'yellow')
    # keep track of which components have finished
    end_runComponents = [end_run_text_comp, end_run_key]
    for thisComponent in end_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_run_text_comp* updates
        if end_run_text_comp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_run_text_comp.frameNStart = frameN  # exact frame index
            end_run_text_comp.tStart = t  # local t and not account for scr refresh
            end_run_text_comp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_run_text_comp, 'tStartRefresh')  # time at next scr refresh
            end_run_text_comp.setAutoDraw(True)
        if end_run_text_comp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_run_text_comp.tStartRefresh + 1200-frameTolerance:
                # keep track of stop time/frame for later
                end_run_text_comp.tStop = t  # not accounting for scr refresh
                end_run_text_comp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_run_text_comp, 'tStopRefresh')  # time at next scr refresh
                end_run_text_comp.setAutoDraw(False)
        
        # *end_run_key* updates
        waitOnFlip = False
        if end_run_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            end_run_key.frameNStart = frameN  # exact frame index
            end_run_key.tStart = t  # local t and not account for scr refresh
            end_run_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_run_key, 'tStartRefresh')  # time at next scr refresh
            end_run_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_run_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_run_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_run_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_run_key.tStartRefresh + 1200-frameTolerance:
                # keep track of stop time/frame for later
                end_run_key.tStop = t  # not accounting for scr refresh
                end_run_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_run_key, 'tStopRefresh')  # time at next scr refresh
                end_run_key.status = FINISHED
        if end_run_key.status == STARTED and not waitOnFlip:
            theseKeys = end_run_key.getKeys(keyList=['d'], waitRelease=False)
            _end_run_key_allKeys.extend(theseKeys)
            if len(_end_run_key_allKeys):
                end_run_key.keys = _end_run_key_allKeys[-1].name  # just the last key pressed
                end_run_key.rt = _end_run_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_run"-------
    for thisComponent in end_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('end_run_text_comp.started', end_run_text_comp.tStartRefresh)
    run.addData('end_run_text_comp.stopped', end_run_text_comp.tStopRefresh)
    # check responses
    if end_run_key.keys in ['', [], None]:  # No response was made
        end_run_key.keys = None
    run.addData('end_run_key.keys',end_run_key.keys)
    if end_run_key.keys != None:  # we had a response
        run.addData('end_run_key.rt', end_run_key.rt)
    run.addData('end_run_key.started', end_run_key.tStartRefresh)
    run.addData('end_run_key.stopped', end_run_key.tStopRefresh)
    cprint('key pressed: '+ end_run_key.keys, 'green')
# completed 1 repeats of 'run'


# ------Prepare to start Routine "end_session"-------
continueRoutine = True
routineTimer.add(1200.000000)
# update component parameters for each repeat
cprint('\nOn screen: End.', 'blue', 'on_white')
print('Text: Vége a feladatnak.')
cprint('Hit SPACE or -> to exit.', 'red')
inter_task_break_key.keys = []
inter_task_break_key.rt = []
_inter_task_break_key_allKeys = []
# keep track of which components have finished
end_sessionComponents = [inter_task_break_text, inter_task_break_key]
for thisComponent in end_sessionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_sessionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_session"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_sessionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_sessionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inter_task_break_text* updates
    if inter_task_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inter_task_break_text.frameNStart = frameN  # exact frame index
        inter_task_break_text.tStart = t  # local t and not account for scr refresh
        inter_task_break_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inter_task_break_text, 'tStartRefresh')  # time at next scr refresh
        inter_task_break_text.setAutoDraw(True)
    if inter_task_break_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inter_task_break_text.tStartRefresh + 1200.0-frameTolerance:
            # keep track of stop time/frame for later
            inter_task_break_text.tStop = t  # not accounting for scr refresh
            inter_task_break_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inter_task_break_text, 'tStopRefresh')  # time at next scr refresh
            inter_task_break_text.setAutoDraw(False)
    
    # *inter_task_break_key* updates
    waitOnFlip = False
    if inter_task_break_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        inter_task_break_key.frameNStart = frameN  # exact frame index
        inter_task_break_key.tStart = t  # local t and not account for scr refresh
        inter_task_break_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inter_task_break_key, 'tStartRefresh')  # time at next scr refresh
        inter_task_break_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(inter_task_break_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(inter_task_break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if inter_task_break_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inter_task_break_key.tStartRefresh + 1195-frameTolerance:
            # keep track of stop time/frame for later
            inter_task_break_key.tStop = t  # not accounting for scr refresh
            inter_task_break_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inter_task_break_key, 'tStopRefresh')  # time at next scr refresh
            inter_task_break_key.status = FINISHED
    if inter_task_break_key.status == STARTED and not waitOnFlip:
        theseKeys = inter_task_break_key.getKeys(keyList=['space', 'right'], waitRelease=False)
        _inter_task_break_key_allKeys.extend(theseKeys)
        if len(_inter_task_break_key_allKeys):
            inter_task_break_key.keys = _inter_task_break_key_allKeys[-1].name  # just the last key pressed
            inter_task_break_key.rt = _inter_task_break_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_sessionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_session"-------
for thisComponent in end_sessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('inter_task_break_text.started', inter_task_break_text.tStartRefresh)
thisExp.addData('inter_task_break_text.stopped', inter_task_break_text.tStopRefresh)
# check responses
if inter_task_break_key.keys in ['', [], None]:  # No response was made
    inter_task_break_key.keys = None
thisExp.addData('inter_task_break_key.keys',inter_task_break_key.keys)
if inter_task_break_key.keys != None:  # we had a response
    thisExp.addData('inter_task_break_key.rt', inter_task_break_key.rt)
thisExp.addData('inter_task_break_key.started', inter_task_break_key.tStartRefresh)
thisExp.addData('inter_task_break_key.stopped', inter_task_break_key.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
