from latexrenderer import *

hat_z = (0, 0, 1)
hat_r = spherical(1, deg2rad(40), deg2rad(40))

R = 4
midpoint = scale3(R, hat_r)

plane = Plane(hat_r, midpoint, hat_z)

w = h = 5/2
plane_edges = [(-0.5, -0.5), (w, -0.5), (w, h), (-0.5, h)]

z_perpendicular = scale3(dot3(hat_z, plane._normal), plane._normal)
z_transverse = sub3(hat_z, z_perpendicular)
u = norm3(z_transverse)

v = cross3(plane._normal, u)

P = plane.uv_to_xyz((2, 2))

with LaTeXRenderer(SphericalCamera(10, deg2rad(-15), deg2rad(30), 4)) as ctx:
    ctx.set_scale(3)

    for a, b in zip(plane_edges, plane_edges[1:] + [plane_edges[0]]):
        A = plane.uv_to_xyz(a)
        B = plane.uv_to_xyz(b)
        ctx.line(A, B)

    ctx.arrow(plane.uv_to_xyz((-1, 0)), plane.uv_to_xyz((3, 0)),
            label=r'$V$',
            where='anchor=east')
            
    ctx.arrow(plane.uv_to_xyz((0, -1)), plane.uv_to_xyz((0, 3)),
            label=r'$U$',
            where='anchor=south')

    ctx.arrow(plane._origin,
            add3(plane._origin, u),
            label=r'$\hat u$',
            where='anchor=east',
            style='very thick')

    ctx.arrow(plane._origin,
            add3(plane._origin, v),
            label=r'$\hat v$',
            where='anchor=east',
            style='very thick')

    ctx.arrow(plane._origin, P,
            label=r'$\vec P$',
            where='anchor=south west',
            style='blue')

    ctx.line(P, add3(plane._origin, scale3(dot3(P, v), v)),
            style='dashed, blue')
    ctx.point(add3(plane._origin, scale3(dot3(P, v), v)),
            label=r'$P_v$', where='anchor=north, color=blue',
            style='circle, fill, color=blue, inner sep=0pt, minimum size=2pt')

    ctx.line(P, add3(plane._origin, scale3(dot3(P, u), u)),
            style='dashed, blue')
    ctx.point(add3(plane._origin, scale3(dot3(P, u), u)),
            label=r'$P_u$', where='anchor=west, color=blue',
            style='circle, fill, color=blue, inner sep=0pt, minimum size=2pt')
