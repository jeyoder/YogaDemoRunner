#!/usr/bin/python3
import subprocess
import time
import os

# CAN CHANGE
QUAD_NAMESPACE="yoga"

# DO NOT CHANGE
SESSION_NAME="stack"
REFNET_NAMESPACE="refnet"
SNAPDRAGON_USERNAME="root"
SNAPDRAGON_IP=QUAD_NAMESPACE + "-snapdragon"
USE_CAMERA=True

# Printout
print("Launching stack in a tmux session.")
print("This tmux session uses:")
print("Modifier: C-b")
print("Horizontal split: \"")
print("Vertical split: %")
print("Launching...")

# Find local directory
PATH=os.path.dirname(os.path.realpath(__file__))
print("PATH={}".format(PATH))

def start_new_tmux_session():
    command = "tmux new -s " + SESSION_NAME + " -d"
    subprocess.run(command, shell=True)

def launch_tmux_window(window_name):
    command = ("tmux new-window -t "
               + SESSION_NAME 
               + " -n " 
               + window_name)
    subprocess.run(command, shell=True)

def run_command_in_window(window_name, window_command, pane_number=0):
    command = ("tmux send -t " 
               + SESSION_NAME 
               + ":" 
               + window_name 
               + "."
               + str(pane_number)
               + " \""
               + window_command
               +"\" Enter")
    subprocess.run(command, shell=True)

def split_window(window_name, dimension, pane_number=0):
    """ Dimension is either -v for vertical or -h for horizontal """
    command = ("tmux split-window -t "
               + SESSION_NAME 
               + ":" 
               + window_name 
               + "."
               + str(pane_number)
               + " -d "
               + dimension)
    subprocess.run(command, shell=True)

def quarter_window(window_name):
    split_window(window_name, '-h', 0)
    split_window(window_name, '-v', 0)
    split_window(window_name, '-v', 2)

# Create new tmux session
start_new_tmux_session()

## Launch PPRX
# Wait 5 seconds before starting streamer
window_name = "PPRX"
launch_tmux_window(window_name)
window_command = "cd " + PATH + "; pprx -f pprx.opt -v"
subprocess.run("tmux rename-window -t " + SESSION_NAME + ":1 " + window_name, shell=True)
run_command_in_window(window_name, window_command)

## Launch Odroid ROS Files
window_name = "ROS"
launch_tmux_window(window_name)
quarter_window(window_name)

# GPS Kalman Filter
#window_command = ("roslaunch gps_kf gpsQuad.launch" +
#    " quad_namespace:=" + QUAD_NAMESPACE)
#run_command_in_window(window_name, window_command, 0)

run_command_in_window(window_name, "roscore", 1)

time.sleep(2)

# Printouts
window_command = ("rostopic echo /" + QUAD_NAMESPACE + "/local_odom")
run_command_in_window(window_name, window_command, 0)

window_command = ("rostopic echo /" + QUAD_NAMESPACE + "/Attitude2D")
run_command_in_window(window_name, window_command, 2)

window_command = ("rostopic echo /" + QUAD_NAMESPACE + "/SingleBaselineRTK")
run_command_in_window(window_name, window_command, 3)

# Launch PPEngine


## Launch GBX-Streamer and PPEngine 
window_name = "PPEngine"
launch_tmux_window(window_name)
quarter_window(window_name)

window_command = ("rosrun ppengineros ppengineros" +
    " --in" + PATH+ "/pprx_read" + 
    " --out " + QUAD_NAMESPACE + 
    " --config " + PATH + "/A2D.cfg" +
    " --config " + PATH+ "/SBRTK.cfg" +
    " --skip 40")
run_command_in_window(window_name, window_command, 1)

# Launch PPEngine
window_command = ("cd " + PATH+"; echo 'Piping...'; < pprx_write tee pprx_read pprx.gbx > /dev/null")
run_command_in_window(window_name, window_command, 2)

window_command = ("roslaunch gnss_visualization gnss.launch")
run_command_in_window(window_name, window_command, 3)

window_command = ("roslaunch gps_kf gpsYoga.launch")
run_command_in_window(window_name, window_command, 0)

# Printout
print("Attach the tmux session with: 'tmux attach -t " + SESSION_NAME + "'")
