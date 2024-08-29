
# ARC: Python & Raspberry Pi Chess Robot

### Introduction


The acronym stands for Automated Chess Robot, and represents the systems ability to move in 3D space with the help of a Chess AI. Users can play with the system virtually through a built-in GUI, while the system recreates the board movements in real life. Robot system's three-dimensional assistance engage graphical user interface (GUI),

### Deployment

To run the program on Raspberry Pi, ensure that Python has already been downloaded and added to path. Install libraries using command:

```bash
  pip install -r requirements.txt
```

Use program through run.py file:

```bash
  python run.py
```

### Robotic Arm

Movement to specific squares on the chess board are defined in controlMovements.json:


```json
  {
    "a1": [190, 185, 17],
    "a2": [186, 175, 13],
    "a3": [183, 166, 9],
    "a4": [181, 158, 7],
    "a5": [179, 150, 6],
    "a6": [175, 142, 7],
    "a7": [167, 134, 6],
    "a8": [165, 126, 11],
    "b1": [193, 182, 16],
    "b2": [192, 174, 9],
    "b3": [191, 164, 9],
    "b4": [188, 156, 7],
    "b5": [187, 146, 7],
    "b6": [184, 139, 7],
    "b7": [181, 129, 11],
    ...
}
```

Values can be changes based on size of board used. For testing, chess board of size 30.5cm x 30.5 cm was used.
