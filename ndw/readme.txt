
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

- technical ndw documentation http://www.ndw.nu/documenten/nl/#cat_3



Example bits of configuration for all the gzip files:

GZIP_FILE: actuele_statusberichten.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'situation'

GZIP_FILE: brugopeningen.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'situation'

GZIP_FILE: DRIPS.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'vmsUnit'

GZIP_FILE: gebeurtenisinfo.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'situation'

GZIP_FILE: incidents.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'situation'

GZIP_FILE: LocatietabelDRIPS.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication.vmsUnitTable'
PAYLOAD_DATA_KEY: 'vmsUnitRecord'

GZIP_FILE: Matrixsignaalinformatie.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.ndw:NdwVms.variable_message_sign_events'
PAYLOAD_DATA_KEY: 'event'

GZIP_FILE: measurement_current.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'measurementSiteTable.measurementSiteRecord'

GZIP_FILE: measurement.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'measurementSiteTable.measurementSiteRecord'

GZIP_FILE: Ongevalideerde_snelheden_en_Intensiteiten.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.ndw:NdwMrm.minute_speed_and_flow_events'
PAYLOAD_DATA_KEY: 'event'

GZIP_FILE: srti.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'situation'

GZIP_FILE: trafficspeed.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication.siteMeasurements'
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'siteMeasurements'

GZIP_FILE: traveltime.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'siteMeasurements'
            
GZIP_FILE: wegwerkzaamheden.xml.gz
PAYLOAD_DEEP_KEYS: 'SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'
PAYLOAD_DATA_KEY: 'situation'
