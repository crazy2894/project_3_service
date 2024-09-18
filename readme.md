# SNS 사진 분석 댓글 및 피드백 프로젝트

### 🍿[메인 페이지 링크](https://github.com/crazy2894/project_3_git)🍿

### 도커 빌드
```
docker compose up --build
```

## 프론트 백엔드 파일 구조 (도커 구조로 수정 해야 함)
```
├── detectron2
├── models
├── py_model
│   ├── __init__.py
│   ├── faster_rcnn.py              # faster r-cnn 얼굴 검출
│   ├── gpt2.py                     # gpt2 언어모델
│   ├── kogpt2.py                   # kogpt2 언어모델
│   ├── t5_base.py                  # t5 언어 모델 base
│   ├── t5_large.py                 # t5 언어 모델 large
│   ├── yolo_oiv.py                 # Yolo 객체 검출
│   ├── yolo10n_face.py             # Yolo 얼굴 검출
├── test_pics
│   ├── .gitignore
│   ├── app.py                      # streamlit
│   ├── main.py                     # fast api
│   ├── readme.md
│   ├── requirements.txt
│   ├── test.png

```

## 환경 설정

```bash
conda create -n project3_front python=3.11
```

```bash
conda activate project3_front
```

## 라이브러리 설치
- window 환경
    ```
    conda install -r requirements.txt

    # 1. 방법
    git clone https://github.com/facebookresearch/detectron2.git
    python -m pip install -e detectron2 

    # 또는
    # 2. 에러 발생 시
    pip install -r requirements.txt
    git clone https://github.com/facebookresearch/detectron2.git
    cd detectron 
    python -m pip install -e . --use-pep517

    # 3. numpy error 발생시
    conda install numpy=1.24.3
    ```

    ```bash
    # detectron 폴더 안
    pyproject.toml 파일을 setup.py가 있는 경로에 만들고 다음 내용 추가
    [build-system]
    requires = ["setuptools>=64", "wheel", "torch", "torchvision"]
    build-backend = "setuptools.build_meta"
    ```

- linux 환경
    ```bash
    pip install -r requirements.txt

    git clone https://github.com/facebookresearch/detectron2.git
    python -m pip install -e detectron2
    ```

## 실행 하기
- fast api 백엔드
```bash
uvicorn main:app --host 0.0.0.0 --port 1234 --reload
```

- streamlit 프론트 엔드
```bash
streamlit run app.py
```
# 결과 이미지
![front_image](front_image.png)