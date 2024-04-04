#include <cv_bridge/cv_bridge.h>                    // OpenCV와 ROS의 이미지 변환을 위한 헤더 파일
#include <opencv2/opencv.hpp>                      // OpenCV 라이브러리 헤더 파일
#include <image_transport/image_transport.h>       // ROS 이미지 전송을 위한 헤더 파일
#include <iostream>                                 // 표준 입력/출력을 위한 헤더 파일
#include <vector>                                   // 벡터를 사용하기 위한 헤더 파일
#include <ros/ros.h>                                // ROS 기본 헤더 파일
#include <opencv2/highgui/highgui.hpp>              // OpenCV GUI 관련 헤더 파일
#include <std_msgs/UInt8MultiArray.h>               // ROS 토픽 메시지 형식을 위한 헤더 파일

int main(int argc, char** argv)
{
    ros::init(argc, argv, "opencv_pub");           // 노드 이름 초기화
    
    ros::NodeHandle nh;                             // ROS 노드 핸들 선언
    ros::Publisher pub = nh.advertise<std_msgs::UInt8MultiArray>("camera/image", 1);   // 이미지를 발행할 ROS 토픽 설정

    cv::VideoCapture cap(0);                        // 웹캠을 사용하여 비디오 캡처를 위한 VideoCapture 객체 생성
    cv::Mat frame;                                   // 프레임을 저장할 OpenCV Mat 객체 생성

    while(nh.ok())                                   // ROS 노드가 정상 동작하는 동안 루프 실행
    {
        cap >> frame;                               // 웹캠에서 프레임을 캡처하여 frame 변수에 저장

        if(!frame.empty())                          // 프레임이 비어있지 않을 경우에만 실행
        {
            cv::imshow("frame", frame);             // 캡처한 프레임을 화면에 표시

            // 이미지를 JPEG 형식으로 인코딩 및 디코딩
            std::vector<uchar> encode;              // 인코딩 결과를 저장할 벡터
            std::vector<int> encode_param;          // 인코딩 파라미터 설정

            encode_param.push_back(cv::IMWRITE_JPEG_QUALITY);   // JPEG 품질을 설정하는 파라미터 추가
            encode_param.push_back(20);                         // JPEG 품질을 20으로 설정

            cv::imencode(".jpg", frame, encode, encode_param); // 프레임을 JPEG 형식으로 인코딩하여 encode 벡터에 저장
            cv::Mat decode = cv::imdecode(encode, 1);          // 인코딩된 이미지를 디코딩하여 decode Mat 객체에 저장
            cv::imshow("decode", decode);                      // 디코딩된 이미지를 화면에 표시

            // 인코딩된 이미지를 ROS std_msgs 형식으로 변환
            std_msgs::UInt8MultiArray msgArray;                 // ROS std_msgs 형식의 메시지 객체 생성
            msgArray.data.clear();                              // 메시지 데이터 초기화
            msgArray.data.resize(encode.size());                // 메시지 데이터 크기 설정
            std::copy(encode.begin(), encode.end(), msgArray.data.begin());   // 인코딩된 이미지 데이터를 메시지 데이터에 복사

            // 메시지 발행
            pub.publish(msgArray);                             // 메시지를 토픽에 발행

            cv::waitKey(1);                                     // 1밀리초 동안 키 입력을 대기
          
        }

        ros::spinOnce();                                        // 콜백 함수 실행
    }

    return 0;
}
