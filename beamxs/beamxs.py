import numpy as np
'''
Beamxs, A python library for beam analysis

Developed by Aryan Karamtoth at Kakatiya Institute of Technology and Science
'''


class beamxs:
    #method for creating a beam
    '''
    Input:  len  --> Length of Beam
    Output: beam --> Beam object
    '''
    @staticmethod
    def createBeam(len):
        beam = np.arange(len)
        return beam
    #-----------------------------------------------------------------------------

    #method for defining the position of pin support
    '''
    Input:  pinPos      --> Pin Support Position
            beam        --> Beam object
    Output: pinposition --> Pin Position
    '''
    def definePin(pinPos,beam):
        #assigning the pin support position to the index
        pinposition = beam[pinPos]
        return pinposition

    #-----------------------------------------------------------------------------

    '''
    Method for defining the position of roller support
    
    Input:  rollPos --> Roller Support Position
            beam    --> Beam object
           
    Output: rollposition --> Roller Position
    '''
    def defineRoller(rollPos,beam):
        #assigning the roller position to the index of beam
        rollposition = beam[rollPos]
        return rollposition

    #-----------------------------------------------------------------------------

    '''
    Method for applying Point Load on the beam
    
    Input:  loadPos --> Position of Point Load
            loadMag --> Magnitude of Point Load
            beam    --> Beam object
           
    Output: load    --> Applied Load 
    '''
    def applyPointLoad(loadPos,loadMag,beam):
        #creating a new beam array to apply the load
        load=np.zeros_like(beam)
        #applying the load
        load[loadPos] = loadMag
        return load

    #-----------------------------------------------------------------------------