from latexrenderer import *

hat_z = (0, 0, 1)
hat_r = spherical(1, deg2rad(40), deg2rad(40))

R = 4
midpoint = scale3(R, hat_r)

plane = Plane(hat_r, midpoint, hat_z)

w = h = 2.5
plane_edges = [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]

z_perpendicular = scale3(dot3(hat_z, plane._normal), plane._normal)
z_transverse = sub3(hat_z, z_perpendicular)

with LaTeXRenderer(SphericalCamera(10, deg2rad(-15), deg2rad(30), 4)) as ctx:
    ctx.set_scale(3)

    for a, b in zip(plane_edges, plane_edges[1:] + [plane_edges[0]]):
        A = plane.uv_to_xyz(a)
        B = plane.uv_to_xyz(b)
        ctx.line(A, B)

    ctx.arrow(plane._origin, add3(plane._origin, plane._normal),
            label=r'$\hat n$',
            where='anchor=south west')
    ctx.arrow(plane._origin, add3(plane._origin, hat_z),
            label=r'$\hat z$',
            where='anchor=south west')
    ctx.arrow(plane._origin,
            add3(plane._origin, z_perpendicular),
            label=r'$\vec z_{\bot}$',
            where='anchor=north west',
            style='very thick')
    ctx.arrow(plane._origin,
            add3(plane._origin, z_transverse),
            label=r'$\vec z_{\parallel}$',
            where='anchor=east',
            style='very thick')

    ctx.line(add3(plane._origin, hat_z), add3(plane._origin, z_perpendicular),
            style='dashed, gray')

    ctx.line(add3(plane._origin, hat_z), add3(plane._origin, z_transverse),
            style='dashed, gray')

    draw_right_angle(ctx, midpoint, hat_r, z_transverse, 0.1)
