FROM python:3.12

WORKDIR /app

COPY . /app

RUN apt update -y \
    && pip install uv \
    && uv sync

EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
