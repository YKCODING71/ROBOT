#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <serial/serial.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "fake_laser_scan_publisher");

  ros::NodeHandle n;
  ros::Publisher scan_pub = n.advertise<sensor_msgs::LaserScan>("fakeScan", 50);

  unsigned int num_readings = 99;
  double laser_frequency = 40;
  double ranges[num_readings];
  double intensities[num_readings];

  serial::Serial ser;
  ser.setPort("/dev/ttyUSB0");  // Replace with your serial port name
  ser.setBaudrate(115200);
  serial::Timeout timeout = serial::Timeout::simpleTimeout(1000);
  ser.setTimeout(timeout);
  ser.open();

  if (!ser.isOpen()) {
    ROS_ERROR("Serial port could not be opened.");
    return -1;
  }

  int count = 0;
  ros::Rate r(1.0);
  int data = 0;
  while(n.ok()){
    //generate some fake data for our laser scan
    
    if(ser.available() >0){
      std::string data_str = ser.readline();
      //if(data_str != ""){ // Sometiems data_str is NULL, then it triggers segment fault 
      //  data = std::stof(data_str);  // Convert string to integer
      //}
      //ROS_INFO("%s\n",data_str.c_str());
      for(unsigned int i = 0; i < num_readings; ++i){
        ranges[i]   = (double)(data_str[i])/10;
        intensities[i] = 100 + count;
        ROS_INFO("%f\n",ranges[i]);
      }
    }
    
    
    ros::Time scan_time = ros::Time::now();

    //populate the LaserScan message
    sensor_msgs::LaserScan scan;
    scan.header.stamp = scan_time;
    scan.header.frame_id = "fake_laser_frame";
    scan.angle_min = -1.57;
    scan.angle_max = 1.57;
    scan.angle_increment = 3.14 / num_readings;
    scan.time_increment = (1 / laser_frequency) / (num_readings);
    scan.range_min = 0.0;
    scan.range_max = 100.0;

    scan.scan_time = (1 / laser_frequency);

    scan.ranges.resize(num_readings);
    scan.intensities.resize(num_readings);
    for(unsigned int i = 0; i < num_readings; ++i){
      scan.ranges[i] = ranges[i];
      scan.intensities[i] = intensities[i];
    }

    scan_pub.publish(scan);
    ++count;
    r.sleep();
  }
}
