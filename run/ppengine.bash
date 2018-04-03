#!/bin/bash
INPUT_GBX="pprx.gbx"
QUAD_GBX="phoenix"
A2D="A2D.cfg"
SBRTK="SBRTK.cfg"

rosrun ppengineros ppengineros --in $INPUT_GBX --out $QUAD_GBX --config $A2D --config $SBRTK
# rosrun --prefix 'gdb -ex run --args' ppengineros ppengineros --in $INPUT_GBX --out $QUAD_GBX --config $A2D --config $SBRTK
