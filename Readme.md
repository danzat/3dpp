# 3dpp - 3D Pre-Processor

This is a set of scripts to help generate [PGF/TikZ](https://pgf-tikz.github.io/) code that compile to 3d scenes with perspective projection.

The idea is that the scenes will be described in Python files which allow them to be programmatic and verbose.

I've included a `Makefile` to help generate PNGs. _E.g._ if the script filename is `script-filename.py` just run:

```sh
make script-filename.png
```

You should have [XeTeX](http://xetex.sourceforge.net/) and [ImageMagick®](https://imagemagick.org/index.php) installed for the `Makefile` to work.
