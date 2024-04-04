#include "ros/ros.h"                            // ROS Default Header File
#include "ros_center/MsgCenter.h"    // MsgSensor Message File Header. The header file is automatically created when building the package.
#include <time.h>
#include <opencv2/opencv.hpp>

int getMaxAreaContourId(std::vector <std::vector<cv::Point>> contours) {
    double maxArea = 0;
    int maxAreaContourId = -1;
    for (int j = 0; j < contours.size(); j++) {
        double newArea = cv::contourArea(contours.at(j));
        if (newArea > maxArea) {
            maxArea = newArea;
            maxAreaContourId = j;
        } // End if
    } // End for
    return maxAreaContourId;
}

int main(int argc, char **argv)                 // Node Main Function
{
  ros::init(argc, argv, "ros_center_pub");     // Initializes Node Name
  ros::NodeHandle nh;                           // Node handle declaration for communication with ROS system

  // Declare publisher, create publisher 'ros_topic_sensorsim_publisher' using the 'MsgSensor'
  // message file from the 'ros_topic_sensorsim_publisher' package. The topic name is
  // 'ros_topic_sensorsim_mag' and the size of the publisher queue is set to 100.
  ros::Publisher ros_center_pub = nh.advertise<ros_center::MsgCenter>("ros_center_msg", 100);

  // Set the loop period. '10' refers to 10 Hz and the main loop repeats at 0.1 second intervals
  ros::Rate loop_rate(10);

  ros_center::MsgCenter msg;     // Declares message 'msg' in 'MsgSensor' message file format
  
  // random number generate for sensor simulation
  srand(time(NULL));

  cv::VideoCapture cap(0);
  cv::Mat frame;

  std::vector<std::vector<cv::Point>> contour;
  std::vector<cv::Vec4i> hi;
  msg.x = 0;
  msg.y = 0;
  while (ros::ok())
  {

    cap >> frame;
    if(!frame.empty()){
        
        cv::Mat hsv_image;
        cv::cvtColor(frame, hsv_image, cv::COLOR_BGR2HSV);
        // high contrast black and white
        cv::Mat img_mask1;
        cv::Mat img_mask2;
        cv::inRange(hsv_image,
            cv::Scalar(100, 150, 0),
            cv::Scalar(140, 255, 255),
            img_mask1);
        /*cv::inRange(hsv_image,
            cv::Scalar(160, 50, 50),
            cv::Scalar(180, 255, 255),
            img_mask2);*/
        cv::imshow("mask", img_mask1);
        cv::findContours(img_mask1, contour, hi, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);
        int max_id = getMaxAreaContourId(contour);
        //cv::drawContours(frame, contour, max_id, cv::Scalar(0,255,0), 5);
        cv::Moments M = cv::moments(contour[max_id]);
        msg.x = M.m10/M.m00;
        msg.y = M.m01/M.m00;
        cv::circle(frame, cv::Point(msg.x, msg.y), 5, cv::Scalar(0, 255, 0), 5);
        cv::waitKey(1);
    }
    ROS_INFO("send x = %d", msg.x);        // Prints the 'temp' message
    ROS_INFO("send y = %d", msg.y); 
    ros_center_pub.publish(msg);          // Publishes 'msg' message
    cv::imshow("frame", frame);
    loop_rate.sleep();                      // Goes to sleep according to the loop rate defined above.

   }

  return 0;
}
