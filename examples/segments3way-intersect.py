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

p0, p1, p2 = Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)

n = Vector3(1, 1, 1)

A = p0 + 0.25 * (n ^ (p1 - p0)) + 0.08 * n
B = p1 + 0.25 * (n ^ (p1 - p0)) - 0.08 * n

C = p1 + 0.25 * (n ^ (p2 - p1)) + 0.08 * n
D = p2 + 0.25 * (n ^ (p2 - p1)) - 0.08 * n

E = p2 + 0.25 * (n ^ (p0 - p2)) + 0.08 * n
F = p0 + 0.25 * (n ^ (p0 - p2)) - 0.08 * n

A_B = (A + B) * 0.5
C_D = (C + D) * 0.5
E_F = (E + F) * 0.5

a = observer.project(A)
b = observer.project(B)
c = observer.project(C)
d = observer.project(D)
e = observer.project(E)
f = observer.project(F)

scene.line(Vector3(-0.5, 0, 0), Vector3(2, 0, 0), style='->')
scene.line(Vector3(0, -0.5, 0), Vector3(0, 4, 0), style='->')
scene.line(Vector3(0, 0, -0.5), Vector3(0, 0, 1), style='->')

scene.line(A_B, B, style='very thick, DarkOrchid')
scene.line(C_D, D, style='very thick, OliveGreen')
scene.line(E_F, F, style='very thick, NavyBlue')

scene.line(A, A_B, style='very thick, DarkOrchid')
scene.line(C, C_D, style='very thick, OliveGreen')
scene.line(E, E_F, style='very thick, NavyBlue')

scene.line(observer.project(A_B), b, style='very thick, DarkOrchid')
scene.line(observer.project(C_D), d, style='very thick, OliveGreen')
scene.line(observer.project(E_F), f, style='very thick, NavyBlue')

scene.line(a, observer.project(A_B), style='very thick, DarkOrchid')
scene.line(c, observer.project(C_D), style='very thick, OliveGreen')
scene.line(e, observer.project(E_F), style='very thick, NavyBlue')

m1 = intersect((a, b), (c, d))
m2 = intersect((a, b), (e, f))

scene.point(m1, style=f'circle, fill, color=red, inner sep=0pt, minimum size=2pt')
scene.point(m2, style=f'circle, fill, color=red, inner sep=0pt, minimum size=2pt')

M1 = intersect_ray_with_segment(V, m1, (A, B))
M2 = intersect_ray_with_segment(V, m2, (A, B))

scene.line(V, V + 1.3 * (M1 - V), style='red!30')
scene.line(V, V + 1.3 * (M2 - V), style='red!30')

scene.point(M1, style=f'circle, fill, color=red, inner sep=0pt, minimum size=2pt')
scene.point(M2, style=f'circle, fill, color=red, inner sep=0pt, minimum size=2pt')

scene.line(A_B + 0.1 * (n ^ (p1 - p0)), A_B - 0.1 * (n ^ (p1 - p0)), style='red, dashed')

scene.polyline(observer.screen.box(-0.5, 0.5, -0.25, 0.45), closed=True, style='black')

scene.render_latex(SphericalCamera(15, deg2rad(10), deg2rad(30), 4))
