import sys
import random

from scene import *
from geometry import *
from observers import *

scene = Scene3D()

random.seed(0)

colors = ['Apricot', 'Blue', 'Brown', 'DarkOrchid', 'ForestGreen', 'Goldenrod',
        'OrangeRed', 'ProcessBlue', 'Lavender', 'Sepia']

scene.polyline(
        [Vector3(-1, -1, -1), Vector3(1, -1, -1), Vector3(1, 1, -1), Vector3(-1, 1, -1)],
        closed=True)
scene.polyline(
        [Vector3(-1, -1, 1), Vector3(1, -1, 1), Vector3(1, 1, 1), Vector3(-1, 1, 1)],
        closed=True)
scene.line(Vector3(-1, -1, -1), Vector3(-1, -1, 1))
scene.line(Vector3(1, -1, -1), Vector3(1, -1, 1))
scene.line(Vector3(1, 1, -1), Vector3(1, 1, 1))
scene.line(Vector3(-1, 1, -1), Vector3(-1, 1, 1))

for color in colors:
    a = Vector3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    b = Vector3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    scene.line(a, b, style=f'very thick, {color}')

for theta in range(0, 360):
    with open(f'many/p{theta}.tex', 'w') as f:
        sys.stdout = f
        scene.render_latex(SphericalCamera(15, deg2rad(theta), deg2rad(30), 4))
