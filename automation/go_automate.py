

import time
import os
import pywinauto
from pywinauto import Application
from pywinauto import findwindows
import subprocess
import sys
sys.path.append('bn_python_common.zip')
from bn_python_common import *

# please close any windows with title 'Astrofox' before running the script

def getConfigs():
    config = Bucket()
    
    # must match in VideoSettings.js
    config.expectedOut = 'D:\\current_video.mp4' 
        
    # path to yarn.cmd, it is usually here after running npm install -g yarn
    config.yarnCmd = f'C:/Users/{os.getlogin()}/scoop/apps/nodejs/current/bin/yarn.cmd'
    assertTrue(files.isfile(config.yarnCmd))
    
    # path to lnzscript, download from https://github.com/moltenform/lnzscript
    config.pathLnzScriptExe = r"C:\Program Files\LnzScript 0.51\lnzscript.exe"
    assertTrue(files.isfile(config.pathLnzScriptExe))
    
    # pause after rendering, to let cpu take a break
    config.sleepAfterRender = 30
    
    # dir with input files
    config.directoryWithInputFiles = 'D:\\input_audio' 
    
    # suffix of input files
    config.inputFileSuffix = '.mp3' 
    
    # you don't need to edit these ones 
    config.pathLnzScript = os.path.abspath('./go_automate_lnz_part.js')
    assertTrue(files.isfile(config.pathLnzScript))
    
    
    return config


def launch():
    config = getConfigs()
    os.chdir('..')
    process = subprocess.Popen([config.yarnCmd, 'start'])
    sleepBetweenActions()
    appInstance =  Application().connect(title='Astrofox', timeout=10)
    return appInstance

def goOneVideo(audioToProcess, finalOutput):
    config = getConfigs()
    assertTrue(not ' ' in config.expectedOut)
    assertTrue(not files.exists(config.expectedOut),
        'incomplete results found, please delete before continuing')
    assertTrue(not files.exists(config.expectedOut + '.mp4'),
        'incomplete results found, please delete before continuing')
    assertTrue(not files.exists(finalOutput),
        'finalOutput already there')
    if files.getsize(audioToProcess) > 200 * 1024 * 1024:
        warn('this is a large input file, may need to bump up delays here and in go_automate_lnz_part.js')
    
    app = launch()
    sleepBetweenActions()
    win = app.window(title_re='.*Astrofox.*')
    win.maximize() # need it for click coords to be accurate
    
    # simulate ctrl-alt-o
    sleepBetweenActions()
    win.type_keys('{VK_CONTROL}{VK_MENU}o')
    sleepBetweenActions()
    win.type_keys('{TAB}'); time.sleep(1)
    win.type_keys('{TAB}'); time.sleep(1)
    win.type_keys('{TAB}'); time.sleep(1)
    win.type_keys('1'); time.sleep(1)
    
    # call out to lnzscript.exe to do this part
    # because we just want to simulate keys to whatever window is in front
    # instead of pywinauto sending to a specific window
    os.chdir(files.getparent(config.pathLnzScriptExe))
    passPathIn = rf'"{audioToProcess}"'
    files.run([config.pathLnzScriptExe, config.pathLnzScript, passPathIn ])
    
    while True:
        sleepBetweenActions()
        if not (files.exists(config.expectedOut)):
            print('waiting-output not seen yet...')
        else:
            if not canRenameFile(config.expectedOut):
                print('waiting-saw output file but it is still being worked on...')
            else:
                print('complete, closing down')
            
        if (files.exists(config.expectedOut)):
            print('Waiting-seeing...-')
            if canRenameFile(config.expectedOut):
                killNodeAndWait()
                killNodeAndWait()
                killNodeAndWait()
                killNodeAndWait()
                killNodeAndWait()
                files.move(config.expectedOut, finalOutput, False)
                return True
        else:
            print('waiting-not seeing...-')

def killNodeAndWait():
    config = getConfigs()
    files.run('taskkill /f /im node.exe', shell=True, throwOnFailure=None)
    sleepBetweenActions()

def canRenameFile(s):
    config = getConfigs()
    assertTrue(not files.exists(s+'.mp4'))
    try:
        files.move(s, s+'.mp4', True)
        files.move(s + '.mp4', s, True)
    except Exception as e:
        if 'MoveFileExW' in str(e):
            pass
        else:
            raise
        return False
    return True



def goEntireDirectory(dir, mustEndWith):
    config = getConfigs()
    for f, short in files.listfiles(dir):
        if f.endswith(mustEndWith):
            finalOutput = f + '.out.mp4'
            if files.exists(finalOutput):
                trace('skipping, already exists', f, finalOutput)
            else:
                trace('doing')
                goOneVideo(f, finalOutput)
                time.sleep(config.sleepAfterRender)
            
    

def sleepBetweenActions():
    # add frequent sleeps, to wait for ui to be ready
    config = getConfigs()
    Time.sleep(4)


if __name__ == '__main__':
    config = getConfigs()
    goEntireDirectory(config.directoryWithInputFiles, config.inputFileSuffix)


