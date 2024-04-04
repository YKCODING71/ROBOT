cmake_minimum_required(VERSION 3.0.2)
project(ros_urdf)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rviz
  tf
  urdf
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
