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

V = observer._camera_position
scene.point(V, style=f'circle, fill, color=gray, inner sep=0pt, minimum size=2pt')

a, b, c = Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)

n = Vector3(1, 1, 1)

A = a + 0.25 * (n ^ (b - a)) + 0.08 * n
B = b + 0.25 * (n ^ (b - a)) - 0.08 * n

C = b + 0.25 * (n ^ (c - b)) + 0.08 * n
D = c + 0.25 * (n ^ (c - b)) - 0.08 * n

E = c + 0.25 * (n ^ (a - c)) + 0.08 * n
F = a + 0.25 * (n ^ (a - c)) - 0.08 * n

A_B = (A + B) * 0.5
C_D = (C + D) * 0.5
E_F = (E + F) * 0.5

scene.line(Vector3(-0.5, 0, 0), Vector3(2, 0, 0), style='->')
scene.line(Vector3(0, -0.5, 0), Vector3(0, 4, 0), style='->')
scene.line(Vector3(0, 0, -0.5), Vector3(0, 0, 1), style='->')

scene.line(A_B, B, style='very thick, DarkOrchid')
scene.line(C_D, D, style='very thick, OliveGreen')
scene.line(E_F, F, style='very thick, NavyBlue')

scene.line(A, A_B, style='very thick, DarkOrchid')
scene.line(C, C_D, style='very thick, OliveGreen')
scene.line(E, E_F, style='very thick, NavyBlue')

scene.line(observer.project(A_B), observer.project(B), style='very thick, DarkOrchid')
scene.line(observer.project(C_D), observer.project(D), style='very thick, OliveGreen')
scene.line(observer.project(E_F), observer.project(F), style='very thick, NavyBlue')

scene.line(observer.project(A), observer.project(A_B), style='very thick, DarkOrchid')
scene.line(observer.project(C), observer.project(C_D), style='very thick, OliveGreen')
scene.line(observer.project(E), observer.project(E_F), style='very thick, NavyBlue')

scene.polyline(observer.screen.box(-0.5, 0.5, -0.25, 0.45), closed=True, style='black')

scene.render_latex(SphericalCamera(15, deg2rad(10), deg2rad(30), 4))
