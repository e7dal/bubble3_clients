FROM python:3
WORKDIR /opt/bubble_test/ndw
RUN apt update
RUN apt install jq
RUN pip install bubble3 xmltodict requests
RUN mkdir ndw_demo
RUN cd ndw_demo
RUN bubble init
RUN git clone https://github.com/e7dal/bubble3_clients
RUN cp bubble3_clients/ndw/ndw_client.py .
RUN cp bubble3_clients/ndw/config/config.yaml config/
#RUN bubble pull
#RUN bubble export -kvpd -r pulled
#RUN cat remember/pulled.jsonl|jq .


