# 3dpp - 3D Pre-Processor

This is a set of scripts to help generate [PGF/TikZ](https://pgf-tikz.github.io/) code that compile to 3d scenes with perspective projection.

The idea is that the scenes will be described in Python files which allow them to be programmatic and verbose.

I've included a `Makefile` to help generate PNGs. _E.g._ if the script filename is `script-filename.py` just run:

```sh
make script-filename.png
```

You should have [XeTeX](http://xetex.sourceforge.net/) and [ImageMagick®](https://imagemagick.org/index.php) installed for the `Makefile` to work.

## Vector3

The `Vector3` class is a convenience class for doing 3d vector math:

```python
>>> from geometry import Vector3
>>> v = Vector3(1, 1, 1)
>>> v
(1, 1, 1)
>>> u = Vector3(1, -1, 2)
>>> u + v # vector addition
(2, 0, 3)
>>> 3 * v # scalar product
(3, 3, 3)
>>> v & v # dot product
2
>>> u ^ v # cross product
(3, -1, 2)
>>> u & (u ^ v)
0
```

## Observer

An observer represents a camera/eye and screen. It has several parameters:

* Camera/eye position (vector)
* Direction (vector)
* Screen distance
* Up hint (vector)

There's a convenience observer that acts like a camera mounted on the shell of a sphere called `SphericalCamera`:

```Python
from observers import SphericalCamera

observer = SphericalCamera(
        5,              # radius
        deg2rad(45),    # azimuth
        deg2rad(10),    # elevation
        2               # screen distance
)
```

## Scene3D

A scene is a collection of 3d entities: lines, points and labels.
You create a scene by just instantiating it:

```python
from scene import Scene3D

scene = Scene3D()
scene.line(tail, head, style='very thick, green')
scene.line(a, b, style='->') # arrow
scene.point(p, style='circle, fill, inner sep=0pt, minimum size=2pt')
scene.label(p, r'$\hat x$', style='red, anchor=west')
```

To render a scene you must specify the observer on which to render:

```python
scene.render(observer, scale=3)
```

Upon calling `render`, LaTeX code will be emitted to standard output.
