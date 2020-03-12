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

scene.point(A, style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(B, style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(C, style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')
scene.point(D, style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')

scene.line(Vector3(-0.5, 0, 0), Vector3(2, 0, 0), style='->')
scene.line(Vector3(0, -0.5, 0), Vector3(0, 4, 0), style='->')
scene.line(Vector3(0, 0, -0.5), Vector3(0, 0, 1), style='->')

scene.line(A, B, style='thick, DarkOrchid')
scene.line(C, D, style='thick, OliveGreen')

scene.line(observer.project(A), observer.project(B), style='thick, DarkOrchid')
scene.line(observer.project(C), observer.project(D), style='thick, OliveGreen')

scene.point(observer.project(A), style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(observer.project(B), style=f'circle, fill, color=DarkOrchid, inner sep=0pt, minimum size=2pt')
scene.point(observer.project(C), style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')
scene.point(observer.project(D), style=f'circle, fill, color=OliveGreen, inner sep=0pt, minimum size=2pt')

scene.polyline(observer.screen.box(-0.6, 0.6, -0.2, 0.25), closed=True, style='black')

scene.line(A, V, style='DarkOrchid!30')
scene.line(B, V, style='DarkOrchid!30')
scene.line(C, V, style='OliveGreen!30')
scene.line(D, V, style='OliveGreen!30')

scene.label(A, r'$\vec{A}$', style='DarkOrchid, anchor=east')
scene.label(B, r'$\vec{B}$', style='DarkOrchid, anchor=west')
scene.label(C, r'$\vec{C}$', style='OliveGreen, anchor=north')
scene.label(D, r'$\vec{D}$', style='OliveGreen, anchor=south')

scene.label(observer.project(A), r'$\vec{a}$', style='DarkOrchid, anchor=east')
scene.label(observer.project(B), r'$\vec{b}$', style='DarkOrchid, anchor=west')
scene.label(observer.project(C), r'$\vec{c}$', style='OliveGreen, anchor=north')
scene.label(observer.project(D), r'$\vec{d}$', style='OliveGreen, anchor=south')

scene.render_latex(SphericalCamera(15, deg2rad(10), deg2rad(30), 4), font_scale=0.7)
