#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "$DIR/common.bash"

CFG_DIR="$DIR/../run"
GSS_DIR="$DIR/../src/gss"
GSS_CFG_DIR="$GSS_DIR/pprx/src/optAndConfigFiles/machineGamesQuads"

# Update GSS
cd $GSS_DIR
git pull origin master
ln -fs $GSS_CFG_DIR/quad_a2d.config $CFG_DIR/A2D.cfg
ln -fs $GSS_CFG_DIR/quad_sbrtk.config $CFG_DIR/SBRTK.cfg
ln -fs $GSS_CFG_DIR/quad_pprx.config $CFG_DIR/pprx.cfg

