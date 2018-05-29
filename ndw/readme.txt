
https://github.com/e7dal/bubble3_clients/ndw

bubble client to pull data from http://opendata.ndw.nu/
currently only the .gz files in datex2 (http://www.datex2.eu) format, maybe only the "dutch" version.

currently "possibly" working files:
actuele_statusberichten.xml.gz
brugopeningen.xml.gz
DRIPS.xml.gz
gebeurtenisinfo.xml.gz
incidents.xml.gz
LocatietabelDRIPS.xml.gz
Matrixsignaalinformatie.xml.gz
measurement_current.xml.gz
measurement.xml.gz
Ongevalideerde_snelheden_en_Intensiteiten.xml.gz
srti.xml.gz
trafficspeed.xml.gz
traveltime.xml.gz
wegwerkzaamheden.xml.gz

for usage exampe see config/config.yaml

with the configuration and client inside a bubble, you can fetch and store the data in jsonl format in bubble's memory.
$ bubble pull


todo: 
- make installable like example in:
- https://github.com/e7dal/bubble3/tree/master/demo_client/mydumboclient_site_packages.mydumboclient
- let someone with actual datex2 knowledge check correctness.
