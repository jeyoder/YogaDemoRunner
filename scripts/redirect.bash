#!/bin/bash
DIR="/home/odroid/PP-Quad/run"
cd $DIR

# Pipe pprx output to pprx_write
# Copy pprx_write to pprx.gbx
# Copy pprx_write to pprx_read
# Don't show stdout
< pprx_write tee pprx_read pprx.gbx > /dev/null
