FROM python:3
WORKDIR /opt/bubble_test/knmi
RUN apt update
RUN apt install jq
RUN pip install bubble3 feedparser
RUN mkdir mkdir warnings
RUN cd warnings
RUN bubble init
RUN git clone https://github.com/e7dal/bubble3_clients
RUN cp bubble3_clients/knmi_warnings .
RUN cp bubble3_clients/knmi_warnings/config/config.yaml config/
#RUN bubble pull
#RUN bubble export -kvpd -r pulled
#RUN cat remember/pulled.jsonl|jq .


