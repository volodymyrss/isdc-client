from __future__ import print_function

import isdcclient

def test_create_client():
    isdcclient.ISDCClient()

def test_lc():
    client=isdcclient.ISDCClient()

    lc=client.genlc("ACS","2011-11-11T11:11:11","10")

    assert len(lc)>10


def test_lc_numpy():
    import numpy as np

    client = isdcclient.ISDCClient()

    lc = client.genlc("ACS", "2011-11-11T11:11:11", "10",format="numpy")

    assert lc[0,1] < 0.1
    assert lc[-1, 1] > 19.0

    assert np.mean(lc[:,2])**0.5/1.3<np.std(lc[:, 2])<np.mean(lc[:,2])**0.5*1.3

def test_lc_pandas():
    import numpy as np

    client = isdcclient.ISDCClient()

    lc = client.genlc("ACS", "2011-11-11T11:11:11", "10",format="pandas")

    assert np.array(lc.seconds_relative[0]) < -9
    assert np.array(lc.seconds_relative)[-1] > 9

    assert np.mean(lc.counts)**0.5/1.3<np.std(lc.counts)<np.mean(lc.counts)**0.5*1.3


def test_scw():
    client=isdcclient.ISDCClient()

    scw=client.getscw("2011-11-11T11:11:11")

    assert scw == b"110800450010"
