#!/bin/bash

# Navigate to the MrSnowman project directory
cd ../04-MrSnowman/MrSnowman

# Create a backup of the original .pro file
cp MrSnowman.pro MrSnowman.pro.bak

# Modify the .pro file to enable Address Sanitizer
echo "QMAKE_CXXFLAGS += -fsanitize=address" >> MrSnowman.pro
echo "QMAKE_LFLAGS += -fsanitize=address" >> MrSnowman.pro

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

# Run your app with Address Sanitizer
${PWD}/MrSnowman.app/Contents/MacOS/MrSnowman

