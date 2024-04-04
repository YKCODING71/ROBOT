#include "ros/ros.h"                     // ROS Default Header File
#include "ros_serial_service/SrvSerial.h"// SrvSerial Service File Header (Automatically created after build)
#include <serial/serial.h>

serial::Serial ser;

// The below process is performed when there is a service request
// The service request is declared as 'req', and the service response is declared as 'res'
bool calculation(ros_serial_service::SrvSerial::Request &req,
                 ros_serial_service::SrvSerial::Response &res)
{
  if(req.motor == 0){
    ROS_INFO("request: motor stop");
    ser.write("a\n");
  }else if(req.motor == 1){
    ROS_INFO("request: motor start");
    ser.write("b\n");
  }
  // The service name is 'ros_ser_srv' and it will call 'calculation' function upon the service request.
  res.result = 20;

  // Displays 'a' and 'b' values used in the service request and
  // the 'result' value corresponding to the service response
  ROS_INFO("request: motor=%ld", (long int)req.motor);
  //ROS_INFO("sending back response: %ld", (long int)res.result);

  return true;
}



int main(int argc, char **argv)              // Node Main Function
{
  ros::init(argc, argv, "service_server");   // Initializes Node Name
  ros::NodeHandle nh;                        // Node handle declaration

 
  ser.setPort("/dev/ttyUSB0");  // Replace with your serial port name
  ser.setBaudrate(115200);
  serial::Timeout timeout = serial::Timeout::simpleTimeout(1000);
  ser.setTimeout(timeout);
  ser.open();

  if (!ser.isOpen()) {
    ROS_ERROR("Serial port could not be opened.");
    return -1;
  }

  // Declare service server 'ros_serial_srv_server'
  // using the 'SrvSerial' service file in the 'ros_serial_service' package.
  // The service name is 'ros_ser_srv' and it will call 'calculation' function
  // upon the service request.
  ros::ServiceServer ros_service_server = nh.advertiseService("ros_ser_srv", calculation);

  ROS_INFO("ready srv server!");

  ros::spin();    // Wait for the service request

  return 0;
}
