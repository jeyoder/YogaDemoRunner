#!/bin/bash
REFNET_GBX="refnet"
QUAD_GBX="phoenix"
A2D="A2D.cfg"
SBRTK="SBRTK.cfg"

rosrun ppengineros ppengineros --ref $REFNET_GBX --rov $QUAD_GBX --out $QUAD_GBX --config $A2D --config $SBRTK
