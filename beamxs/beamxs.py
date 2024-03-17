import numpy as np


class beamxs:
    #method for creating a beam
    @staticmethod
    def createBeam(len):
        beam = np.arange(len)
        return beam

    #method for defining the position of pin support
    def definePin(pinPos,beam):
        pinposition = beam[pinPos]
        return pinposition

    #method for defining the position of roller support
    def defineRoller(rollPos,beam):
        rollposition = beam[rollPos]
        return rollposition

    