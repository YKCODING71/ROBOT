#include "ros/ros.h"                          // ROS 기본 헤더 파일
#include "ros_serial_topic/MsgSerial.h"       // MsgSerial 메시지 파일 헤더. 이 헤더 파일은 패키지를 빌드할 때 자동으로 생성됩니다.

// 메시지 콜백 함수입니다. 이 함수는 'ros_serial_msg'라는 이름의 토픽 메시지가
// 수신되면 호출됩니다. 입력 메시지로는 'ros_serial_topic' 패키지의 'MsgSerial' 메시지를 받습니다.
void msgCallback(const ros_serial_topic::MsgSerial::ConstPtr& msg)
{
  ROS_INFO("수신된 메시지 = %f", msg->temp);        // 'temp' 메시지를 출력합니다.
}

int main(int argc, char **argv)                         // 노드 메인 함수
{
  ros::init(argc, argv, "serial_topic_subscriber");            // 노드 이름을 초기화합니다.

  ros::NodeHandle nh;                                   // ROS 시스템과의 통신을 위한 노드 핸들을 선언합니다.

  // 구독자를 선언합니다. 'ros_serial_topic' 패키지의 'MsgSerial' 메시지 파일을 사용하여
  // 'ros_serial_msg' 토픽에 대한 구독자를 생성합니다. 구독자 큐의 크기는 100으로 설정합니다.
  ros::Subscriber ros_serial_sub = nh.subscribe("ros_serial_msg", 100, msgCallback);

  // 콜백 함수를 호출하고, 메시지 수신을 기다리며, 메시지를 수신하면 콜백 함수를 실행하는 함수입니다.
  ros::spin();

  return 0;
}