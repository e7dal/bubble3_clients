import sys
import os
import json
import xmltodict
import gzip

import requests

from bubble3 import Bubble

payload_key='SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'

def deep_key_content(data={},deep_key=payload_key):
    try:
        curr=data
        for k in deep_key.split('.'):
            curr=curr[k]
        print(curr.keys())
        for k in curr.keys():
            print(k,type(curr[k]))
        return curr
    except Exception as e:
        pass

def read_gzipped_xml_from_url(ndw_url=None,gzip_file=None,deep_key=None):
    resp=requests.get(ndw_url+'/'+gzip_file,stream=True)
    gzip_file_fd=gzip.open(resp.raw)
    gzip_content=gzip_file_fd.read()
    xml_data=xmltodict.parse(gzip_content)

    if deep_key:
        return deep_key_content(xml_data,deep_key=deep_key)
    return xml_data


class BubbleClient(Bubble):
    def __init__(self,cfg={}):
        self.CFG=cfg
        print(cfg)
    def pull(self, amount='all', index=0):
        if amount=='all':
            all=True
            self.say('BC: pulling all')
        else:
            sl=slice(index,index+amount)
            self.say('BC: %d,%d'%(amount,index))
        data=read_gzipped_xml_from_url(self.CFG.NDW_URL,
                                       self.CFG.GZIP_FILE,
                                       self.CFG.PAYLOAD_DEEP_KEYS)
        #print(data.keys)
        ci=0
        for d in data[self.CFG.PAYLOAD_DATA_KEY]:
           if all or ci in sl:
                yield d


if __name__ == '__main__':
    from bubble3.util.cfg import get_config
    BCFG = get_config(Bubble())
    NDW = BCFG.CFG.DEV.SOURCE
    puller = BubbleClient(NDW)
    print(puller)
    pulled=puller.pull()

