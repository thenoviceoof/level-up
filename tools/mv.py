import sys
import os
import subprocess

def rev(path):
    for f in os.listdir(path):
        l = len(os.listdir('.'))
        tof = "1-1-{0}-{1}".format(l-int(f.split("-")[2])+1, f.split("-")[3])
        subprocess.call(["mv",os.path.join(path,f),os.path.join(path,tof)])

rev(sys.argv[1])
