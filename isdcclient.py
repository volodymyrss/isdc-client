import requests
import StringIO
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np

isdc_server="isdc.unige.ch"

timeout=300
num_max_retries=10
retry_delay=10


def genlc(target,utc,span):
    return requests.get("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl", params={"requeststring": target+" "+utc+" "+span,'submit':"Submit", 'generate':'genlc'},
            max_retries=num_max_retries, delay_between_retries=retry_delay,timeout=timeout).content

def getscw(intime):
    return requests.get("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl?requeststring="+intime,params=dict(generate="scw",submit="Submit"),
            max_retries=num_max_retries, dely_between_retries=3,timeout=timeout).content[:12]
