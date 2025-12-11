# Text Summarizer Project  
**Open Source Software Term Project - Jeon GyuJin**

본 프로젝트는 한국어 문장을 입력하면 핵심 내용을 자동으로 요약해주는 **텍스트 요약 프로그램**입니다.  
Hugging Face의 한국어 요약 모델 **KoBART(digit82/kobart-summarization)**를 사용하여 안정적인 한국어 요약을 제공합니다.

---

## 사용 기술

| 항목 | 내용 |
|------|------|
| Language | Python 3 |
| Library | Transformers, SentencePiece |
| Model | digit82/kobart-summarization |
| 실행 환경 | CLI(Command Line Interface) |

---

## 프로젝트 구조

Jeon_KyuJin_Project/
│
├── summarizer.py # 요약 기능을 수행하는 메인 프로그램
├── requirements.txt # 필요한 패키지 목록
└── README.md # 프로젝트 설명 문서


---

## 실행 방법

### 1) 필요한 패키지 설치

프로젝트 폴더에서 다음 명령어 실행:
pip install -r requirements.txt


KoBART 모델은 sentencepiece 패키지가 필요합니다.

---

### 2) 프로그램 실행
python summarizer.py

## 실행 예시
<img width="567" height="43" alt="image" src="https://github.com/user-attachments/assets/309a563b-9eaf-4b90-b154-7353d0c23032" />


