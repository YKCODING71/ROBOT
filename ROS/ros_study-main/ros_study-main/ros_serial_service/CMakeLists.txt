cmake_minimum_required(VERSION 3.0.2)
project(ros_serial_service)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  serial
  std_msgs
)

add_service_files(
   FILES
   SrvSerial.srv
)


generate_messages(
   DEPENDENCIES
   std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(ros_serial_srv_server src/ros_serial_srv_server.cpp)
add_dependencies(ros_serial_srv_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ros_serial_srv_server ${catkin_LIBRARIES})
add_executable(ros_serial_srv_client src/ros_serial_srv_client.cpp)
add_dependencies(ros_serial_srv_client ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ros_serial_srv_client ${catkin_LIBRARIES})
