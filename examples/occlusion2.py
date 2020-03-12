from scene import *
from geometry import *
from observers import *

def pretty_point(scene, pos, color):
    scene.point(pos, style=f'circle, fill, color={color}, inner sep=0pt, minimum size=2pt')
    scene.line(pos, XY.project(pos), style=f'{color}!30')
    scene.line(XY.project(pos), XZ.project(XY.project(pos)), style=f'{color}!30, dotted')
    scene.line(XY.project(pos), YZ.project(XY.project(pos)), style=f'{color}!30, dotted')

scene = Scene3D()

observer = SphericalCamera(5, deg2rad(45), deg2rad(10), 2)

A = [Vector3(1, 0.1, 0.3), Vector3(0.3, 1, 0.4)]
B = [Vector3(0.9, 0.6, -0.1), Vector3(0.1, 0.1, 0.5)]

scene.line(Vector3(-0.5, 0, 0), Vector3(2, 0, 0), style='->')
scene.line(Vector3(0, -0.5, 0), Vector3(0, 2, 0), style='->')
scene.line(Vector3(0, 0, -0.5), Vector3(0, 0, 1), style='->')

scene.line(A[0], A[1], style='very thick, OliveGreen')
scene.line(B[0], B[1], style='very thick, DarkOrchid')

pretty_point(scene, A[0], 'OliveGreen')
pretty_point(scene, A[1], 'OliveGreen')

pretty_point(scene, B[0], 'DarkOrchid')
pretty_point(scene, B[1], 'DarkOrchid')

scene.render_latex(SphericalCamera(15, deg2rad(10), deg2rad(30), 4))
