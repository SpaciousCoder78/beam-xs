from beamxs.beamxs import beamxs as bm



#createBeam() test
beam = bm.createBeam(10)
print(beam)

loads = [
    {'type': 'point', 'position': 2, 'magnitude': 50},
    {'type': 'udl', 'start': 3, 'end': 5, 'magnitude': 20},
    {'type': 'uvl', 'start': 6, 'end': 8, 'start_magnitude': 10, 'end_magnitude': 30}
]
pinPos = 1
rollPos = 9
Ra, Rb = bm.calcReactionsSSB(loads, pinPos, rollPos, beam)
print(Ra)
print(Rb)