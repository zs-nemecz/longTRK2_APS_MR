#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on July 19, 2022, at 12:35
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
expInfo = {'online ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['online ID'],'session_1', expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Zsuzsa\\HCCCL\\TerKepEsz_Tasks\\computer_based_tasks\\longTRK_Phase2\\longTRK2_APS_MR\\terkepesz_session1_lastrun.py',
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
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='MR ', color=[0.114,0.310,0.380], colorSpace='rgb',
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Üdvözöljük a TTK Agyi Képalkotó Központjában!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
import os
os.system('color')
from termcolor import colored, cprint
import colorama
colorama.init()
win.mouseVisible = False


# Initialize components for Routine "anatomy"
anatomyClock = core.Clock()
anatomy_text = visual.TextStim(win=win, name='anatomy_text',
    text='Anatómiai felvételek következnek.\n\nA felvételek közben videót vetítünk le Önnek.',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
general_instructions_key = keyboard.Keyboard()
general_instructions_continue = visual.TextStim(win=win, name='general_instructions_continue',
    text='Ha minden rendben, nyomja le a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "choose_video"
choose_videoClock = core.Clock()
choose_video_text = visual.TextStim(win=win, name='choose_video_text',
    text='Válasszon az alábbi videók közül.\n\nJobb mutatóujj: Skócia a levegőből\nJobb hüvelykujj: Afrika szépségei\n\nBal mutatóujj: Vihar\nBal hüvelykujj: Űr',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
choose_video_key = keyboard.Keyboard()

# Initialize components for Routine "loading"
loadingClock = core.Clock()
loading_video = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='loading_video')
loading_text = visual.TextStim(win=win, name='loading_text',
    text='A videó betölt...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "video"
videoClock = core.Clock()
end_video_key = keyboard.Keyboard()

# Initialize components for Routine "resting_state_instruction"
resting_state_instructionClock = core.Clock()
rest_instructions_text = visual.TextStim(win=win, name='rest_instructions_text',
    text='Köszönjük, vége az anatómiai mérésnek.\n\nMost a nyugalmi mérés következik.\n\nA mérés közben egy fixációs keresztet lát majd a képernyőn.\n\nNézze ezt a keresztet. Gondolatait hagyja kalandozni.\nKérjük, közben maradjon ébren. A nyugalmi mérés 8 percig tart.\n\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=0.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rest_instructions_key = keyboard.Keyboard()
rest_instructions_continue = visual.TextStim(win=win, name='rest_instructions_continue',
    text='Ha minden rendben nyomja le a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "resting_state"
resting_stateClock = core.Clock()
fx_cross = visual.TextStim(win=win, name='fx_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=0.65, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rest_end_key = keyboard.Keyboard()

# Initialize components for Routine "prepare_task"
prepare_taskClock = core.Clock()
prepare_task_text = visual.TextStim(win=win, name='prepare_task_text',
    text='Remekül csinálja, köszönjük!\n\nMost a feladatok következnek.',
    font='Arial',
    pos=(0.0, 0), height=0.05, wrapWidth=0.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prepare_task_key = keyboard.Keyboard()
prepare_task_button_text = visual.TextStim(win=win, name='prepare_task_button_text',
    text='Ha minden rendben, nyomja le a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0.0, -0.2), height=0.05, wrapWidth=0.7, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
cprint('On Screen: Welcome Message', 'blue', 'on_white')
print('Mouse disabled on screen. Keep CMD window active!')
cprint('Hit SPACE or -> to continue.', 'red')
# keep track of which components have finished
welcomeComponents = [welcome_text, key_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['right', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "anatomy"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
general_instructions_key.keys = []
general_instructions_key.rt = []
_general_instructions_key_allKeys = []
info_text = 'Anatómiai felvételek következnek.\nA felvételek közben videót vetítünk le Önnek.'
cprint(info_text, 'blue', 'on_white')
cprint('\n\nWaiting for participant response.\n\n', 'yellow')
# keep track of which components have finished
anatomyComponents = [anatomy_text, general_instructions_key, general_instructions_continue]
for thisComponent in anatomyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
anatomyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "anatomy"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = anatomyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=anatomyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anatomy_text* updates
    if anatomy_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anatomy_text.frameNStart = frameN  # exact frame index
        anatomy_text.tStart = t  # local t and not account for scr refresh
        anatomy_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anatomy_text, 'tStartRefresh')  # time at next scr refresh
        anatomy_text.setAutoDraw(True)
    if anatomy_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anatomy_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            anatomy_text.tStop = t  # not accounting for scr refresh
            anatomy_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(anatomy_text, 'tStopRefresh')  # time at next scr refresh
            anatomy_text.setAutoDraw(False)
    
    # *general_instructions_key* updates
    waitOnFlip = False
    if general_instructions_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
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
        if tThisFlipGlobal > general_instructions_key.tStartRefresh + 295.0-frameTolerance:
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
    
    # *general_instructions_continue* updates
    if general_instructions_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_continue.frameNStart = frameN  # exact frame index
        general_instructions_continue.tStart = t  # local t and not account for scr refresh
        general_instructions_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_continue, 'tStartRefresh')  # time at next scr refresh
        general_instructions_continue.setAutoDraw(True)
    if general_instructions_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_continue.tStop = t  # not accounting for scr refresh
            general_instructions_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_continue, 'tStopRefresh')  # time at next scr refresh
            general_instructions_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in anatomyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "anatomy"-------
for thisComponent in anatomyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('anatomy_text.started', anatomy_text.tStartRefresh)
thisExp.addData('anatomy_text.stopped', anatomy_text.tStopRefresh)
# check responses
if general_instructions_key.keys in ['', [], None]:  # No response was made
    general_instructions_key.keys = None
thisExp.addData('general_instructions_key.keys',general_instructions_key.keys)
if general_instructions_key.keys != None:  # we had a response
    thisExp.addData('general_instructions_key.rt', general_instructions_key.rt)
thisExp.addData('general_instructions_key.started', general_instructions_key.tStartRefresh)
thisExp.addData('general_instructions_key.stopped', general_instructions_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('general_instructions_continue.started', general_instructions_continue.tStartRefresh)
thisExp.addData('general_instructions_continue.stopped', general_instructions_continue.tStopRefresh)
cprint('Button pressed: d', 'green')

# ------Prepare to start Routine "choose_video"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
choose_video_key.keys = []
choose_video_key.rt = []
_choose_video_key_allKeys = []
print('Participant chooses video.')
# keep track of which components have finished
choose_videoComponents = [choose_video_text, choose_video_key]
for thisComponent in choose_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
choose_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "choose_video"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = choose_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=choose_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *choose_video_text* updates
    if choose_video_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choose_video_text.frameNStart = frameN  # exact frame index
        choose_video_text.tStart = t  # local t and not account for scr refresh
        choose_video_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choose_video_text, 'tStartRefresh')  # time at next scr refresh
        choose_video_text.setAutoDraw(True)
    if choose_video_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > choose_video_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            choose_video_text.tStop = t  # not accounting for scr refresh
            choose_video_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(choose_video_text, 'tStopRefresh')  # time at next scr refresh
            choose_video_text.setAutoDraw(False)
    
    # *choose_video_key* updates
    waitOnFlip = False
    if choose_video_key.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        choose_video_key.frameNStart = frameN  # exact frame index
        choose_video_key.tStart = t  # local t and not account for scr refresh
        choose_video_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choose_video_key, 'tStartRefresh')  # time at next scr refresh
        choose_video_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(choose_video_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(choose_video_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if choose_video_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > choose_video_key.tStartRefresh + 298.5-frameTolerance:
            # keep track of stop time/frame for later
            choose_video_key.tStop = t  # not accounting for scr refresh
            choose_video_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(choose_video_key, 'tStopRefresh')  # time at next scr refresh
            choose_video_key.status = FINISHED
    if choose_video_key.status == STARTED and not waitOnFlip:
        theseKeys = choose_video_key.getKeys(keyList=['a', 'd', 'c', 'b'], waitRelease=False)
        _choose_video_key_allKeys.extend(theseKeys)
        if len(_choose_video_key_allKeys):
            choose_video_key.keys = _choose_video_key_allKeys[-1].name  # just the last key pressed
            choose_video_key.rt = _choose_video_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in choose_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "choose_video"-------
for thisComponent in choose_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('choose_video_text.started', choose_video_text.tStartRefresh)
thisExp.addData('choose_video_text.stopped', choose_video_text.tStopRefresh)
# check responses
if choose_video_key.keys in ['', [], None]:  # No response was made
    choose_video_key.keys = None
thisExp.addData('choose_video_key.keys',choose_video_key.keys)
if choose_video_key.keys != None:  # we had a response
    thisExp.addData('choose_video_key.rt', choose_video_key.rt)
thisExp.addData('choose_video_key.started', choose_video_key.tStartRefresh)
thisExp.addData('choose_video_key.stopped', choose_video_key.tStopRefresh)
thisExp.nextEntry()
key_pressed=choose_video_key.keys
selected_video='stimuli/eye_of_the_storm.mp4'
if key_pressed=='d':
    selected_video='stimuli/beauty_of_africa.mp4'
elif key_pressed=='c':
    selected_video='stimuli/scotland.mp4'
elif key_pressed=='a':
    selected_video='stimuli/hubble_final.mp4'
elif key_pressed=='b':
    selected_video='stimuli/eye_of_the_storm.mp4'
    
print('Video selected: ', selected_video)

# ------Prepare to start Routine "loading"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
cprint('On Screen: A videó betölt...', 'blue', 'on_white')
# keep track of which components have finished
loadingComponents = [loading_video, loading_text]
for thisComponent in loadingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
loadingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "loading"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = loadingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=loadingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *loading_text* updates
    if loading_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        loading_text.frameNStart = frameN  # exact frame index
        loading_text.tStart = t  # local t and not account for scr refresh
        loading_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_text, 'tStartRefresh')  # time at next scr refresh
        loading_text.setAutoDraw(True)
    if loading_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            loading_text.tStop = t  # not accounting for scr refresh
            loading_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_text, 'tStopRefresh')  # time at next scr refresh
            loading_text.setAutoDraw(False)
    # *loading_video* period
    if loading_video.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        loading_video.frameNStart = frameN  # exact frame index
        loading_video.tStart = t  # local t and not account for scr refresh
        loading_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_video, 'tStartRefresh')  # time at next scr refresh
        loading_video.start(3.0)
    elif loading_video.status == STARTED:  # one frame should pass before updating params and completing
        loading_video.complete()  # finish the static period
        loading_video.tStop = loading_video.tStart + 3.0  # record stop time
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "loading"-------
for thisComponent in loadingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('loading_video.started', loading_video.tStart)
thisExp.addData('loading_video.stopped', loading_video.tStop)
thisExp.addData('loading_text.started', loading_text.tStartRefresh)
thisExp.addData('loading_text.stopped', loading_text.tStopRefresh)

# ------Prepare to start Routine "video"-------
continueRoutine = True
routineTimer.add(2700.000000)
# update component parameters for each repeat
video_file = visual.MovieStim3(
    win=win, name='video_file',units='pix', 
    noAudio = False,
    filename=selected_video,
    ori=0, pos=(0, 0), opacity=1,
    loop=True,
    size=(1920,1080),
    depth=0.0,
    )
end_video_key.keys = []
end_video_key.rt = []
_end_video_key_allKeys = []
cprint('Video playing...', 'blue', 'on_white')
cprint('Wait until the end of the anatomical sequences.', 'red', 'on_white')
cprint('Press SPACE or -> to end video.', 'red')
# keep track of which components have finished
videoComponents = [video_file, end_video_key]
for thisComponent in videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "video"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *video_file* updates
    if video_file.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        video_file.frameNStart = frameN  # exact frame index
        video_file.tStart = t  # local t and not account for scr refresh
        video_file.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(video_file, 'tStartRefresh')  # time at next scr refresh
        video_file.setAutoDraw(True)
    if video_file.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > video_file.tStartRefresh + 2700.0-frameTolerance:
            # keep track of stop time/frame for later
            video_file.tStop = t  # not accounting for scr refresh
            video_file.frameNStop = frameN  # exact frame index
            win.timeOnFlip(video_file, 'tStopRefresh')  # time at next scr refresh
            video_file.setAutoDraw(False)
    
    # *end_video_key* updates
    waitOnFlip = False
    if end_video_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        end_video_key.frameNStart = frameN  # exact frame index
        end_video_key.tStart = t  # local t and not account for scr refresh
        end_video_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_video_key, 'tStartRefresh')  # time at next scr refresh
        end_video_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_video_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_video_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_video_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_video_key.tStartRefresh + 2695.0-frameTolerance:
            # keep track of stop time/frame for later
            end_video_key.tStop = t  # not accounting for scr refresh
            end_video_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_video_key, 'tStopRefresh')  # time at next scr refresh
            end_video_key.status = FINISHED
    if end_video_key.status == STARTED and not waitOnFlip:
        theseKeys = end_video_key.getKeys(keyList=['right', 'space'], waitRelease=False)
        _end_video_key_allKeys.extend(theseKeys)
        if len(_end_video_key_allKeys):
            end_video_key.keys = _end_video_key_allKeys[-1].name  # just the last key pressed
            end_video_key.rt = _end_video_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "video"-------
for thisComponent in videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
video_file.stop()
# check responses
if end_video_key.keys in ['', [], None]:  # No response was made
    end_video_key.keys = None
thisExp.addData('end_video_key.keys',end_video_key.keys)
if end_video_key.keys != None:  # we had a response
    thisExp.addData('end_video_key.rt', end_video_key.rt)
thisExp.addData('end_video_key.started', end_video_key.tStartRefresh)
thisExp.addData('end_video_key.stopped', end_video_key.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "resting_state_instruction"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
rest_instructions_key.keys = []
rest_instructions_key.rt = []
_rest_instructions_key_allKeys = []
cprint('On Screen', 'blue', 'on_white')
cprint('Köszönjük, vége az anatómiai mérésnek.', 'blue', 'on_white')
cprint('Most a nyugalmi mérés következik.', 'blue', 'on_white')
cprint('A mérés közben egy fixációs keresztet lát majd a képernyőn.', 'blue', 'on_white')
cprint('Nézze ezt a keresztet. Gondolatait hagyja kalandozni.',  'blue', 'on_white')
cprint('Kérjük, közben maradjon ébren. A nyugalmi mérés 8 percig tart.',  'blue', 'on_white')
cprint('Waiting for participant response...', 'yellow')

# keep track of which components have finished
resting_state_instructionComponents = [rest_instructions_text, rest_instructions_key, rest_instructions_continue]
for thisComponent in resting_state_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
resting_state_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "resting_state_instruction"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = resting_state_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=resting_state_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_instructions_text* updates
    if rest_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_text.frameNStart = frameN  # exact frame index
        rest_instructions_text.tStart = t  # local t and not account for scr refresh
        rest_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_text, 'tStartRefresh')  # time at next scr refresh
        rest_instructions_text.setAutoDraw(True)
    if rest_instructions_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_instructions_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_instructions_text.tStop = t  # not accounting for scr refresh
            rest_instructions_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_instructions_text, 'tStopRefresh')  # time at next scr refresh
            rest_instructions_text.setAutoDraw(False)
    
    # *rest_instructions_key* updates
    waitOnFlip = False
    if rest_instructions_key.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_key.frameNStart = frameN  # exact frame index
        rest_instructions_key.tStart = t  # local t and not account for scr refresh
        rest_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_key, 'tStartRefresh')  # time at next scr refresh
        rest_instructions_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rest_instructions_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rest_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rest_instructions_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_instructions_key.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_instructions_key.tStop = t  # not accounting for scr refresh
            rest_instructions_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_instructions_key, 'tStopRefresh')  # time at next scr refresh
            rest_instructions_key.status = FINISHED
    if rest_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = rest_instructions_key.getKeys(keyList=['d'], waitRelease=False)
        _rest_instructions_key_allKeys.extend(theseKeys)
        if len(_rest_instructions_key_allKeys):
            rest_instructions_key.keys = _rest_instructions_key_allKeys[-1].name  # just the last key pressed
            rest_instructions_key.rt = _rest_instructions_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rest_instructions_continue* updates
    if rest_instructions_continue.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_continue.frameNStart = frameN  # exact frame index
        rest_instructions_continue.tStart = t  # local t and not account for scr refresh
        rest_instructions_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_continue, 'tStartRefresh')  # time at next scr refresh
        rest_instructions_continue.setAutoDraw(True)
    if rest_instructions_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_instructions_continue.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_instructions_continue.tStop = t  # not accounting for scr refresh
            rest_instructions_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_instructions_continue, 'tStopRefresh')  # time at next scr refresh
            rest_instructions_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_state_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "resting_state_instruction"-------
for thisComponent in resting_state_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rest_instructions_text.started', rest_instructions_text.tStartRefresh)
thisExp.addData('rest_instructions_text.stopped', rest_instructions_text.tStopRefresh)
# check responses
if rest_instructions_key.keys in ['', [], None]:  # No response was made
    rest_instructions_key.keys = None
thisExp.addData('rest_instructions_key.keys',rest_instructions_key.keys)
if rest_instructions_key.keys != None:  # we had a response
    thisExp.addData('rest_instructions_key.rt', rest_instructions_key.rt)
thisExp.addData('rest_instructions_key.started', rest_instructions_key.tStartRefresh)
thisExp.addData('rest_instructions_key.stopped', rest_instructions_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rest_instructions_continue.started', rest_instructions_continue.tStartRefresh)
thisExp.addData('rest_instructions_continue.stopped', rest_instructions_continue.tStopRefresh)
cprint('Button pressed: d', 'green')

# ------Prepare to start Routine "resting_state"-------
continueRoutine = True
# update component parameters for each repeat
rest_end_key.keys = []
rest_end_key.rt = []
_rest_end_key_allKeys = []
cprint('\n\nFixation cross on screen.', 'blue', 'on_white') 
cprint('Wait until end of resting state sequence.', 'red', 'on_white')
cprint('Press SPACE or -> to end resting state.', 'red')
# keep track of which components have finished
resting_stateComponents = [fx_cross, rest_end_key]
for thisComponent in resting_stateComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
resting_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "resting_state"-------
while continueRoutine:
    # get current time
    t = resting_stateClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=resting_stateClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fx_cross* updates
    if fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fx_cross.frameNStart = frameN  # exact frame index
        fx_cross.tStart = t  # local t and not account for scr refresh
        fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fx_cross, 'tStartRefresh')  # time at next scr refresh
        fx_cross.setAutoDraw(True)
    
    # *rest_end_key* updates
    waitOnFlip = False
    if rest_end_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        rest_end_key.frameNStart = frameN  # exact frame index
        rest_end_key.tStart = t  # local t and not account for scr refresh
        rest_end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_end_key, 'tStartRefresh')  # time at next scr refresh
        rest_end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rest_end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rest_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rest_end_key.status == STARTED and not waitOnFlip:
        theseKeys = rest_end_key.getKeys(keyList=['right', 'space'], waitRelease=False)
        _rest_end_key_allKeys.extend(theseKeys)
        if len(_rest_end_key_allKeys):
            rest_end_key.keys = _rest_end_key_allKeys[-1].name  # just the last key pressed
            rest_end_key.rt = _rest_end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_stateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "resting_state"-------
for thisComponent in resting_stateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fx_cross.started', fx_cross.tStartRefresh)
thisExp.addData('fx_cross.stopped', fx_cross.tStopRefresh)
# check responses
if rest_end_key.keys in ['', [], None]:  # No response was made
    rest_end_key.keys = None
thisExp.addData('rest_end_key.keys',rest_end_key.keys)
if rest_end_key.keys != None:  # we had a response
    thisExp.addData('rest_end_key.rt', rest_end_key.rt)
thisExp.addData('rest_end_key.started', rest_end_key.tStartRefresh)
thisExp.addData('rest_end_key.stopped', rest_end_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "resting_state" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prepare_task"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
cprint('On Screen: \nMessage on screen:\n Remekül csinálja, köszönjük!',  'blue', 'on_white')
cprint('On Screen: \nMessage on screen:\nA feladatok következnek.Ha minden rendben, nyomja le a gombot a jobb hüvelykujjával.',  'blue', 'on_white')
cprint('Waiting for participant response...', 'yellow')


prepare_task_key.keys = []
prepare_task_key.rt = []
_prepare_task_key_allKeys = []
# keep track of which components have finished
prepare_taskComponents = [prepare_task_text, prepare_task_key, prepare_task_button_text]
for thisComponent in prepare_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prepare_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prepare_task"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prepare_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prepare_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prepare_task_text* updates
    if prepare_task_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prepare_task_text.frameNStart = frameN  # exact frame index
        prepare_task_text.tStart = t  # local t and not account for scr refresh
        prepare_task_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepare_task_text, 'tStartRefresh')  # time at next scr refresh
        prepare_task_text.setAutoDraw(True)
    if prepare_task_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prepare_task_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            prepare_task_text.tStop = t  # not accounting for scr refresh
            prepare_task_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prepare_task_text, 'tStopRefresh')  # time at next scr refresh
            prepare_task_text.setAutoDraw(False)
    
    # *prepare_task_key* updates
    waitOnFlip = False
    if prepare_task_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        prepare_task_key.frameNStart = frameN  # exact frame index
        prepare_task_key.tStart = t  # local t and not account for scr refresh
        prepare_task_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepare_task_key, 'tStartRefresh')  # time at next scr refresh
        prepare_task_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prepare_task_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(prepare_task_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prepare_task_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prepare_task_key.tStartRefresh + 295-frameTolerance:
            # keep track of stop time/frame for later
            prepare_task_key.tStop = t  # not accounting for scr refresh
            prepare_task_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prepare_task_key, 'tStopRefresh')  # time at next scr refresh
            prepare_task_key.status = FINISHED
    if prepare_task_key.status == STARTED and not waitOnFlip:
        theseKeys = prepare_task_key.getKeys(keyList=['d'], waitRelease=False)
        _prepare_task_key_allKeys.extend(theseKeys)
        if len(_prepare_task_key_allKeys):
            prepare_task_key.keys = _prepare_task_key_allKeys[-1].name  # just the last key pressed
            prepare_task_key.rt = _prepare_task_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *prepare_task_button_text* updates
    if prepare_task_button_text.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        prepare_task_button_text.frameNStart = frameN  # exact frame index
        prepare_task_button_text.tStart = t  # local t and not account for scr refresh
        prepare_task_button_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepare_task_button_text, 'tStartRefresh')  # time at next scr refresh
        prepare_task_button_text.setAutoDraw(True)
    if prepare_task_button_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prepare_task_button_text.tStartRefresh + 295-frameTolerance:
            # keep track of stop time/frame for later
            prepare_task_button_text.tStop = t  # not accounting for scr refresh
            prepare_task_button_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prepare_task_button_text, 'tStopRefresh')  # time at next scr refresh
            prepare_task_button_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepare_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prepare_task"-------
for thisComponent in prepare_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
cprint('Button pressed: d', 'green')
thisExp.addData('prepare_task_text.started', prepare_task_text.tStartRefresh)
thisExp.addData('prepare_task_text.stopped', prepare_task_text.tStopRefresh)
# check responses
if prepare_task_key.keys in ['', [], None]:  # No response was made
    prepare_task_key.keys = None
thisExp.addData('prepare_task_key.keys',prepare_task_key.keys)
if prepare_task_key.keys != None:  # we had a response
    thisExp.addData('prepare_task_key.rt', prepare_task_key.rt)
thisExp.addData('prepare_task_key.started', prepare_task_key.tStartRefresh)
thisExp.addData('prepare_task_key.stopped', prepare_task_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('prepare_task_button_text.started', prepare_task_button_text.tStartRefresh)
thisExp.addData('prepare_task_button_text.stopped', prepare_task_button_text.tStopRefresh)

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
