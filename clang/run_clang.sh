#!/bin/bash

# Navigate to the MrSnowman project directory
cd ../04-MrSnowman/MrSnowman

# Create a backup of the original .pro file
cp MrSnowman.pro MrSnowman.pro.bak

# Modify the .pro file to use clang for compilation
echo "QMAKE_CXX = clang++" >> MrSnowman.pro
echo "QMAKE_CC = clang" >> MrSnowman.pro
echo "QMAKE_LINK = clang++" >> MrSnowman.pro

# Clean the project
make clean

# Generate Makefile using qmake
qmake

# Build the project using make
make

# Remove the modified .pro file
rm MrSnowman.pro

# Restore the original .pro file from the backup
mv MrSnowman.pro.bak MrSnowman.pro

# Run Clang Static Analyzer on the project using scan-build
/opt/homebrew/opt/llvm/bin/scan-build qmake

