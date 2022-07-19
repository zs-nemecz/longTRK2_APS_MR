#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on July 19, 2022, at 12:58
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
expName = 'longTRK'  # from the Builder filename that created this script
expInfo = {'online ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['online ID'],'session_2', expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Zsuzsa\\HCCCL\\TerKepEsz_Tasks\\computer_based_tasks\\longTRK_Phase2\\longTRK2_APS_MR\\terkepesz_session2.py',
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

# Initialize components for Routine "setup"
setupClock = core.Clock()
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

# Initialize components for Routine "loading_video"
loading_videoClock = core.Clock()
loading = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='loading')
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

# Initialize components for Routine "prepare_task"
prepare_taskClock = core.Clock()
prepare_task_text = visual.TextStim(win=win, name='prepare_task_text',
    text='Remekül csinálta, köszönjük!\n\nVége az anatómiai mérésnek.',
    font='Arial',
    pos=(0.0, 0), height=0.05, wrapWidth=0.52, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prepare_task_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
print('State: Setup')
print('Mouse disabled on screen. Keep CMD window active!')
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
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
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
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
cprint('\n\nWaiting for participant response.', 'yellow')
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

# ------Prepare to start Routine "loading_video"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
cprint('On Screen: A videó betölt...', 'blue', 'on_white')
# keep track of which components have finished
loading_videoComponents = [loading, loading_text]
for thisComponent in loading_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
loading_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "loading_video"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = loading_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=loading_videoClock)
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
    # *loading* period
    if loading.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        loading.frameNStart = frameN  # exact frame index
        loading.tStart = t  # local t and not account for scr refresh
        loading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading, 'tStartRefresh')  # time at next scr refresh
        loading.start(3.0)
    elif loading.status == STARTED:  # one frame should pass before updating params and completing
        loading.complete()  # finish the static period
        loading.tStop = loading.tStart + 3.0  # record stop time
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in loading_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "loading_video"-------
for thisComponent in loading_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('loading.started', loading.tStart)
thisExp.addData('loading.stopped', loading.tStop)
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
cprint('Wait until the end of anatomical and DTI sequences', 'red', 'on_white')
cprint('Press SPACE or -> to end video', 'red')
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

# ------Prepare to start Routine "prepare_task"-------
continueRoutine = True
# update component parameters for each repeat
prepare_task_key.keys = []
prepare_task_key.rt = []
_prepare_task_key_allKeys = []
cprint('On Screen:\n Remekül csinálta, köszönjük! \nVége az anatómiai mérésnek.',  'blue', 'on_white')
cprint('Press SPACE to exit.', 'red')
# keep track of which components have finished
prepare_taskComponents = [prepare_task_text, prepare_task_key]
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
while continueRoutine:
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
    if prepare_task_key.status == STARTED and not waitOnFlip:
        theseKeys = prepare_task_key.getKeys(keyList=['d', 'space', 'right'], waitRelease=False)
        _prepare_task_key_allKeys.extend(theseKeys)
        if len(_prepare_task_key_allKeys):
            prepare_task_key.keys = _prepare_task_key_allKeys[-1].name  # just the last key pressed
            prepare_task_key.rt = _prepare_task_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# the Routine "prepare_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
