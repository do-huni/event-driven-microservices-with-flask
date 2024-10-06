# Poetry 기반 Flask Dockerfile
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# Poetry 설치
RUN pip install poetry

# 필요한 파일 복사
COPY pyproject.toml poetry.lock /app/

# Poetry를 사용하여 의존성 설치
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Flask 앱 소스 복사
COPY . /app

# PYTHONPATH 설정
ENV PYTHONPATH=/app/src

# Flask 서버 실행
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=3000"]
