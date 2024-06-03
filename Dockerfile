FROM python:3.9
RUN mkdir /app && cd /app
WORKDIR /app
COPY ./ ./
RUN apt-get update --allow-unauthenticated && apt-get install -y python3-pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
