from math import sqrt, cos, sin, pi

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def scale(a, s):
        return Vector3(a.x * s, a.y * s, a.z * s)

    __mul__ = __rmul__ = scale

    def __truediv__(a, s):
        return Vector3(a.x / s, a.y / s, a.z / s)

    def add(a, b):
        return Vector3(a.x + b.x, a.y + b.y, a.z + b.z)
    
    __add__ = __radd__ = add

    def sub(a, b):
        return Vector3(a.x - b.x, a.y - b.y, a.z - b.z)

    __sub__ = sub

    def __neg__(self):
        return self.scale(-1)

    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    __and__ = __rand__ = dot

    def cross(a, b):
        ''' Cross product
        | x  y  z  |
        | ax ay az | = (ay * bz - az * by, az * bz - ax * bz, ax * by - ay * bx)
        | bx by bz |
        '''
        return Vector3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

    __xor__ = cross

    @property
    def length(self):
        return sqrt(self & self)

    def normalize(self):
        return self / sqrt(self & self)

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

class Plane:
    def __init__(self, normal, origin, y_hint):
        self._normal = normal
        self._origin = origin
        y_hint_perpendicular = (normal & y_hint) * normal
        y_hint_transverse = y_hint - y_hint_perpendicular
        self._y = y_hint_transverse.normalize()
        self._x = normal ^ self._y

    def project(self, p):
        px = (p & self._x) * self._x
        py = (p & self._y) * self._y
        return px + py

    def uv_to_xyz(self, p):
        u, v = p
        return self._origin + (u * self._x) + (v * self._y)

    def xyz_to_uv(self, p):
        # We assume p is in the plane, i.e. (p - origin) * norm = 0
        P = p - self._origin
        return (P & self._x), (P & self._y)

    @staticmethod
    def from_span(origin, vec1, vec2):
        normal = (vec1 ^ vec2).normalize()
        return Plane(normal, origin, vec1)

    def box(self, left, right, top, bottom):
        v_left = left * self._x
        v_right = right * self._x
        v_top = top * self._y
        v_bottom = bottom * self._y

        top_left = v_top + v_left
        top_right = v_top + v_right
        bottom_right = v_bottom + v_right
        bottom_left = v_bottom + v_left

        return [self._origin + top_left,
                self._origin + top_right,
                self._origin + bottom_right,
                self._origin + bottom_left]

def deg2rad(deg):
    return deg * pi / 180

def spherical(r, theta, phi):
    return Vector3(r * cos(phi) * cos(theta), r * cos(phi) * sin(theta), r * sin(phi))

def spherical_d_phi(r, theta, phi):
    return Vector3(-r * sin(phi) * cos(theta), -r * sin(phi) * sin(theta), r * cos(phi))

O = Vector3(0, 0, 0)
hat_x = Vector3(1, 0, 0)
hat_y = Vector3(0, 1, 0)
hat_z = Vector3(0, 0, 1)

XY = Plane(hat_z, O, hat_y)
YZ = Plane(hat_x, O, hat_z)
XZ = Plane(hat_y, O, hat_x)

def does_intersect(ab, cd, plane):
    a, b = ab
    c, d = cd
    n = plane._normal

    t1 = (c - a) ^ (b - a)
    t2 = (d - a) ^ (b - a)
    t3 = (a - c) ^ (d - c)
    t4 = (b - c) ^ (d - c)

    return (t1 & n) * (t2 & n) < 0 and (t3 & n) * (t4 & n) < 0

def intersect(ab, cd):
    a, b = ab
    c, d = cd

    t1 = ((d - c) ^ (a - c)).length
    t2 = ((a - b) ^ (c - b)).length
    t3 = ((d - c) ^ (b - c)).length
    t4 = ((b - a) ^ (c - a)).length

    t = t1 * t2 / (t3 * t4)
    s = 1 / (1 + t)

    return s * a + (1 - s) * b

def distance_to_segment(v, m, ab):
    a, b = ab
    return ((a - v) ^ (b - a)).length / ((m - v) ^ (b - a)).length

def intersect_ray_with_segment(v, m, ab):
    alpha = distance_to_segment(v, m, ab)
    return v + alpha * (m - v)
