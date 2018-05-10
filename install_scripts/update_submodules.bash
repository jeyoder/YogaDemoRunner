#!/bin/bash

set -e 

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$DIR/.."

git submodule init
git submodule sync --recursive
git submodule update --recursive
