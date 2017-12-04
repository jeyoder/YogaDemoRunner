#!/bin/bash

# Pull in the git repos
git submodule update --init --recursive

# Build pprx
mkdir build
cd build
cmake -DSINGLE_BIT=ON ..
make all
sudo make install

