#!/bin/bash

# Exit on failure
set -e

TOP_DIR=`pwd`

# Install dependencies
cd dependencies
./install.sh

# Build pprx and ros packages
cd $TOP_DIR
cd src
./install.sh

cd $TOP_DIR
