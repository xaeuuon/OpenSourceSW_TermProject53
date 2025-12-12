# 얼굴 인식 시스템

## 프로젝트 개요
이 프로젝트는 OpenCV를 이용하여 이미지나 비디오에서 얼굴을 실시간으로 인식하는 시스템입니다. 얼굴 인식 알고리즘을 활용하여 카메라나 이미지 파일에서 얼굴을 감지하고 표시합니다.

## 사용한 패키지
- opencv-python==4.5.3.56
- numpy==1.21.0
- imutils==0.5.4

## 실행 방법
1. 웹캠을 이용한 실시간 얼굴 인식:
   ```bash
   python face_recognition.py
   ```
2. 이미지 파일에서 얼굴 인식:
   ```bash
   python face_recognition.py --image "path_to_image.jpg"
   ```

## 참고자료
- [OpenCV 공식 문서](https://docs.opencv.org/)
