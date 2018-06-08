import sys
import os
import json
import xmltodict
import gzip

import requests

from bubble3 import Bubble

payload_key='SOAP:Envelope.SOAP:Body.d2LogicalModel.payloadPublication'

class BubbleClient(Bubble):
    def __init__(self,cfg={}):
        self.CFG=cfg
        print(cfg)
    def pull(self, amount='all', index=0):
        if amount=='all':
            all_items=True
            self.say('BC: pulling all')
            sl=False
        else:
            all_items=False
            sl=slice(index,index+amount)
            self.say('BC: %d,%d'%(amount,index))
        data=self.read_gzipped_xml_from_url(self.CFG.NDW_URL,
                                            self.CFG.GZIP_FILE,
                                            self.CFG.PAYLOAD_DEEP_KEYS)
        #print(data.keys)
        ci=0
        for d in self.deep_key_content(data,self.CFG.PAYLOAD_DATA_KEY):
           if all_items or ci in sl:
                yield d
                ci+=1

    def deep_key_content(self,data={},deep_key=payload_key):
        try:
            curr=data
            for k in deep_key.split('.'):
                curr=curr[k]
                print(k,type(curr))
                if type(curr)=='dict':
                    print(curr.keys())

            self.say('found:'+deep_key)
            if type(curr)==list:
                self.say('type=listi len=%d'%len(curr))
                return curr
            for k in curr.keys():
                print(k,type(curr[k]))
            return curr
        except Exception as e:
            pass

    def read_gzipped_xml_from_url(self,ndw_url=None,gzip_file=None,deep_key=None):
        resp=requests.get(ndw_url+'/'+gzip_file,stream=True)
        gzip_file_fd=gzip.open(resp.raw)
        gzip_content=gzip_file_fd.read()
        self.say('content',stuff=gzip_content)
        xml_data=xmltodict.parse(gzip_content)

        if deep_key:
            return self.deep_key_content(xml_data,deep_key=deep_key)
        return xml_data

if __name__ == '__main__':
    from bubble3.util.cfg import get_config
    BCFG = get_config(Bubble())
    NDW = BCFG.CFG.DEV.SOURCE
    puller = BubbleClient(NDW)
    print(puller)
    pulled=puller.pull()

