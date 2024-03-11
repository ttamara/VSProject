# Overview

AStyle is a code formatter that helps maintain consistent coding styles across projects. This readme explains how to use AStyle with a provided `.astylerc` configuration file and a script (`run_astyle.sh`) to format C++ code in the `04-MrSnowman` project.

# Formatting Code

To format C++ code in the `04-MrSnowman` project, execute the `run_astyle.sh` script in the `astyle` directory:

```bash
./run_astyle.sh
```

This script uses the `.astylerc` configuration file to format all `.cpp` and `.h` files in the `04-MrSnowman` project.

# Running AStyle Script

The `run_astyle.sh` script is designed to automate the process of formatting C++ code in the `04-MrSnowman` project using AStyle. Below is an explanation of what the script does:

## Script Overview

The purpose of the script is to apply consistent code formatting to all C++ files (`*.cpp` and `*.h`) within the `04-MrSnowman` project directory. It achieves this by utilizing AStyle, a code formatter that reads configuration options from a specified file (`.astylerc` in this case) and applies those rules to the source code files.

## Script Execution Process

1. **Finding C++ Files:**
   - The script uses the `find` command to locate all C++ files (`*.cpp` and `*.h`) within the `04-MrSnowman` project directory.

2. **AStyle Formatting:**
   - For each found C++ file, the script executes the AStyle command with the specified configuration file (`.astylerc`) using the `exec` option of `find`.
   - AStyle reads the formatting rules from `.astylerc` and applies them to each file.

## Interpreting AStyle Results

Upon successful execution of the `run_astyle.sh` script, the terminal will list all processed files, indicating whether they have been modified.
