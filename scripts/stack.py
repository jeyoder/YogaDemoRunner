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
USE_CAMERA=False

# Printout
print("Launching stack in a tmux session.")
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
window_command = "cd /home/odroid/PP-Quad/run; pprx -f pprx.opt -v"
subprocess.run("tmux rename-window -t " + SESSION_NAME + ":1 " + window_name, shell=True)
run_command_in_window(window_name, window_command)


## Launch GBX-Streamer and PPEngine 
window_name = "GBX"
launch_tmux_window(window_name)
quarter_window(window_name)

# Launch GBX-Streamer
window_command = ("roslaunch refnetclientros refnet.launch")
run_command_in_window(window_name, window_command, 0)

# Launch PPEngine
window_command = ("rosrun ppengineros ppengineros" +
    " --in /home/odroid/PP-Quad/run/pprx_read" + 
    " --out " + QUAD_NAMESPACE + 
    " --config /home/odroid/PP-Quad/run/A2D.cfg" +
    " --config /home/odroid/PP-Quad/run/SBRTK.cfg")
run_command_in_window(window_name, window_command, 1)

# Launch PPEngine
window_command = ("cd /home/odroid/PP-Quad/run; echo 'Piping...'; < pprx_write tee pprx_read pprx.gbx > /dev/null")
run_command_in_window(window_name, window_command, 2)


## Launch Odroid ROS Files
window_name = "ROS"
launch_tmux_window(window_name)
quarter_window(window_name)

# GPS Kalman Filter
# window_command = ("roslaunch gps_kf gpsQuad.launch" +
#     " quad_namespace:=" + QUAD_NAMESPACE)
# run_command_in_window(window_name, window_command, 0)

# Waypoint control
# window_command = ("roslaunch waypoint_control stack.launch")
# run_command_in_window(window_name, window_command, 2)


## Start Snapdragon files
window_name = "SNAP"
launch_tmux_window(window_name)
quarter_window(window_name)

# PX4
# window_command = ("ssh -t " +
#     SNAPDRAGON_USERNAME + 
#     "@" +
#     SNAPDRAGON_IP + 
#     " \'/home/linaro/px4 /home/linaro/mainapp.config\'")
# run_command_in_window(window_name, window_command, 0)

# PX4 Control
# window_command = ("ssh -t " +
#     SNAPDRAGON_USERNAME + 
#     "@" +
#     SNAPDRAGON_IP + 
#     " \'echo roslaunch px4_control stack.launch ns:=" + QUAD_NAMESPACE + " | bash -i\'")
# run_command_in_window(window_name, window_command, 1)

# Launch Camera
# if(USE_CAMERA == True):
#     window_command = ("ssh -t " +
#         SNAPDRAGON_USERNAME + 
#         "@" +
#         SNAPDRAGON_IP + 
#         " \'echo roslaunch snap_cam main.launch | bash -i\'")
#     run_command_in_window(window_name, window_command, 2)



# Printout
print("Attach the tmux session with: 'tmux attach -t " + SESSION_NAME + "'")
