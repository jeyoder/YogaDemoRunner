#!/usr/bin/python3
import subprocess
import time

# CAN CHANGE
QUAD_NAMESPACE="phoenix"

# DO NOT CHANGE
SESSION_NAME="stack"
REFNET_NAMESPACE="refnet"
SNAPDRAGON_USERNAME="root"
SNAPDRAGON_IP=QUAD_NAMESPACE + "-snapdragon"
USE_CAMERA=True

# Printout
print("Launching stack in a tmux session. Will take ~15 seconds.")
print("This tmux session uses:")
print("Modifier: C-a")
print("Horizontal split: -")
print("Vertical split: |")
print("Launching...")

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

def halve_window(window_name, dimension):
    """ Dimension is either -v for vertical or -h for horizontal """
    command = ("tmux split-window -t "
               + SESSION_NAME 
               + ":" 
               + window_name 
               + " -d "
               + dimension)
    subprocess.run(command, shell=True)

def select_pane(window_name, position):
    """ Position is -DLRU"""
    command = ("tmux select-pane " + position)
    subprocess.run(command, shell=True)

# Create new tmux session
start_new_tmux_session()

## Launch PPRX
# Wait 5 seconds before starting streamer
# window_name = "PPRX"
# window_command = "cd /home/odroid/PP-Quad/run; pprx -f pprx.opt -v"
# launch_tmux_window(window_name)
# run_command_in_window(window_name, window_command)
# time.sleep(5)



## Launch GBX-Streamer and PPEngine 
# window_name = "GBX"
# launch_tmux_window(window_name)
# halve_window(window_name, '-v')
# 
# # Launch GBX-Streamer
# window_command = ("roslaunch refnetclientros quad.launch" + 
#     " quad_namespace:=" + QUAD_NAMESPACE + 
#     " refnet_namespace:=" + REFNET_NAMESPACE)
# run_command_in_window(window_name, window_command, 0)
# 
# # Launch PPEngine
# window_command = ("rosrun ppengine ppengine" +
#     " --ref " + REFNET_NAMESPACE + 
#     " --rov " + QUAD_NAMESPACE + 
#     " --out " + QUAD_NAMESPACE + 
#     " --config /home/odroid/PP-Quad/run/A2D.cfg" +
#     " --config /home/odroid/PP-Quad/run/SBRTK.cfg")
# run_command_in_window(window_name, window_command, 1)



## Launch Odroid ROS Files
# GPS Kalman Filter
# window_name = "GPS-KF"
# window_command = ("roslaunch gps_kf gpsQuad.launch" +
#     " quad_namespace:=" + QUAD_NAMESPACE)
# launch_tmux_window(window_name)
# run_command_in_window(window_name, window_command)

# PX4 Control
# window_command = ("ssh -t " +
#     SNAPDRAGON_USERNAME + 
#     "@" +
#     SNAPDRAGON_IP + 
#     " \'echo /home/linaro/px4 /home/linaro/mainapp.config | bash -i\'")
# run_command_in_window(window_name, window_command, 1)



## Start Snapdragon files
window_name = "SNAP"
launch_tmux_window(window_name)
halve_window(window_name, '-v')

# PX4
window_command = ("ssh -t " +
    SNAPDRAGON_USERNAME + 
    "@" +
    SNAPDRAGON_IP + 
    " \'echo /home/linaro/px4 /home/linaro/mainapp.config | bash -i\'")
run_command_in_window(window_name, window_command, 0)


# Launch Camera
if(USE_CAMERA == True):
    window_command = ("ssh -t " +
        SNAPDRAGON_USERNAME + 
        "@" +
        SNAPDRAGON_IP + 
        " \'echo roslaunch snap_cam main.launch | bash -i\'")
    run_command_in_window(window_name, window_command, 1)



# Printout
print("Attach the tmux session with: 'tmux attach -t " + SESSION_NAME + "'")
