FROM ubuntu:latest
RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install flask pandas numpy apscheduler plotly
COPY . /app
CMD python3 /app/web.py