#!/bin/bash
INPUT_GBX="pprx_read"
OUTPUT_TOPIC="phoenix"
A2D="A2D.cfg"
SBRTK="SBRTK.cfg"

rosrun ppengineros ppengineros --in $INPUT_GBX --out $OUTPUT_TOPIC --config $A2D --config $SBRTK --skip 40
