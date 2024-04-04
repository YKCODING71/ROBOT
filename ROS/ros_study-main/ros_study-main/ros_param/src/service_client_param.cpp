#include "ros/ros.h"                          // ROS Default Header File
#include "ros_param/SrvTutorial.h"// SrvTutorial Service File Header (Automatically created after build)
#include <cstdlib>                            // Library for using the "atoll" function

int main(int argc, char **argv)               // Node Main Function
{
  ros::init(argc, argv, "service_client");    // Initializes Node Name

  if (argc != 3)  // Input value error handling
  {
    ROS_INFO("cmd : rosrun ros_param service_client_param arg0 arg1");
    ROS_INFO("arg0: double number, arg1: double number");
    return 1;
  }

  ros::NodeHandle nh;       // Node handle declaration for communication with ROS system

  // Declares service client 'service_client_param'
  // using the 'SrvTutorial' service file in the 'ros_param' package.
  // The service name is 'ros_param_srv'
  ros::ServiceClient ros_param_client = nh.serviceClient<ros_param::SrvTutorial>("ros_param_srv");

  // Declares the 'srv' service that uses the 'SrvTutorial' service file
  ros_param::SrvTutorial srv;

  // Parameters entered when the node is executed as a service request value are stored at 'a' and 'b'
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);

  // Request the service. If the request is accepted, display the response value
  if (ros_param_client.call(srv))
  {
    ROS_INFO("send srv, srv.Request.a and b: %ld, %ld", (long int)srv.request.a, (long int)srv.request.b);
    ROS_INFO("receive srv, srv.Response.result: %ld", (long int)srv.response.result);
  }
  else
  {
    ROS_ERROR("Failed to call service ros_param_srv");
    return 1;
  }
  return 0;
}
