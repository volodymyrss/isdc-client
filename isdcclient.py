import requests
import StringIO
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np

isdc_server="isdc.unige.ch"
ISDC_killflag_filename="/home/integral/isdc-offline-flag"

import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.timeout import Timeout



def get_with_retries(url,params):
    if os.path.exists(ISDC_killflag_filename):
        raise Exception("ISDC offline")

    s = requests.Session()

    timeout=Timeout(100,100,100)

    retries = Retry(total=10,
                    read=10,
                    backoff_factor=0.1,
                    status_forcelist=[ 500, 502, 503, 504 ])

    s.mount('http://', HTTPAdapter(max_retries=retries))

    return s.get(url,params=params,timeout=100)#timeout)

def genlc(target,utc,span):
    return get_with_retries("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl", params={"requeststring": target+" "+utc+" "+span,'submit':"Submit", 'generate':'genlc'}).content

def getscw(intime):
    return get_with_retries("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl?requeststring="+intime,params=dict(generate="scw",submit="Submit")).content[:12]
