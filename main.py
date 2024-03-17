from beamxs.beamxs import beamxs

beam = beamxs.createBeam(10)

# Define the positions of the pin and roller supports
pinPos = beamxs.definePin(0, beam)  # Pin at one end
rollPos = beamxs.defineRoller(9, beam)  # Roller at the other end

# Apply a point load of magnitude 5 at position 4
load = beamxs.applyPointLoad(4, 5, beam)

# Calculate the reactions at the supports
# For a simply supported beam with a single point load, the reaction at the pin support (Ra) and the reaction at the roller support (Rb) can be calculated as:
# Ra = (Rb * a) / L
# Rb = (P * (L - a)) / L
# where P is the point load, a is the distance from the load to the pin support, and L is the length of the beam

P = load[4]  # Point load
a = 4 - pinPos  # Distance from the load to the pin support
L = len(beam)  # Length of the beam

Rb = (P * (L - a)) / L  # Reaction at the roller support
Ra = (Rb * a) / L  # Reaction at the pin support

print("Reaction at the pin support (Ra):", Ra)
print("Reaction at the roller support (Rb):", Rb)