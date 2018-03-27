FROM python:3.6-slim

ADD https://raw.githubusercontent.com/oioki/blue-docker/master/app.py .
ADD https://raw.githubusercontent.com/oioki/blue-docker/master/data.json .

CMD ["python", "app.py"]
