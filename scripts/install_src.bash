#!/bin/bash

# Exit on failure
set -e

DIR="/home/jey369/git/PP-Quad/src/"
cd $DIR

# Export pythonpath or the install gets confused
export PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages/

# Build pprx
if [ ! -d "build" ]; then mkdir build; fi
cd build
cmake -DSINGLE_BIT=ON ..
sudo make all install
