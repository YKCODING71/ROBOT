#include <ros/ros.h>                                    // ROS 기본 헤더 파일
#include <opencv2/opencv.hpp>                          // OpenCV 라이브러리 헤더 파일
#include <image_transport/image_transport.h>           // ROS 이미지 전송을 위한 헤더 파일
#include <opencv2/highgui/highgui.hpp>                  // OpenCV GUI 관련 헤더 파일
#include <cv_bridge/cv_bridge.h>                        // OpenCV와 ROS 이미지 변환을 위한 헤더 파일
#include <vector>                                       // 벡터를 사용하기 위한 헤더 파일
#include <std_msgs/UInt8MultiArray.h>                   // ROS 토픽 메시지 형식을 위한 헤더 파일

// 이미지 콜백 함수
void imageCallback(const std_msgs::UInt8MultiArray::ConstPtr& array)
{
  try
  {
    cv::Mat frame = cv::imdecode(array->data, 1);       // 인코딩된 이미지를 디코딩하여 frame 변수에 저장
    cv::imshow("view", frame);                          // 화면에 이미지를 표시
    cv::waitKey(1);                                     // 1밀리초 동안 키 입력을 대기
  }
  catch (cv_bridge::Exception& e)
  {
    ROS_ERROR("이미지를 디코딩할 수 없습니다");
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "opencv_sub");                  // 노드 이름 초기화

  cv::namedWindow("view");                              // 이미지를 표시할 창 생성
  cv::startWindowThread();                              // GUI 창을 위한 스레드 시작

  ros::NodeHandle nh;                                   // ROS 노드 핸들 선언
  ros::Subscriber sub = nh.subscribe("camera/image", 5, imageCallback);   // 이미지 토픽 구독

  ros::spin();                                          // 노드 실행 및 대기

  cv::destroyWindow("view");                            // 창 닫기
}
