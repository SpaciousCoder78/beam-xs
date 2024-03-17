# beam-xs


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Python Library for Beam Analysis for Civil Engineering

## Supported Features

- Making a beam
- Calculating Support Reactions of a beam
- Applying load on a beam

## Installation

```
pip install beamxs
```
## Getting Started

Import the package

```py
import beamxs as bm
```
Read the documentation and apply the required method for your purpose

## Documentation

### Built-in Methods:
- `createBeam(len)`:
Method for creating a beam

    Input:  len  --> Length of Beam
    Output: beam --> Beam object

Example:
```py
beam = bm.createBeam(10)
print(beam)
```

- `definePin(pinPos,beam)`:
Method for defining the position of pin support
   
    Input:  pinPos      --> Pin Support Position
            beam        --> Beam object
    Output: pinposition --> Pin Position

Example:
```py
pinpos = bm.definePin(2,beam)
print(pinpos)
```

- `defineRoller(rollPos,beam)`:
  Method for defining the position of roller support
    
    Input:  rollPos --> Roller Support Position
            beam    --> Beam object
           
    Output: rollposition --> Roller Position

  Example:
  ```py
  rollpos = bm.defineRoller(4,beam)
  print(rollpos)
  ```
  
- `applyPointLoad(loadPos,loadMag,beam)`:
- sdsd

