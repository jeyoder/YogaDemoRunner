#!/usr/local/bin/python3
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
    return
    command = ("tmux new-window -t "
               + SESSION_NAME 
               + " -n " 
               + window_name)
    subprocess.run(command, shell=True)

def run_command_in_window(window_name, window_command):
    print(window_command)
    return
    command = ("tmux send -t " 
               + SESSION_NAME 
               + ":" 
               + window_name 
               + " '"
               + window_command
               +"' Enter")
    subprocess.run(command, shell=True)

# Create new tmux session
start_new_tmux_session()

# Launch PPRX
# Wait 5 seconds before starting streamer
window_name = "PPRX"
window_command = "cd /home/odroid/PP-Quad/run; pprx -f pprx.opt -v"
launch_tmux_window(window_name)
run_command_in_window(window_name, window_command)
time.sleep(5)

# Launch GBX-Streamer
window_name = "GBX-ROS"
window_command = ("roslaunch refnetclientros quad.launch" + 
    " quad_namespace:=" + QUAD_NAMESPACE + 
    " refnet_namespace:=" + REFNET_NAMESPACE)
launch_tmux_window(window_name)
run_command_in_window(window_name, window_command)

# Launch PPEngine
window_name = "PP-Engine"
window_command = ("rosrun ppengine ppengine" +
    " --ref " + REFNET_NAMESPACE + 
    " --rov " + QUAD_NAMESPACE + 
    " --out " + QUAD_NAMESPACE + 
    " --config /home/odroid/PP-Quad/run/A2D.cfg" +
    " --config /home/odroid/PP-Quad/run/SBRTK.cfg")
launch_tmux_window(window_name)
run_command_in_window(window_name, window_command)

# Launch GPS-Kalman-Filter
window_name = "GPS-KF"
window_command = ("roslaunch gps_kf gpsQuad.launch" +
    " quad_namespace:=" + QUAD_NAMESPACE)
launch_tmux_window(window_name)
run_command_in_window(window_name, window_command)

# Launch Camera
if(USE_CAMERA == True):
    window_name = "SNAPCAM"
    window_command = ("ssh -t " +
        SNAPDRAGON_USERNAME + 
        "@" +
        SNAPDRAGON_IP + 
        " \"bash -ic 'roslaunch snap_cam main.launch'\"")
    launch_tmux_window(window_name)
    run_command_in_window(window_name, window_command)

# Printout
print("Attach the tmux session with: 'tmux attach -t " + SESSION_NAME + "'")
