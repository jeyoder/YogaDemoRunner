#!/bin/bash

TOP_DIR=`pwd`

cd dependencies
./install.sh

cd $TOP_DIR
cd src
./install.sh

cd $TOP_DIR
