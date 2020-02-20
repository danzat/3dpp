from math import sqrt, cos, sin, pi

def dot3(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return ax * bx + ay * by + az * bz

def cross3(a, b):
    ''' Cross product
    | x  y  z  |
    | ax ay az | = (ay * bz - az * by, az * bz - ax * bz, ax * by - ay * bx)
    | bx by bz |
    '''
    ax, ay, az = a
    bx, by, bz = b
    return (ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx)

def add3(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (ax + bx, ay + by, az + bz)

def sub3(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (ax - bx, ay - by, az - bz)

def scale3(a, v):
    vx, vy, vz = v
    return (a * vx, a * vy, a * vz)

def norm3(v):
    vx, vy, vz = v
    d = sqrt(dot3(v, v))
    return (vx / d, vy / d, vz / d)

def deg2rad(deg):
    return deg * pi / 180

def spherical(r, theta, phi):
    return (r * cos(phi) * cos(theta), r * cos(phi) * sin(theta), r * sin(phi))

def spherical_d_phi(r, theta, phi):
    return (-r * sin(phi) * cos(theta), -r * sin(phi) * sin(theta), r * cos(phi))

class Camera:
    def __init__(self):
        pass

    def project(self, r):
        delta = sub3(r, self._camera_position)
        alpha = self._screen_distance / dot3(self._camera_direction, delta)
        r_sigma = add3(self._camera_position, scale3(alpha, delta))
        return r_sigma

    def raster(self, r_sigma):
        return (-dot3(r_sigma, self._x), dot3(r_sigma, self._y))

    def screen(self, w, h):
        offset = add3(self._camera_position,
                scale3(self._screen_distance, self._camera_direction))

        half_y = scale3(0.5 * h, self._y)
        half_x = scale3(0.5 * w, self._x)
        A = add3(offset, add3(half_x, half_y))
        B = add3(offset, sub3(half_x, half_y))
        C = sub3(offset, add3(half_x, half_y))
        D = sub3(offset, sub3(half_x, half_y))
        return [A, B, C, D]

class SphericalCamera(Camera):
    def __init__(self, r, theta, phi, d):
        super(SphericalCamera, self).__init__()

        self._screen_distance = d
        self._camera_position = spherical(r, theta, phi)
        self._camera_direction = spherical(-1, theta, phi)
        self._y = spherical_d_phi(1, theta, phi)
        self._x = cross3(self._y, self._camera_direction)

class LaTeXRenderer:
    def __init__(self, camera):
        self._camera = camera

    def set_scale(self, scale):
        self._scale = scale

    def project(self, r):
        projected = self._camera.project(r)
        return self._camera.raster(scale3(self._scale, projected))

    def line(self, tail, head, style=None):
        xt, yt = self.project(tail)
        xh, yh = self.project(head)
        style_fmt = ''
        if style:
            style_fmt = f'[{style}]'
        print(f'\draw{style_fmt} ({xt}, {yt}) -- ({xh}, {yh});')

    def arrow(self, tail, head, label=None, where=None, style=None):
        xt, yt = self.project(tail)
        xh, yh = self.project(head)
        if not where:
            where = ''
        if label:
            node = f'node [{where}] {{{label}}}'
        else:
            node = ''
        if style:
            print(f'\draw[->,{style}] ({xt}, {yt}) -- ({xh}, {yh}) {node};')
        else:
            print(f'\draw[->] ({xt}, {yt}) -- ({xh}, {yh}) {node};')

    def point(self, p, label=None, where=None, style=None):
        px, py = self.project(p)
        style_fmt = ''
        if style:
            style_fmt = f'[{style}]'
        print(fr'\node{style_fmt} at ({px}, {py}) {{}};')
        if label:
            if not where:
                where = ''
            else:
                where = f'[{where}]'
            print(fr'\node{where} at ({px}, {py}) {{{label}}};')

    def __enter__(self):
        print(r'\documentclass[border=5pt, convert={density=300,outext=.png}]{standalone}')
        print(r'\usepackage{tikz}')
        print(r'\begin{document}')
        print(r'\begin{tikzpicture}')
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print(r'\end{tikzpicture}')
        print(r'\end{document}')

class Plane:
    def __init__(self, normal, origin, y_hint):
        self._normal = normal
        self._origin = origin
        y_hint_perpendicular = scale3(dot3(normal, y_hint), normal)
        y_hint_transverse = sub3(y_hint, y_hint_perpendicular)
        self._y = norm3(y_hint_transverse)
        self._x = cross3(normal, self._y)

    def uv_to_xyz(self, p):
        u, v = p
        return add3(self._origin, add3(scale3(u, self._x), scale3(v, self._y)))

    def xyz_to_uv(self, p):
        # We assume p is in the plane, i.e. (p - origin) * norm = 0
        P = sub3(p, self._origin)
        return dot3(P, self._x), dot3(P, self._y)

    @staticmethod
    def from_span(origin, vec1, vec2):
        normal = norm3(cross3(vec1, vec2))
        return Plane(normal, origin, vec1)

def draw_right_angle(ctx, origin, vec1, vec2, size):
    p = Plane.from_span(origin, vec1, vec2)
    a = p.uv_to_xyz((size, 0))
    b = p.uv_to_xyz((size, size))
    c = p.uv_to_xyz((0, size))
    ctx.line(a, b)
    ctx.line(b, c)
