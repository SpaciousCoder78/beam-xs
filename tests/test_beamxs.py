from beamxs.beamxs import beamxs as bm

def test_createBeam():
    beam = bm.createBeam(10)
    assert beam is not None

def test_definePin():
    beam = bm.createBeam(10)
    pinpos = bm.definePin(2,beam)
    assert pinpos is not None

def test_defineRoller():
    beam = bm.createBeam(10)
    rollpos = bm.defineRoller(4,beam)
    assert rollpos is not None

def test_applyPointLoad():
    beam = bm.createBeam(10)
    ptload = bm.applyPointLoad(4,60,beam)
    assert ptload is not None

def test_applyUDL():
    beam = bm.createBeam(10)
    udlarray = bm.applyUDL(beam,20)
    assert udlarray is not None

def test_applyUVL():
    beam = bm.createBeam(10)
    uvlarray = bm.applyUVL(beam,20,40)
    assert uvlarray is not None