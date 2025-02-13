FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY main_scores.py /app/
COPY Scores.txt /app/Scores.txt

EXPOSE 8777

ENV PYTHONUNBUFFERED=1

CMD ["python", "main_scores.py"]
