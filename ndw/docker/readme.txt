this is an example of how you might run this inside a docker container

example build and run:
docker build -t ndwtry .
docker run -it ndwtry /bin/bash

in the container, pull data and view run:
bubble pull
bubble export -kvpd -r pulled
cat remember/pulled_DEV.jsonl  | jq .

todo:
volumes
scheduling
some small examples from transform and push
