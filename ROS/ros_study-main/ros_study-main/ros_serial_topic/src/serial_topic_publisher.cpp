#include "ros/ros.h"                            // ROS 기본 헤더 파일
#include "ros_serial_topic/MsgSerial.h"         // MsgSerial 메시지 파일 헤더. 이 헤더 파일은 패키지를 빌드할 때 자동으로 생성됩니다.
#include <serial/serial.h>                      // 시리얼 통신 라이브러리

int main(int argc, char **argv)                 // 노드 메인 함수
{
  ros::init(argc, argv, "serial_topic_publisher");     // 노드 이름을 초기화합니다.
  ros::NodeHandle nh;                           // ROS 시스템과의 통신을 위한 노드 핸들을 선언합니다.

  // 발행자를 선언합니다. 'ros_serial_topic' 패키지의 'MsgSerial' 메시지 파일을 사용하여
  // 'ros_serial_msg' 토픽에 대한 발행자를 생성합니다. 발행자 큐의 크기는 100으로 설정합니다.
  ros::Publisher ros_serial_pub = nh.advertise<ros_serial_topic::MsgSerial>("ros_serial_msg", 100);

  // 루프 주기를 설정합니다. '10'은 10 Hz를 의미하며, 메인 루프는 0.1초 간격으로 반복됩니다.
  ros::Rate loop_rate(10);

  ros_serial_topic::MsgSerial msg;     // 'MsgSerial' 메시지 형식의 'msg' 메시지를 선언합니다.

  serial::Serial ser;     // 시리얼 통신 객체를 선언합니다.
  ser.setPort("/dev/ttyUSB0");  // 시리얼 포트 이름을 지정합니다. 사용 환경에 따라 변경해야 합니다.
  ser.setBaudrate(115200);      // 통신 속도를 설정합니다.
  serial::Timeout timeout = serial::Timeout::simpleTimeout(1000);
  ser.setTimeout(timeout);
  ser.open();                   // 시리얼 포트를 연결합니다.

  if (!ser.isOpen()) {
    ROS_ERROR("시리얼 포트를 열 수 없습니다.");
    return -1;
  }

  while (ros::ok())
  { 
    if (ser.available()>0){
      std::string data_str = ser.readline();   // 시리얼 포트로부터 데이터를 읽어옵니다.

      if(data_str != ""){ // 데이터가 비어있지 않은 경우에만 처리합니다.
        int data = std::stof(data_str);  // 문자열을 정수로 변환합니다.
        msg.temp = (float)data;          // 변환된 값을 메시지에 저장합니다.
        ROS_INFO("send msg = %f", msg.temp);        // 'temp' 메시지를 출력합니다.
        ros_serial_pub.publish(msg);          // 'msg' 메시지를 발행합니다.
      }
      
    }
    loop_rate.sleep();                      // 루프 주기에 따라 잠을 듭니다.

  }

  return 0;
}