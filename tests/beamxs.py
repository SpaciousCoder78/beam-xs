from beamxs.beamxs import beamxs as bm



#createBeam() test
beam = bm.createBeam(10)
print(beam)

#definePin() test
pinpos = bm.definePin(2,beam)
print(pinpos)

#defineRoller() test
rollpos = bm.defineRoller(4,beam)
print(rollpos)

#applyPointLoad() test
ptload = bm.applyPointLoad(4,60,beam)
print(ptload)

#applyUDL() test
udlarray = bm.applyUDL(beam,20)
print(udlarray)

#applyUVL()  test
uvlarray = bm.applyUVL(beam,20,40)
print(uvlarray)

#applyMoment() test
appliedmoment = bm.applyMoment(3,20,beam)
print(appliedmoment)

#reactionsPTLoad() test
print(bm.reactionsPTLoad(3,30,1,5,beam))