#!/bin/bash

find ../04-MrSnowman -name "*.cpp" -o -name "*.h" -exec astyle --options=.astylerc {} \;
