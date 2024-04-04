#include "ros/ros.h"                          // ROS Default Header File
#include "ros_serial_service/SrvSerial.h"// SrvTutorial Service File Header (Automatically created after build)
#include <cstdlib>                            // Library for using the "atoll" function

int main(int argc, char **argv)               // Node Main Function
{
  ros::init(argc, argv, "service_client");    // Initializes Node Name

  if (argc != 2)  // Input value error handling
  {
    ROS_INFO("cmd : rosrun ros_serial_service ros_seiral_srv_client arg0");
    ROS_INFO("arg0: 0: motor stop, 1: motor start");
    return 1;
  }

  ros::NodeHandle nh;       // Node handle declaration for communication with ROS system

  // Declares service client 'ros_serial_srv_client'
  // using the 'SrvSerial' service file in the 'ros_serial_service' package.
  // The service name is 'ros_ser_srv'
  ros::ServiceClient ros_service_client = nh.serviceClient<ros_serial_service::SrvSerial>("ros_ser_srv");

  // Declares the 'srv' service that uses the 'SrvSerial' service file
  ros_serial_service::SrvSerial srv;

  // Parameters entered when the node is executed as a service request value are stored at 'a' and 'b'
  srv.request.motor = atoll(argv[1]);

  // Request the service. If the request is accepted, display the response value
  if (ros_service_client.call(srv))
  {
    ROS_INFO("send srv, srv.Request.motor: %ld", (long int)srv.request.motor);
    ROS_INFO("receive srv, srv.Response.result: %ld", (long int)srv.response.result);
  }
  else
  {
    ROS_ERROR("Failed to call service ros_tutorial_srv");
    return 1;
  }
  return 0;
}
