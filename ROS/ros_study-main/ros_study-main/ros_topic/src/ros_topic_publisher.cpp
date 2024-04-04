#include "ros/ros.h"                    // ROS 기본 헤더 파일
#include "ros_topic/Message1.h"         // 메시지 파일 헤더. 이 헤더 파일은 패키지를 빌드할 때 자동으로 생성됩니다.

int main(int argc, char **argv)         // 노드 메인 함수
{
  ros::init(argc, argv, "ros_topic_publisher");   // 노드 이름을 초기화합니다.
  ros::NodeHandle nh;                             // ROS 시스템과의 통신을 위한 노드 핸들을 선언합니다.


//여기서 ros::init(argc, argv, "ros_topic_publisher"); 는 ROS 시스템을 초기화하는 부분으로, 세 개의 인자를 받습니다.
//
//argc: 프로그램에 전달된 명령행 인자(argument)의 개수를 나타냅니다.
//argv: 프로그램에 전달된 실제 명령행 인자들의 배열입니다.
//"ros_topic_publisher": 노드의 이름을 나타냅니다. 이것은 ROS 마스터에 등록되는 노드의 고유한 식별자로 사용됩니다.
//한글로 각각을 표현하면 다음과 같습니다:
//argc: 전달된 명령행 인자의 개수
//argv: 실제 명령행 인자들의 배열
//"ros_topic_publisher": 노드의 이름, ROS 마스터에 등록되는 고유한 식별자

  // 발행자를 선언하고, 'ros_topic' 패키지의 'Message1' 메시지 파일을 사용하여
  // 'ros_topic_msg' 토픽을 생성합니다. 발행자 큐의 크기는 100으로 설정합니다.
  ros::Publisher ros_topic_pub = nh.advertise<ros_topic::Message1>("ros_topic_msg", 100);

  // 루프 주기를 설정합니다. '10'은 10 Hz를 의미하며, 메인 루프는 0.1초 간격으로 반복됩니다.
  ros::Rate loop_rate(10);		//

  ros_topic::Message1 msg;           // 'Message1' 메시지 형식의 'msg' 메시지를 선언합니다.
  int count = 0;                     // 메시지에 사용될 변수입니다.

  while (ros::ok())
  {
    msg.stamp = ros::Time::now();   // 'msg'의 타임스탬프에 현재 시간을 저장합니다.
    msg.data  = count;              // 'msg'의 데이터에 'count' 값을 저장합니다.

    ROS_INFO("send msg = %d", msg.stamp.sec);    // 'stamp.sec' 메시지를 출력합니다.(초) 메시지 발행시간
    ROS_INFO("send msg = %d", msg.stamp.nsec);   // 'stamp.nsec' 메시지를 출력합니다.(나노 단위의 시간)
    ROS_INFO("send msg = %d", msg.data);         // 'data' 메시지를 출력합니다.

    ros_topic_pub.publish(msg);    // 'msg' 메시지를 발행합니다.

    loop_rate.sleep();             // 위에서 설정한 루프 속도에 맞게 잠을 듭니다.(0.1초간격으로 데이터 전송)

    ++count;                       // count 변수를 1씩 증가시킵니다.
  }

  return 0;
}

이 코드는 주어진 토픽("ros_topic_msg")에 메시지를 반복적으로 발행하는 발행자 노드입니다. 
메시지는 "ros_topic/Message1" 형식으로 이루어져 있으며, 메시지에는 현재 시간과 count 변수의 값을 포함하고 있습니다. 코드를 실행하면 루프가 반복되면서 메시지가 발행되며, 발행된 메시지의 내용이 ROS의 로그에 출력됩니다.





