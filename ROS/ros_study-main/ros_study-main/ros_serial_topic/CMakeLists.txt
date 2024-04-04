cmake_minimum_required(VERSION 3.0.2)
project(ros_serial_topic)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  serial
  std_msgs
)

add_message_files(
   FILES
   MsgSerial.msg
 )

generate_messages(
   DEPENDENCIES
   std_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(serial_topic_publisher src/serial_topic_publisher.cpp)
add_dependencies(serial_topic_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(serial_topic_publisher ${catkin_LIBRARIES})

add_executable(serial_topic_subscriber src/serial_topic_subscriber.cpp)
add_dependencies(serial_topic_subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(serial_topic_subscriber ${catkin_LIBRARIES})

