# Dockerfile

FROM python:3.8.2

WORKDIR /api

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000 

CMD ["source","flask-api-venv/bin/activate"]

CMD ["python3","api.py"]
