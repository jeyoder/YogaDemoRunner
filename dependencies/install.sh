#!/bin/bash

# Install apt dependencies
sudo apt-get install liblapack-dev install ncurses-dev install libfftw3-dev libboost-all-dev 

# Pull all of the submodules
git submodule update --init --recursive

# Dependencies dir
DIR=`pwd`

# Install GPSTk
cd $DIR
cd GPSTK
mkdir build
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
wget -O armadillo.tar.xz http://sourceforge.net/projects/arma/files/armadillo-8.300.1.tar.xz # This may need to be updated
tar -xvf armadillo.tar.xz
cd armadillo
cmake .
make
sudo make install

