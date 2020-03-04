from scene import *
from geometry import *
from observers import *

scene = Scene3D()

hat_r = spherical(1, deg2rad(40), deg2rad(40))

R = 4

midpoint = R * hat_r

plane = Plane(hat_r, midpoint, hat_z)

w = h = 5/2
scene.polyline(plane.box(-0.5, w, -0.5, h), closed=True, style='black')

z_perpendicular = (hat_z & plane._normal) * plane._normal
z_transverse = hat_z - z_perpendicular

u = z_transverse.normalize()
v = plane._normal ^ u

with Scene2D(scene, plane) as sub_scene:
    P = (2, 2)
    Pv = (2, 0)
    Pu = (0, 2)
    sub_scene.line((-1, 0), (3, 0), style='->')
    sub_scene.label((3, 0), r'$V$', style='anchor=east')

    sub_scene.line((0, -1), (0, 3), style='->')
    sub_scene.label((0, 3), r'$U$', style='anchor=south')

    sub_scene.line(P, Pu, style='blue, dashed')
    sub_scene.point(Pu,
            style='circle, fill, color=blue, inner sep=0pt, minimum size=2pt') 
    sub_scene.label(Pu, r'$P_u$', style='anchor=west, color=blue')

    sub_scene.line(P, Pv, style='blue, dashed')
    sub_scene.point(Pv,
            style='circle, fill, color=blue, inner sep=0pt, minimum size=2pt') 
    sub_scene.label(Pv, r'$P_v$', style='anchor=west, color=blue')

    sub_scene.line((0, 0), P, style='->, blue')
    sub_scene.label(P, r'$\vec P$', style='blue, anchor=south west')

    sub_scene.line((0, 0), (0, 1), style='->, very thick')
    sub_scene.label((0, 1), r'$\hat u$', style='anchor=east')

    sub_scene.line((0, 0), (1, 0), style='->, very thick')
    sub_scene.label((1, 0), r'$\hat v$', style='anchor=east')

scene.render_latex(SphericalCamera(10, deg2rad(-15), deg2rad(30), 4), scale=3)
