#!/bin/bash

# Exit on failure
set -e

# Pull in the git repos
git submodule update --init --recursive

# Export pythonpath or the install gets confused
export PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages/

# Build pprx
if [ ! -d "build" ]; then mkdir build; fi
cd build
cmake -DSINGLE_BIT=ON ..
make all
sudo make install

