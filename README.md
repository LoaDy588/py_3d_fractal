# py_3d_fractal
3D Fractal generator with basic OpenGL renderer.

Utilises PyOpenGL library for renderer and PyGame for control.

Fractals are defined in a file, which has specific format.

Seminar project for IB111 @ FI MUNI

## Launch
```
python3 app.py
```

## Fractal definition
File with definition has this format:
```
cube;(0, 6, 8, 12, 16, 18, 22, 24, 26);(6);(0, 6, 8, 12, 16, 18, 22, 24, 26)
```
First is the shape from which the fractal is created.

Second is list of which sub shapes to keep in next iteration.

Third is a list of which sub shapes should be only drawn once and then not iterated over.

Fourth is list of which cubes should be drawn with no gap. This only applies for cubes, but the list must be there for parser to work.

Every list can be empty, but must be always present, if empty, write it like this:
```
cube;(1, 2, 3);();()
```
