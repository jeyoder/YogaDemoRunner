#!/bin/bash
# Author: Tucker Haydon

echo "Launching stack in a tmux session. Will take ~30 seconds."
echo "This tmux session uses:"
echo "Modifier: C-a"
echo "Horizontal split: -"
echo "Vertical split: |"

SESSION_NAME="Flight-Stack"
REFNET_NAMESPACE="refnet"
QUAD_NAMESPACE="phoenix"
SNAPDRAGON_USERNAME="root"
SNAPDRAGON_IP="${QUAD_NAMESPACE}-snapdragon"
USE_CAMERA=1


# Create a new tmux session
tmux new -s $SESSION_NAME -d

# Helper function to launch commands in a new window
function LAUNCH_COMMAND_IN_WINDOW() {
    local WINDOW_NAME=$1
    local COMMAND=$2

    tmux new-window -t $SESSION_NAME -n $WINDOW_NAME
    tmux send -t "$SESSION_NAME":"$WINDOW_NAME" "$COMMAND" Enter
}

# Start pprx in a new window
WINDOW_NAME="PPRX"
COMMAND="cd /home/odroid/PP-Quad/run; pprx -f pprx.opt"
LAUNCH_COMMAND_IN_WINDOW $WINDOW_NAME "$COMMAND" 

# Wait for PPRX to launch before launching the publishing node
sleep 5

# Start quad GBX_TO_ROS node
WINDOW_NAME="GBX-ROS"
COMMAND="roslaunch refnetclientros quad.launch quad_namespace:=$QUAD_NAMESPACE refnet_namespace:=$REFNET_NAMESPACE"
LAUNCH_COMMAND_IN_WINDOW $WINDOW_NAME "$COMMAND" 

# Wait for GBX data to be published to ros before starting ppengine
sleep 5

# Start PPEngine
WINDOW_NAME="PP-Engine"
COMMAND="rosrun ppengine ppengine --ref $REFNET_NAMESPACE --rov $QUAD_NAMESPACE --out $QUAD_NAMESPACE --config /home/odroid/PP-Quad/run/A2D.cfg --config /home/odroid/PP-Quad/run/SBRTK.cfg"
LAUNCH_COMMAND_IN_WINDOW $WINDOW_NAME "$COMMAND" 

# Launch GPS Kalman Filter
WINDOW_NAME="GPS-KF"
COMMAND="roslaunch gps_kf gpsQuad.launch quad_namespace:=$QUAD_NAMESPACE"
LAUNCH_COMMAND_IN_WINDOW $WINDOW_NAME "$COMMAND" 

# Launch camera
if [ $USE_CAMERA ]; then        
    WINDOW_NAME="SNAP-CAM"
    COMMAND="ssh -t $SNAPDRAGON_USERNAME@$SNAPDRAGON_IP \"bash -ic 'roslaunch snap_cam main.launch'\""
    LAUNCH_COMMAND_IN_WINDOW $WINDOW_NAME "$COMMAND" 
fi

# Attach tmux
echo "Attach the tmux session with: 'tmux attach -t $SESSION_NAME'"

