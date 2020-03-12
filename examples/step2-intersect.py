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

A, B = Vector3(1, 0.1, 0.3), Vector3(0.3, 1, 0.4)
C, D = Vector3(0.9, 0.6, -0.1), Vector3(0.1, 0.1, 0.5)

a = observer.project(A)
b = observer.project(B)
c = observer.project(C)
d = observer.project(D)

scene.point(A, style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(B, style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(C, style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')
scene.point(D, style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')

scene.line(Vector3(-0.5, 0, 0), Vector3(2, 0, 0), style='->')
scene.line(Vector3(0, -0.5, 0), Vector3(0, 4, 0), style='->')
scene.line(Vector3(0, 0, -0.5), Vector3(0, 0, 1), style='->')

scene.line(A, B, style='thick, DarkOrchid')
scene.line(C, D, style='thick, OliveGreen')

scene.line(a, b, style='thick, DarkOrchid')
scene.line(c, d, style='thick, OliveGreen')

scene.point(a, style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(b, style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(c, style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')
scene.point(d, style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')

scene.polyline(observer.screen.box(-0.6, 0.6, -0.2, 0.25), closed=True, style='black')

m = intersect((a, b), (c, d))
scene.point(m, style=f'circle, fill, color=red, inner sep=0pt, minimum size=3pt')
scene.label(m, r'$\vec{m}$', style='red, anchor=west')

scene.render_latex(SphericalCamera(15, deg2rad(10), deg2rad(30), 4), font_scale=0.7)
