# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/alfred/shared_mac/Mekatronikk3/src/ngc_interfaces

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alfred/shared_mac/Mekatronikk3/src/build/ngc_interfaces

# Utility rule file for ngc_interfaces_uninstall.

# Include any custom commands dependencies for this target.
include CMakeFiles/ngc_interfaces_uninstall.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/ngc_interfaces_uninstall.dir/progress.make

CMakeFiles/ngc_interfaces_uninstall:
	/usr/bin/cmake -P /home/alfred/shared_mac/Mekatronikk3/src/build/ngc_interfaces/ament_cmake_uninstall_target/ament_cmake_uninstall_target.cmake

ngc_interfaces_uninstall: CMakeFiles/ngc_interfaces_uninstall
ngc_interfaces_uninstall: CMakeFiles/ngc_interfaces_uninstall.dir/build.make
.PHONY : ngc_interfaces_uninstall

# Rule to build all files generated by this target.
CMakeFiles/ngc_interfaces_uninstall.dir/build: ngc_interfaces_uninstall
.PHONY : CMakeFiles/ngc_interfaces_uninstall.dir/build

CMakeFiles/ngc_interfaces_uninstall.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ngc_interfaces_uninstall.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ngc_interfaces_uninstall.dir/clean

CMakeFiles/ngc_interfaces_uninstall.dir/depend:
	cd /home/alfred/shared_mac/Mekatronikk3/src/build/ngc_interfaces && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alfred/shared_mac/Mekatronikk3/src/ngc_interfaces /home/alfred/shared_mac/Mekatronikk3/src/ngc_interfaces /home/alfred/shared_mac/Mekatronikk3/src/build/ngc_interfaces /home/alfred/shared_mac/Mekatronikk3/src/build/ngc_interfaces /home/alfred/shared_mac/Mekatronikk3/src/build/ngc_interfaces/CMakeFiles/ngc_interfaces_uninstall.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/ngc_interfaces_uninstall.dir/depend

