cmake_minimum_required(VERSION 3.0.2)
project(ros_center)


find_package(catkin REQUIRED COMPONENTS
  ##cv_bridge
  message_generation
  roscpp
  std_msgs
)

find_package(OpenCV REQUIRED)

add_message_files(
   FILES
   MsgCenter.msg
)

generate_messages(
   DEPENDENCIES
   std_msgs
)
catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}

)


add_executable(ros_center_pub src/ros_center_pub.cpp)
add_dependencies(ros_center_pub ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ros_center_pub
   ${catkin_LIBRARIES}  ${OpenCV_LIBRARIES}
)

add_executable(ros_center_sub src/ros_center_sub.cpp)
add_dependencies(ros_center_sub ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ros_center_sub
   ${catkin_LIBRARIES}  ${OpenCV_LIBRARIES}
)