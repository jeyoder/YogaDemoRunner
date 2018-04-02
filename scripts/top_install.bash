#!/bin/bash

# Exit on failure
set -e

DIR=`pwd`
TOP_DIR="$(pwd)/../"

# Pull all submodules
git submodule update --init --recursive

# Install dependencies
cd $DIR
./install_dependencies.bash

# Build pprx and ros packages
cd $DIR
./install_src.bash

cd $TOP_DIR
