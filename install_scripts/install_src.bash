#!/bin/bash

# Exit on failure
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/common.bash"
source "$DIR/ros_env.bash"

cd $DIR/../src

# Export pythonpath or the install gets confused
export PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages/

# Build pprx
if [ ! -d "build" ]; then mkdir build; fi
cd build
#cmake -DSINGLE_BIT=ON ..    [USE THIS LINE IF SINGLE BIT QUANTIZATION IS DESIRED]
cmake -DSINGLE_BIT=OFF ..
sudo make all install

../install_scripts/update_cfg.bash
