# ros2_AirsSim_UnrealEngine
To control a car using keyboard in airsim simulation and in ROS2
Step 1
Install ROS2(https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html).Here I am using ROS2 foxy which is compatible with airsim.

Step 2
Install Unreal Engine and AirSim (https://microsoft.github.io/AirSim/build_linux/).

Step 3
AirSim-ROS2 integration through airsim_ros_pkgs(https://microsoft.github.io/AirSim/airsim_ros_pkgs/).
cd ros2
colcon build
after the build come succesful you can create the ROS2 packages to write your program code. 
Also you can change the AirSim settings according to your preference. change mode to car to control the car.

Step 4
open a terminal and run unreal Engine in that terminal and start play in Unreal Engine. 
Open other terminals and run 
colcon build 
source install/setup.bash
Open other 3 terminals to run the other nodes in each terminal. 

hooray! Now you can control the car using keyboard keys W,S,A and D
