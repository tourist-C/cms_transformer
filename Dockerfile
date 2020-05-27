FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN pip3 -q install pip –upgrade
COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
RUN python3 cms_transformer.py