#!/bin/bash
REFNET_GBX="$1 $2"
QUAD_GBX="$3 $4"
OUTPUT="$5 $6"
A2D_CONFIG="$7 $8"
SB_CONFIG="$9 ${10}"

cmd="rosrun ppengineros ppengineros $REFNET_GBX $QUAD_GBX $OUTPUT $A2D_CONFIG $SB_CONFIG"
$cmd

