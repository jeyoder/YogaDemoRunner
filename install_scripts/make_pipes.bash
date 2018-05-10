#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/common.bash"

cd $DIR/../run

mkfifo pprx_write pprx_read

