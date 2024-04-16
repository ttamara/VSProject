# Running Address Sanitizer (ASan)

## Overview

This project utilizes Address Sanitizer (ASan) to detect memory-related issues and ensure code correctness in the MrSnowman project. The `run_asan.sh` script automates the process of enabling ASan, compiling the code with the necessary flags, and running the application to detect memory errors.

## Enabling Address Sanitizer

To enable Address Sanitizer for the project, execute the `run_asan.sh` script:

```bash 
./run_asan.sh
```

This script modifies the `MrSnowman.pro` file to include ASan flags, cleans the project, reconfigures it using `qmake`, rebuilds the project with ASan enabled, and then runs the application to detect memory errors.

## Address Sanitizer Process

The `run_asan.sh` script performs the following steps:

- **Modify .pro File:**
  - The script appends the necessary ASan flags (`-fsanitize=address`) to the `MrSnowman.pro` file to enable ASan during compilation and linking.

- **Clean and Rebuild Project:**
  - The project is cleaned, reconfigured using `qmake`, and then rebuilt using `make` with ASan flags.

- **Run Application with Address Sanitizer:**
  - The script executes the application with ASan enabled to detect memory-related issues.

## Interpreting Address Sanitizer Results

After running the `run_asan.sh` script, the terminal output will display any memory-related issues detected by Address Sanitizer. An example output indicating a memory error could look like this:

```
==55599==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x00010a70241a ...
```

In this example:

- **heap-buffer-overflow**: Indicates that a buffer overflow occurred, writing beyond the allocated memory block.
  
- **WRITE of size 52**: The program tried to write 52 bytes of data to the buffer, exceeding its allocated size.

- **SUMMARY**: Provides a summary of the ASan error, indicating a heap-buffer-overflow, and aborts the program.

If no issues are found, the application will run normally without any ASan error messages.

## Note

It's important to note that the Qt-related messages displayed in the terminal output, such as window positions and font operations, are unrelated to Address Sanitizer (ASan) and are provided for informational purposes only.
