#!/usr/bin/env python3
import subprocess
import sys


input = sys.argv[1]

try:
    if float(input) > 0.0 and float(input) <= 1.0:
        brightness = input
    else:
        raise Exception("wrong argument")
except:
    print("Give brightness argument 0.0 - 1")
    sys.exit(1)



get_screens = 'xrandr | grep " connected" | cut -f1 -d " "'

p1 = subprocess.Popen(get_screens, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
screens = p1.communicate()[0]

screen_list = screens.splitlines()

for screen in screen_list:
    subprocess.run(['xrandr', '--output', screen, '--brightness', str(brightness)])
