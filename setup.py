import sys
from cx_Freeze import setup,Executable

base=None
if sys.platform =='win32' :
    base='Win32GUI'
opts={'include_files' : ['C:\\Users\\TROJAN\\Downloads\\minecraft.png'],'includes':['re']}
setup( name='LOTTO',
       version='1.0',
       description='Lucky Number Picker',
       author='Tarun Chauhan',
       options={'build_exe':opts},
       executables={Executable('lotto.py',base=base)})
