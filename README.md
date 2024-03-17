# beam-xs


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Python Library for Beam Analysis for Civil Engineering

Developed by Aryan Karamtoth from Information Technology Department at Kakatiya Institute of Technology and Science

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

  Method for applying Point Load on the beam
    
    Input:  loadPos --> Position of Point Load
            loadMag --> Magnitude of Point Load
            beam    --> Beam object
           
    Output: load    --> Applied Load 

  Example:
  ```py
  ptload = bm.applyPointLoad(4,60,beam)
  print(ptload)
  ```
  
- `applyUDL(beam,loadPerUnitLength)`:

  Method for applying UDL (Uniformly Distributed Load) on the beam
    
    Input:  beam              --> Beam object
            loadPerUnitLength --> Load Per Unit Length
           
    Output: udl               --> Applied UDL

  Example:
  
  ```py
  udlarray = bm.applyUDL(beam,20)
  print(udlarray)
  ```

- `applyUVL(beam,startLoad,endLoad)`:

  Method for applying UVL (Uniformly Varying Load) on the beam
    
    Input:  beam       --> Beam object
            startLoad  --> Start Load
            endLoad    --> End Load
    
    Output: uvl        --> Applied UVL

  Example:
  ```py
  uvlarray = bm.applyUVL(beam,20,40)
  print(uvlarray)
  ```
- `applyMoment(momentPos, momentMag, beam)`:

  Method for applying Moment on the beam
    
    Input:  momentPos --> Moment Position
            momentMag --> Moment Magnitude
            beam      --> Beam Object
            
    Output: moments    --> Moment Applied

  Example:
  ```py
  appliedmoment = bm.applyMoment(3,20,beam)
  print(appliedmoment)
  ```
- `reactionsPTLoad(loadPos, loadMag, pinPos, rollPos, beam)`:

  Method for calculation support reaction of a simply supported beam with point load
    
    Input:  loadPos  --> Point Load Position
            loadMag  --> Point Load Magnitude
            beam     --> Beam Object
            pinPos   --> Pin Position
            rollPos  --> Roller Support Position
            
    Output: Ra       --> Reaction at pin support
            Rb       --> Reaction at roller support

  Example:

  ```py
  print(bm.reactionsPTLoad(3,30,1,5,beam))
  ```
  

