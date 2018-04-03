#!/bin/bash

# Exit on failure
set -e

# Install apt dependencies
sudo apt-get install liblapack-dev ncurses-dev libfftw3-dev libboost-all-dev 

# Dependencies dir
DIR="/home/odroid/PP-Quad/dependencies"

# Install GPSTk
cd $DIR
cd GPSTK
if [ ! -d "build" ]; then mkdir build; fi
cd build
cmake -DBUILD_EXT=ON -DCMAKE_BUILD_TYPE=Release ..
make -j 8
sudo make install


# Install OpenBLAS
cd $DIR
cd OpenBLAS
make USE_THREAD=0 # <build target dependent on system>
sudo make install PREFIX=/usr/local


# Install Armadillo
cd $DIR
if [ ! -d "armadillo-8.300.1" ]; then 
    wget -O armadillo.tar.xz http://sourceforge.net/projects/arma/files/armadillo-8.300.1.tar.xz # This may need to be updated
    tar -xvf armadillo.tar.xz
    rm armadillo.tar.xz
fi
cd armadillo-8.300.1
cmake .
make
sudo make install

