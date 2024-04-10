


from ben_python_common import *
import time
import os
import pywinauto
import subprocess
#~ 935, 781

from pywinauto import Application
from pywinauto import findwindows
#~ from pywinauto.keyboard import type_keys


r"""
flac, high, 40fps
flac, low, 40fps
m4a, high, 70fps
m4a, low, 106fps

make symlink for "C:\Users\mf\AppData\Local\Temp\Astrofox" to a ram drive

used to do: 12fps at low quality, got about 40fps
now trying 8fps at high quality 

disk speedreading from the hdd might be causing it too
    N, reading from c drive is the same

the fps might be limited by flac->aac conversion
that is the output Audio: AAC 44100Hz stereo 192kbps [A: SoundHandler (aac lc, 44100 Hz, stereo, 192 kb/s)]
which is reasonable i guess

"""

import win32gui

# def winEnumHandler( hwnd, ctx ):
#     if win32gui.IsWindowVisible( hwnd ):
#         trace ( ( hwnd ), win32gui.GetWindowText( hwnd ) )
# 
# win32gui.EnumWindows( winEnumHandler, None )

def launch():
    os.chdir(r'D:\acool\astr\astrofox-1.4.0')
    #~ app111 = Application().start(r"C:/Users/mf/scoop/apps/nodejs/current/bin/yarn.cmd start", timeout=20)
    process = subprocess.Popen(['C:/Users/mf/scoop/apps/nodejs/current/bin/yarn.cmd', 'start'])
    time.sleep(3)
    #~ all = pywinauto.findwindows.find_windows(title_re=".*Astrofox.*")
    #~ for item in all:
        #~ trace(item)
    
    app222 =  Application().connect(title='Astrofox', timeout=10)
    return app222

def goOne(audioToProcess, finalOutput):
    expout = r'H:\ttt.mp4' # cannot be changed
    assertTrue(expout == r'H:\ttt.mp4' , 'or update the js in the build')
    assertTrue(not ' ' in expout)
    assertTrue(not files.exists(expout))
    assertTrue(not  files.exists(expout + '.mp4'))
    
    app = launch()
    time.sleep(3)
    win = app.window(title_re='.*Astrofox.*')
    win.maximize() # need it for click coords
    time.sleep(3)
    win.type_keys('{VK_CONTROL}{VK_MENU}o')
    time.sleep(3)
    win.type_keys('{TAB}'); time.sleep(1)
    win.type_keys('{TAB}'); time.sleep(1)
    win.type_keys('{TAB}'); time.sleep(1)
    win.type_keys('123'); time.sleep(1)
    
    if False:
        win.type_keys('^%o'); time.sleep(4)
        win.type_keys(r'"D:\mirr3\devhere\project2d.afx"'); time.sleep(1)
        win.type_keys('{ENTER}'); time.sleep(4)
        win.type_keys('^%L'); time.sleep(4)
        #~ win.type_keys(r'"H:\Fujiyama.flac"'); time.sleep(1)
        #~ win.type_keys(r'"H:\Fujiyama.flac"'); time.sleep(1)
        win.type_keys(rf'"{audioToProcess}"'); time.sleep(1)
        win.type_keys('{ENTER}'); time.sleep(4)
        win.type_keys('^%R'); time.sleep(4)
        time.sleep(6) # wait for it to autofill dest…;
        pywinauto.mouse.click(button='left', coords=(935, 781))
        #~ Click at the specified coordinates
    else:
        os.chdir(r'D:\mirr3\m\software_save\current_exe\benutils\apps\LnzScript 0.51')
        audParama = rf'"{audioToProcess}"'
        files.run([r"D:\mirr3\m\software_save\current_exe\benutils\apps\LnzScript 0.51\lnzscript.exe", r"D:\mirr3\devhere\w2bautomate\goReal.js", audParama ])
        
                
    #~ app_top_window = app.top_window()
    #~ app_top_window.maximize()
    while True:
        time.sleep(3)
        if (files.exists(expout)):
            print('waiting-seeing...-')
            if canRenameFile(expout):
                time.sleep(5)
                files.run('taskkill /f /im node.exe', shell=True, throwOnFailure=None)
                time.sleep(1)
                files.run('taskkill /f /im node.exe', shell=True, throwOnFailure=None)
                time.sleep(1)
                files.run('taskkill /f /im node.exe', shell=True, throwOnFailure=None)
                time.sleep(1)
                files.move(expout, finalOutput, False)
                return True
        else:
            print('waiting-not seeing...-')
                

def canRenameFile(s):
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


# ones at first are 12fps………
# ones 2/26 are 8fps
# ones 2/27 at midnight are 6fps

def goAll():
    
    #~ for f, short in files.listfiles(r'G:\larger-files-out\results'):
    for f, short in files.listfiles(r'D:\mirr3\transfer\a'):
        if files.exists(r'D:\mirr3\devhere\w2bautomate\stop.txt'):
            break
    #~ for f, short in files.listfiles(r'H:\atemp'):
        #~ if '2c.flac' in short and files.getsize(f) < 370 * 1024 * 1024:
        #~ if '2c.flac' in short and files.getsize(f) < 400 * 1024 * 1024:
        if '.flac' in short and files.getsize(f) < 400 * 1024 * 1024:
            # we confirmed that 400mb generally works
        #~ if '2c.flac' in short and files.getsize(f) > 200 * 1024 * 1024 and files.getsize(f) < 400 * 1024 * 1024:
            finalOutput = r'G:\larger-files-out\vidres/' + short + '.out.mp4'
            if files.exists(finalOutput):
                trace('skipping already exists', f)
            else:
                trace('doing')
                goOne(f, finalOutput)
                time.sleep(30)
    
    

goAll()
#~ launch()
#~ goOne(r'D:\mirr3\devhere\w2bsample2short.ogg', r'G:\larger-files-out\vidres\w2bsample2short.mp4')
#~ files.run('taskkill /f /im node.exe', shell=True, throwOnFailure=None)…
#~ app = Application().start("Notepad.exe")
#~ writer_app = app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
#~ writer_app.type_keys("test 123123")
#~ time.sleep(4)
#~ app.type_keys("test 123123")
