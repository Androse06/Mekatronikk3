#!/bin/bash

# Navigate to your ROS 2 workspace
source /opt/ros/jazzy/setup.bash
source .venv/bin/activate

# Set the environmentvariable for Oskar's fucked up pc
export PYTHONPATH=$PYTHONPATH:/home/adolf-fick/Desktop/Mekatronikk3/.venv/lib/python3.12/site-packages

# sourcing the install folder
source install/setup.bash

rm -rf estimator_data.csv
rm -rf kontroller_data.csv
# Launch the ROS 2 launch file
ros2 launch ngc_bringup ngc.launch.py
