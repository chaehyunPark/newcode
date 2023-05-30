FROM python:3
# 작업 디렉토리 설정
WORKDIR /usr/src/app
# 현재 디렉토리의 모든 파일을 작업 디렉토리로 복사
COPY . .
# 현재 작업 디렉토리 내의 main.py 스크립트 실행
CMD [ "python", "./main.py" ]