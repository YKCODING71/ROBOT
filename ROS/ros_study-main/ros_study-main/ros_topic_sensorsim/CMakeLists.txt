cmake_minimum_required(VERSION 3.0.2)
project(ros_topic_sensorsim)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  std_msgs
)

add_message_files(
   FILES
   MsgSensor.msg
)

generate_messages(
   DEPENDENCIES
   std_msgs
)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(ros_topic_sensorsim_publisher src/ros_topic_sensorsim_publisher.cpp)
add_dependencies(ros_topic_sensorsim_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ros_topic_sensorsim_publisher
   ${catkin_LIBRARIES}
)

add_executable(ros_topic_sensorsim_subscriber src/ros_topic_sensorsim_subscriber.cpp)
add_dependencies(ros_topic_sensorsim_subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ros_topic_sensorsim_subscriber
   ${catkin_LIBRARIES}
)