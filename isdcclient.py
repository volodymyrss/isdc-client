import requests
import StringIO
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np

isdc_server="isdc.unige.ch"

timeout=300


def genlc(target,utc,span):
    return requests.get("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl", params={"requeststring": target+" "+utc+" "+span,'submit':"Submit", 'generate':'genlc'},timeout=timeout).content

def getscw(intime):
    return requests.get("http://isdc.unige.ch/~savchenk/spiacs-online/spiacs.pl?requeststring="+intime,params=dict(generate="scw",submit="Submit"),timeout=timeout).content[:12]
