from geometry import *

class Segment:
    def __init__(self, tail, head, style=None):
        self._tail = tail
        self._head = head
        self._style = style if style else ''

    def project_to(self, observer):
        return Segment(
                observer.project(self._tail),
                observer.project(self._head),
                style=self._style
                )

class Label:
    def __init__(self, position, text, style=None):
        self._position = position
        self._text = text
        self._style = style

    def project_to(self, observer):
        return Label(
                observer.project(self._position),
                self._text,
                style=self._style
                )

class Point:
    def __init__(self, position, style=None):
        self._position = position
        self._style = style

    def project_to(self, observer):
        return Point(
                observer.project(self._position),
                style=self._style
                )

class Scene2D:
    def __init__(self, scene3d, plane):
        self._scene3d = scene3d
        self._plane = plane

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def line(self, tail, head, style=None):
        _tail = self._plane.uv_to_xyz(tail)
        _head = self._plane.uv_to_xyz(head)
        self._scene3d.line(_tail, _head, style)

    def polyline(self, vertices, closed=False, style=None):
        _vertices = [self._plane.uv_to_xyz(v) for v in vertices]
        self._scene3d.polyline(_vertices, closed, style)

    def label(self, position, text, style=None):
        _position = self._plane.uv_to_xyz(position)
        self._scene3d.label(_position, text, style)

    def point(self, p, style=None):
        _p = self._plane.uv_to_xyz(p)
        self._scene3d.point(_p, style)

class Scene3D:
    def __init__(self, segments=None, labels=None, points=None):
        self._segments = segments if segments else []
        self._labels = labels if labels else []
        self._points = points if points else []

    def point(self, p, style=None):
        self._points.append(Point(p, style))

    def line(self, tail, head, style=None):
        self._segments.append(Segment(tail, head, style))

    def label(self, position, text, style=None):
        self._labels.append(Label(position, text, style))

    def polyline(self, vertices, closed=False, style=None):
        segments = [Segment(t, h, style) for t, h in zip(vertices[:-1], vertices[1:])]
        self._segments.extend(segments)
        if closed:
            self._segments.append(Segment(vertices[-1], vertices[0], style))

    def extend_segments(self, other):
        self._segments.extend(other._segments)

    def extend(self, other):
        self._segments.extend(other._segments)
        self._labels.extend(other._labels)
        self._points.extend(other._points)

    def right_angle(self, origin, vec1, vec2, size):
        p = Plane.from_span(origin, vec1, vec2)
        a = p.uv_to_xyz((size, 0))
        b = p.uv_to_xyz((size, size))
        c = p.uv_to_xyz((0, size))
        self.line(a, b)
        self.line(b, c)

    def project_to(self, observer):
        ''' Return a new (3d) scene that's made of the current scene projected
        onto the observer's sceen '''
        segments = []
        labels = []
        points = []
        for segment in self._segments:
            segments.append(segment.project_to(observer))
        for label in self._labels:
            labels.append(label.project_to(observer))
        for point in self._points:
            points.append(point.project_to(observer))
        return Scene3D(segments, labels, points)

    def render_latex(self, observer, scale=4, font_scale=1):
        print(r'\documentclass[border=5pt, convert={density=250,outext=.png}]{standalone}')
        print(r'\usepackage[dvipsnames]{xcolor}')
        print(r'\usepackage{tikz}')
        print(r'\begin{document}')
        print(r'\begin{tikzpicture}[every node/.style={scale={' + str(font_scale) + '}}]')

        for segment in self._segments:
            projected_tail = observer.project(segment._tail)
            projected_head = observer.project(segment._head)

            xt, yt = observer.raster(scale * projected_tail)
            xh, yh = observer.raster(scale * projected_head)

            style_fmt = ''
            if segment._style:
                style_fmt = f'[{segment._style}]'
            print(f'\draw{style_fmt} ({xt}, {yt}) -- ({xh}, {yh});')

        for point in self._points:
            projected_position = observer.project(point._position)
            x, y = observer.raster(scale * projected_position)
            style_fmt = ''
            if point._style:
                style_fmt = f'[{point._style}]'
            print(fr'\node{style_fmt} at ({x}, {y}) {{}};')

        for label in self._labels:
            projected_position = observer.project(label._position)
            x, y = observer.raster(scale * projected_position)
            style_fmt = ''
            if label._style:
                style_fmt = f'[{label._style}]'
            print(fr'\node{style_fmt} at ({x}, {y}) {{{label._text}}};')

        print(r'\end{tikzpicture}')
        print(r'\end{document}')
