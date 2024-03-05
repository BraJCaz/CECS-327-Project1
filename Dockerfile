FROM python:latest

COPY . /app
RUN pip install app/requirements.txt

WORKDIR /app 

CMD ["pyhton", "-m" ,"cecs327project1"]
