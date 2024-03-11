# Running Clang Static Analysis

## Overview

This project leverages Clang Static Analysis to ensure code correctness and identify potential issues in the MrSnowman project. The `run_clang.sh` script, located in the `clang` directory, automates the process of running Clang analysis and provides insights into the codebase.

## Running Clang Static Analysis

To perform Clang Static Analysis on the project, execute the `run_clang.sh` script in the `clang` directory:

```bash
./run_clang.sh
``` 
This script configures the project for Clang analysis, compiles the code with the necessary flags, runs the static analysis, and provides a summary of the results.

## Clang Static Analysis Process

The `run_clang.sh` script performs the following steps:

- **Modify .pro File:**
  - The script appends the necessary Clang flags (QMAKE_CXX, QMAKE_CC, QMAKE_LINK) to the `MrSnowman.pro` file to enable Clang analysis during compilation.

- **Clean and Rebuild Project:**
  - The project is cleaned, reconfigured using qmake, and then rebuilt using make with Clang analysis flags.

- **Run Clang Static Analysis:**
  - The script uses the `scan-build` tool provided by Clang to perform static analysis.
  - Clang analysis is executed, and the results are displayed in the terminal.

## Interpreting Clang Static Analysis Results

Upon successful completion of the `run_clang.sh` script, a summary in the terminal indicates whether any issues are found.
