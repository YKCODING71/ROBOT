#include "ros/ros.h"                          // ROS Default Header File
#include "ros_center/MsgCenter.h"  // MsgSensor Message File Header. The header file is automatically created when building the package.

// Message callback function. This is a function is called when a topic
// message named 'ros_topic_sensorsim_msg' is received. As an input message,
// the 'MsgSensor' message of the 'ros_topic_sensorsim' package is received.
void msgCallback(const ros_center::MsgCenter::ConstPtr& msg)
{
  ROS_INFO("recieve x = %d", msg->x);        // Prints the 'data' message
  ROS_INFO("recieve y = %d", msg->y);  
}

int main(int argc, char **argv)                         // Node Main Function
{
  ros::init(argc, argv, "ros_center_sub");            // Initializes Node Name

  ros::NodeHandle nh;                                   // Node handle declaration for communication with ROS system

  // Declares subscriber. Create subscriber 'ros_topic_sensorsim_subscriber' using the 'MsgSensor'
  // message file from the 'ros_topic_sensorsim' package. The topic name is
  // 'ros_topic_sensorsim_msg' and the size of the publisher queue is set to 100.
  ros::Subscriber ros_center_sub = nh.subscribe("ros_center_msg", 100, msgCallback);

  // A function for calling a callback function, waiting for a message to be
  // received, and executing a callback function when it is received.
  ros::spin();

  return 0;
}
