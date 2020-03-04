from scene import *
from geometry import *
from observers import *

scene = Scene3D()

hat_r = spherical(1, deg2rad(40), deg2rad(40))

R = 4

midpoint = R * hat_r

plane = Plane(hat_r, midpoint, hat_z)

w = h = 2.5/2
scene.polyline(plane.box(-w, w, -h, h), closed=True, style='black')

z_perpendicular = (hat_z & plane._normal) * plane._normal
z_transverse = hat_z - z_perpendicular

scene.line(plane._origin, plane._origin + plane._normal, style='->')
scene.label(plane._origin + plane._normal, r'$\hat n$', style='anchor=south west')

scene.line(plane._origin, plane._origin + hat_z, style='->')
scene.label(plane._origin + hat_z, r'$\hat z$', style='anchor=south east')

scene.line(plane._origin, plane._origin + z_perpendicular, style='->, very thick')
scene.label(plane._origin + z_perpendicular, r'$\vec z_{\bot}$', style='anchor=north west')

scene.line(plane._origin, plane._origin + z_transverse, style='->, very thick')
scene.label(plane._origin + z_transverse, r'$\vec z_{\parallel}$', style='anchor=east')

scene.line(plane._origin + hat_z, plane._origin + z_perpendicular,
        style='dashed, gray')

scene.line(plane._origin + hat_z, plane._origin + z_transverse,
        style='dashed, gray')

scene.right_angle(midpoint, hat_r, z_transverse, 0.1)

scene.render_latex(SphericalCamera(10, deg2rad(-15), deg2rad(30), 4), scale=5)
