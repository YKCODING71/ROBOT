cmake_minimum_required(VERSION 3.0.2)
project(laser_scan)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  serial
)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(laser_scan_pub src/laser_scan_pub.cpp)
target_link_libraries(laser_scan_pub ${catkin_LIBRARIES})


add_executable(laser_scan_sub src/laser_scan_sub.cpp)
target_link_libraries(laser_scan_sub ${catkin_LIBRARIES})


add_executable(laser_scan_serial src/laser_scan_serial.cpp)
target_link_libraries(laser_scan_serial ${catkin_LIBRARIES})

