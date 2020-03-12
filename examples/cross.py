from scene import *
from geometry import *
from observers import *

scene = Scene3D()

scene.line(Vector3(0, -1, 0), Vector3(0, 8, 0), style='->, dashed')
scene.line(Vector3(-2, 0, 0), Vector3(2, 0, 0), style='<->, dashed')
scene.line(Vector3(-2, 2, 0), Vector3(2, 2, 0), style='<->, dashed')
scene.line(Vector3(-2, 4, 0), Vector3(2, 4, 0), style='<->, dashed')
scene.line(Vector3(-2, 6, 0), Vector3(2, 6, 0), style='<->, dashed')

scenarios = [
        (Vector3(0, 0.7, 0.3), Vector3(0, 0, 0), Vector3(0, 1, 0)),
        (Vector3(0, 1.8, 0.5), Vector3(0, 2, 0), Vector3(0, 3, 0)),
        (Vector3(0, 3.7, -0.5), Vector3(0, 4, 0), Vector3(0, 5, 0)),
        (Vector3(0, 6.5, -0.2), Vector3(0, 6, 0), Vector3(0, 7, 0))
    ]

for r, a, b in scenarios:
    scene.line(a, b, style='->, very thick')
    n = 2 * ((r - a) ^ (b - a))
    scene.line(a, r, style='->, very thick, blue')
    scene.line(a, a + n, style='->, very thick, red')
    scene.right_angle(a, b - a, n, 0.2)

with Scene2D(scene, YZ) as scene2d:
    scene2d.polyline([(0.5, -1.5), (-7.5, -1.5), (-7.5, 1.5), (0.5, 1.5)], closed=True)

scene.render_latex(SphericalCamera(15, deg2rad(10), deg2rad(30), 4))
