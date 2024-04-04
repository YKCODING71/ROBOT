#include "ros/ros.h"                                    // ROS 기본 헤더 파일
#include "ros_topic_sensorsim/MsgSensor.h"             // MsgSensor 메시지 파일 헤더. 이 헤더 파일은 패키지를 빌드할 때 자동으로 생성됩니다.
#include <time.h>                                       // 시간 관련 헤더 파일

int main(int argc, char **argv)                         // 노드 메인 함수
{
  ros::init(argc, argv, "ros_topic_sensorsim_publisher");   // 노드 이름 초기화
  ros::NodeHandle nh;                                   // ROS 시스템과 통신하기 위한 노드 핸들 선언

  // 발행자 선언, 'ros_topic_sensorsim_publisher'라는 발행자를 'ros_topic_sensorsim_msg' 토픽으로 생성합니다.
  // 메시지 파일은 'ros_topic_sensorsim' 패키지의 'MsgSensor'입니다. 발행자 큐 사이즈는 100입니다.
  ros::Publisher ros_topic_sensorsim_pub = nh.advertise<ros_topic_sensorsim::MsgSensor>("ros_topic_sensorsim_msg", 100);

  // 루프 주기 설정. '10'은 10 Hz를 의미하며, 메인 루프는 0.1초 간격으로 반복됩니다.
  ros::Rate loop_rate(10);

  ros_topic_sensorsim::MsgSensor msg;     // 'MsgSensor' 메시지 파일 형식의 'msg' 메시지 선언
  
  // 센서 시뮬레이션을 위한 난수 생성
  srand(time(NULL));

  while (ros::ok())
  {
    msg.temp  = (float)(rand() % 40);                      // 'msg'의 'temp' 값을 랜덤으로 설정

    ROS_INFO("send msg = %f", msg.temp);        // 'temp' 메시지를 출력

    ros_topic_sensorsim_pub.publish(msg);          // 'msg' 메시지를 발행

    loop_rate.sleep();                      // 위에서 설정한 루프 주기에 따라 대기합니다.

   }

  return 0;
}
