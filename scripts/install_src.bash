#!/bin/bash

# Exit on failure
set -e

TOP_DIR=`pwd`
DIR="$(pwd)/../src/"

cd $DIR

# Export pythonpath or the install gets confused
export PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages/

# Build pprx
if [ ! -d "build" ]; then mkdir build; fi
cd build
cmake -DSINGLE_BIT=ON ..
sudo make all -j4 install

cd $TOP_DIR
