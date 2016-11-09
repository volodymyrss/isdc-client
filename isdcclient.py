import requests
import StringIO
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np

isdc_server="isdc.unige.ch"

timeout=300
num_max_retries=10
retry_delay=10


import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def get_with_retries(url,params):
    s = requests.Session()

    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[ 500, 502, 503, 504 ])

    s.mount('http://', HTTPAdapter(max_retries=retries))

    return s.get(url,params=params)

def genlc(target,utc,span):
    return get_with_retries("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl", params={"requeststring": target+" "+utc+" "+span,'submit':"Submit", 'generate':'genlc'}).content

def getscw(intime):
    return get_with_retries("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl?requeststring="+intime,params=dict(generate="scw",submit="Submit")).content[:12]
