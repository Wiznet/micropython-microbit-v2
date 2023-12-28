#!/bin/bash

# Variables
MICROPYTHON_DIR="$(pwd)"
PATCHES_DIR="$MICROPYTHON_DIR/patchs"

echo ">> Update micropython submodule"
cd $MICROPYTHON_DIR
git submodule init
git submodule update

echo ">> Apply micropython patch"
cd $MICROPYTHON_DIR/lib/micropython/
git apply $PATCHES_DIR/0001_microbit_wiznet5k_micropython_lib.patch

echo">> Update wiznet5k submodule"
git submodule init
git submodule update

echo ">> Apply wiznet5k patch"
cd $MICROPYTHON_DIR/lib/micropython/lib/wiznet5k/
git apply $PATCHES_DIR/0002_microbit_wiznet5k_iolibrary.patch

echo "Submodules updated and patches applied."
