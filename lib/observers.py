from geometry import *

class Camera:
    def __init__(self, camera_position, camera_direction, screen_distance, up):
        self._camera_position = camera_position
        self._camera_direction = camera_direction
        self._screen_distance = screen_distance
        self._y = up
        self._x = self._y ^ self._camera_direction

    def project(self, r):
        delta = r - self._camera_position
        alpha = self._screen_distance / (self._camera_direction & delta)
        r_sigma = self._camera_position + alpha * delta
        return r_sigma

    def raster(self, r_sigma):
        return (-r_sigma & self._x, r_sigma & self._y)

    @property
    def screen(self):
        '''Get the screen's plane'''
        screen_origin = self._camera_position + self._screen_distance * self._camera_direction
        return Plane(
                normal=self._camera_direction,
                origin=screen_origin,
                y_hint=self._y
                )

class SphericalCamera(Camera):
    def __init__(self, r, theta, phi, d):
        super(SphericalCamera, self).__init__(spherical(r, theta, phi),
                spherical(-1, theta, phi), d, spherical_d_phi(1, theta, phi))
