# Unitree Go1 IMU Republisher ROS node

The IMU data on the Unitree Go1 dog is not published on a ROS topic, only broadcasted over LCM.
This node simply subscribes to the LCM IMU channel and republishes IMU messages on a ROS `/imu` topic.

# Launch

Git clone this repository in your `src` catkin workspace folder. Build your workspace, source it then:

`roslaunch go1_imu_republisher start.launch`