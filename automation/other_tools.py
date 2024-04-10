
import gzip
import sys
sys.path.append('bn_python_common.zip')
from bn_python_common import *


def decodeSavedAfxFile(s):
    d = files.readall(s, 'rb')
    data = gzip.decompress(d)
    print(data.decode('utf-8'))



def winEnumHandler( hwnd, ctx=None ):
    import win32gui
    if win32gui.IsWindowVisible( hwnd ):
        trace ( ( hwnd ), win32gui.GetWindowText( hwnd ) )

def findWindows():
    all = pywinauto.findwindows.find_windows(title_re=".*Astrofox.*")
    for item in all:
        trace(item)

