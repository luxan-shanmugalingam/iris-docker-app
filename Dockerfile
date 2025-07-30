FROM python:3.10-slim

WORKDIR /usr/ML/app

COPY requirements.txt .
COPY docker_app.py .
COPY rf.pkl .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "docker_app.py"]
