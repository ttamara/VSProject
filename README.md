# MrSnowman Project Analysis

## Author Information

- **Name and Surname:** Tamara Savić
- **Index Number:** 1057/2021

## Project Description

MrSnowman is a C++ Qt project that represents a 2D game where you help a snowman on his perilous journey!

- **Project Source Code:** [MrSnowman](https://gitlab.com/matf-bg-ac-rs/course-rs/projects-2021-2022/04-MrSnowman)
- **Analyzed Branch:** master
- **Commit Hash:** f28a6c201c1a70c35364b434ad601bb352846205

## Analysis Tools

Five tools were used for the project analysis:

1. **Address Sanitizer (ASan):**
    - Dynamic analysis
    - Detection of memory issues

2. **Astyle:**
    - Code formatting

3. **Clang Static Analyzer:**
    - Static analysis
    - Detection of potential code issues

4. **Thread Sanitizer (TSan):**
    - Dynamic analysis
    - Detection of thread-related issues

5. **Unit Tests:**
    - Dynamic analysis
    - Detection of errors and code coverage

### Instructions for Reproducing Results

Before running the scripts, initialize the project submodule using the following command:

```bash
git submodule update --init --recursive --checkout
```

To run the analysis, use the respective scripts located in the appropriate directories for each tool:

- **Address Sanitizer:** `./run_asan.sh` (located in the Address Sanitizer directory)
- **Astyle:** `./run_astyle.sh` (located in the Astyle directory)
- **Clang Static Analyzer:** `./run_clang.sh` (located in the Clang Static Analyzer directory)
- **Thread Sanitizer:** `./run_tsan.sh` (located in the Thread Sanitizer directory)
- **Unit Tests:** `./run_tests.py` (located in the Unit Tests directory)

### Conclusions

- **Address Sanitizer:** No detected errors or warnings.
- **Thread Sanitizer:** No detected errors or warnings.
- **Astyle:** Code formatting applied successfully to specific files.
- **Clang Static Analyzer:** No errors or warnings found.
- **Unit Tests:** Code and functionality coverage has been analyzed and is available in the `coverage-html` folder.

### Note

Information on tool usage can be found in the respective README.md files within each tool's directory.
