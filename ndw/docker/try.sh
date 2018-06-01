apt install jq
pip install bubble3 xmltodict requests

git clone https://github.com/e7dal/bubble3_clients
mkdir ndw_demo
cd ndw_demo
bubble init
cp ../bubble3_clients/ndw/ndw_client .
cp ../bubble3_clients/ndw/config/config.yaml config/
bubble pull
#bubble export -kvpd -r pulled
cat remember/pulled.jsonl|jq .

