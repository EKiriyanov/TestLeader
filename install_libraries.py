import subprocess

from time import sleep

cmds = ['unittest','requests', 'googlesearch', 'selenium'] # Libraries to install

for cmd in cmds:
    try:
        subprocess.Popen("pip install " + cmd, shell = True)
        print ("\n Library was installed:", cmd)
    except:
        print("Library was NOT installed", cmd)