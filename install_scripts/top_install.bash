#!/bin/bash


# Exit on failure
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/common.bash"

cd $DIR

TOP_DIR="$DIR/../"

# Pull all submodules
./update_submodules.bash

# Install dependencies
./install_dependencies.bash

# Build pprx and ros packages
./install_src.bash

# Add names pipes
./make_pipes.bash
