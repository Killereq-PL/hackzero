#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

git fetch
git pull
python3 $SCRIPT_DIR/main.py --fullscreen