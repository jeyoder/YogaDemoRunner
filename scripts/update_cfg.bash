#!/bin/bash

set -e

CFG_DIR="/home/odroid/PP-Quad/run"
GSS_DIR="/home/odroid/PP-Quad/src/gss"
GSS_CFG_DIR="$GSS_DIR/pprx/src/optAndConfigFiles/machineGamesQuads"

# Update GSS
cd $GSS_DIR
git pull origin master
ln -fs $GSS_CFG_DIR/quad_a2d.config $CFG_DIR/A2D.cfg
ln -fs $GSS_CFG_DIR/quad_sbrtk.config $CFG_DIR/SBRTK.cfg
ln -fs $GSS_CFG_DIR/quad_pprx.config $CFG_DIR/pprx.cfg

