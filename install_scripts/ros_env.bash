#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export ROS_IP=$(hostname -I)
#export ROS_MASTER_URI=http://192.168.1.102:11311/

source "$DIR/../src/build/devel/setup.bash"
