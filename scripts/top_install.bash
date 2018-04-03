#!/bin/bash

# Exit on failure
set -e

TOP_DIR="/home/odroid/PP-Quad"

# Pull all submodules
cd $TOP_DIR
git submodule update --init --recursive

# Install dependencies
cd $TOP_DIR/scripts
./install_dependencies.bash

# Build pprx and ros packages
cd $TOP_DIR/scripts
./install_src.bash

# Add names pipes
cd $TOP_DIR/scripts
./make_pipes.bash
