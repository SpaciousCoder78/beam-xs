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

    '''
    Method for applying UDL (Uniformly Distributed Load) on the beam
    
    Input:  beam              --> Beam object
            loadPerUnitLength --> Load Per Unit Length
           
    Output: udl               --> Applied UDL
    '''
    def applyUDL(beam,loadPerUnitLength):
        #creating a 1d array like beam array and applying udl
        udl = np.full_like(beam,loadPerUnitLength)
        return udl

    #----------------------------------------------------------------------------

    '''
    Method for applying UVL (Uniformly Varying Load) on the beam
    
    Input:  beam       --> Beam object
            startLoad  --> Start Load
            endLoad    --> End Load
    
    Output: uvl        --> Applied UVL
    '''
    def applyUVL(beam,startLoad,endLoad):
        #creating an array with the same length as beam and applying uvl on it
        uvl = np.linspace(startLoad,endLoad,len(beam))
        return uvl

    #-----------------------------------------------------------------------------

    '''
    Method for applying Moment on the beam
    
    Input:  momentPos --> Moment Position
            momentMag --> Moment Magnitude
            beam      --> Beam Object
            
    Output: moments    --> Moment Applied
    '''
    def applyMoment(momentPos, momentMag, beam):
        # Create an array like beam
        moments = np.zeros_like(beam)
        #applying moment magnitude at the index
        moments[momentPos] = momentMag
        return moments

    #----------------------------------------------------------------------------

    '''
    Method for calculation support reaction of a simply supported beam with point load
    
    Input:  loadPos  --> Point Load Position
            loadMag  --> Point Load Magnitude
            beam     --> Beam Object
            pinPos   --> Pin Position
            rollPos  --> Roller Support Position
            
    Output: Ra       --> Reaction at pin support
            Rb       --> Reaction at roller support
    '''

    def calculateReactions(loadPos, loadMag, pinPos, rollPos, beam):
        # Calculating the distance from pin support
        a = abs(loadPos - pinPos)
        # Calcing length of beam
        L = len(beam)
        # Calculate the reactions
        Rb = (loadMag * (L - a)) / L  # Reaction at the roller support
        Ra = (loadMag * a) / L  # Reaction at the pin support
        return Ra, Rb

    #----------------------------------------------------------------------------