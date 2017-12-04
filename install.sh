#!/bin/bash

DIR=`pwd`

cd dependencies
./install.sh

cd $DIR
cd src
./install.sh

cd $DIR
