#include "ros/ros.h"
#include "ros_topic/Message1.h"

int main(int argc, char, **argv){
    ros::init(argc,atgv, "ros_topic_publisher")
    ros::NodeHandle nh;

    ros::Publisher ros_topic_pub = nh.advertise<ros_topic::Message1>("ros_topic_msg",100);

    ros::Rate loop_rate(10);

    ros_topic::Message1 msg;

    int count = 0;

    while(ros::ok()){
        msg.stamp=ros::Time::now();
        msg.data=count;

        ROS_INFO("send msg = %d", msg.stame.sec);
        ROS_INFO("send msg = %d", msg.stamp.nsec);
        ROS_INFO("send msg = %d", msg.data);

        ros_topic_pub.publish(msg);
        loop_rate.sleep();
        ++count;
    }
    return 0;
}

