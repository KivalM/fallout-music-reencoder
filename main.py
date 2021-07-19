import os
import sys
import getopt
import subprocess

sys.setrecursionlimit(10**6)
home = os.environ["HOME"]
falloutdir = os.path.join(
    home,  ".local/share/Steam/steamapps/common/Fallout 3 goty/Data")
os.chdir(falloutdir)
dbug = False
argv = sys.argv[1:]
run = True
backup = True
try:
    opts, args = getopt.getopt(
        argv, "d:ahg:b", ["dir=", "debug", "help", "game=", "backup"])
except:
    print("Error")
for opt, arg in opts:
    if opt in ['-d', "--dir"]:
        falloutdir = arg
    elif opt in ['-a', "--debug"]:
        dbug = True
    elif opt in ['-b', "--nobackup"]:
        backup = False
    elif opt in ['-g', "--game"]:
        if arg == 3:
            falloutdir = os.path.join(
                home,  ".local/share/Steam/steamapps/common/Fallout 3 goty/")
        elif arg == "nv":
            falloutdir = os.path.join(
                home,  ".local/share/Steam/steamapps/common/Fallout New Vegas/")
    elif opt in ['-h', "--help"]:
        run = False
        print("""
This program will go through the fallout directory recursively and encode all mp3s to 192kbps to avoid skipping of tracks caused by Proton's recent regressions
USAGE: 
main.py -d FALLOUTDIRECTORY -b
-d or --dir 
    tells the program where to look for fallout.
    Default location is $HOME/.local/share/Steam/steamapps/common/Fallout 3 goty
    point it to your Data directory. it will work faster
-a or --debug 
    shows the output of ffmpeg  
-b or --nobackup 
    tells the program to delete the unencoded files
-g or --game 
    chooses the game
    this is only effective if using the default game directory 
        i.e not using -d to specify a dir
    valid options are '3' and 'nv'
    Fallout 3 by default
-h 
    displays this message
        """)


def convert(file):
    new = "BAK_" + file
    cmd = "mv {} {}".format(file, new)
    result = subprocess.run([cmd], stdout=subprocess.DEVNULL, shell=True)
    print("CONVERTING: ", file)
    cmd = 'ffmpeg -i "{}" -codec:a libmp3lame -b:a 192k "{}"'.format(
        new, file)
    if not dbug:
        cmd += " >> /dev/null"
    if not backup:
        cmd = cmd + "&&rm {}".format(new)
    result = subprocess.run([cmd], stdout=subprocess.DEVNULL, shell=True)
    print(result.stderr)


def recursive(currdir):
    os.chdir(currdir)
    items = os.listdir()
    print("LOOKING IN: ", currdir)
    for item in items:
        directory = os.path.join(currdir, item)
        if os.path.isdir(directory):
            recursive(directory)
        else:
            if item[-3:] == "mp3":
                convert(item)
                print("DONE::", item)


def main():
    if run:
        recursive(falloutdir)


main()
