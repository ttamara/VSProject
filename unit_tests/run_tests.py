import os
import subprocess

def main():
    # Add additional unit tests
    subprocess.run(["cp", "tests/MyUnitTest1.cpp", "../04-MrSnowman/MrSnowman_tests"]) 
    subprocess.run(["cp", "tests/MyUnitTest2.cpp", "../04-MrSnowman/MrSnowman_tests"]) 

    # Compile MrSnowman
    os.chdir("../04-MrSnowman/MrSnowman")
    subprocess.run(["cp", "MrSnowman.pro", "MrSnowman.pro.bak"])
    subprocess.run(["sh", "-c", 'echo "QMAKE_CXXFLAGS += -fprofile-arcs -ftest-coverage" >> MrSnowman.pro'])
    subprocess.run(["sh", "-c", 'echo "QMAKE_LFLAGS += -fprofile-arcs -ftest-coverage" >> MrSnowman.pro'])
    subprocess.run(["make", "clean"])
    subprocess.run(["qmake"])
    subprocess.run(["make"])
    subprocess.run(["rm", "MrSnowman.pro"])
    subprocess.run(["mv", "MrSnowman.pro.bak", "MrSnowman.pro"])

    # Run MrSnowman_tests
    os.chdir("../MrSnowman_tests")
    subprocess.run(["cp", "MrSnowman_tests.pro", "MrSnowman_tests.pro.bak"]) 
    subprocess.run(["sh", "-c", 'echo "QMAKE_CXXFLAGS += --coverage" >> MrSnowman_tests.pro'])
    subprocess.run(["sh", "-c", 'echo "QMAKE_LFLAGS += --coverage" >> MrSnowman_tests.pro'])
    subprocess.run(["sh", "-c", 'echo "CONFIG -= app_bundle" >> MrSnowman_tests.pro'])
    subprocess.run(["sh", "-c", 'echo "SOURCES += MyUnitTest1.cpp" >> MrSnowman_tests.pro'])
    subprocess.run(["sh", "-c", 'echo "SOURCES += MyUnitTest2.cpp" >> MrSnowman_tests.pro'])
    subprocess.run(["make", "clean"])
    subprocess.run(["qmake"])
    subprocess.run(["make"])
    subprocess.run(["rm", "MrSnowman_tests.pro"])
    subprocess.run(["mv", "MrSnowman_tests.pro.bak", "MrSnowman_tests.pro"])
    subprocess.run(["./MrSnowman_tests"])

    # Generate code coverage report
    subprocess.run(["geninfo", "--output-filename", "coverage.info", "--ignore-errors", "inconsistent,gcov", "."])
    subprocess.run(["genhtml", "coverage.info", "--ignore-errors", "inconsistent,unmapped", "--output-directory", "../../unit_tests/coverage-html"])

    # Remove added unit tests
    subprocess.run(["rm", "MyUnitTest1.cpp"])
    subprocess.run(["rm", "MyUnitTest2.cpp"])

if __name__ == "__main__":
    main()
