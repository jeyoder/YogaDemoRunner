#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/common.bash"

cd $DIR/../run

# Pipe pprx output to pprx_write
# Copy pprx_write to pprx.gbx
# Copy pprx_write to pprx_read
# Don't show stdout
< pprx_write tee pprx_read pprx.gbx > /dev/null
