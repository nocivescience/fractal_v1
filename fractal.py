from manim import *
import itertools as it
class FractalScene(Scene):
    CONFIG={
        'colors':[GREEN,BLUE_A,YELLOW,RED],
        'paths':[
            [
                np.array([-4,0,0]),
                np.array([4,0,0]),
            ],
            [
                np.array([-4,0,0]),
                np.array([0,4,0]),
                np.array([4,0,0]),
            ],
            [
                np.array([-4,0,0]),
                ORIGIN,
                np.array([0,4,0]),
                np.array([4,4,0]),
                np.array([4,0,0]),
            ],
            [
                np.array([-4,0,0]),
                ORIGIN,
                np.array([0,4,0]),
                np.array([4,4,0]),
                np.array([4,0,0]),
            ],
        ]
    }
    def construct(self):
        paths=self.getting_path()
        self.play(Create(paths[0]))
        for path in paths[1:]:
            self.play(Transform(paths[0],path))
        self.wait()
    def getting_path(self):
        paths=VGroup()
        for points in self.CONFIG['paths']:
            path=VMobject()
            path.set_points_as_corners(points)
            paths.add(path)
        return paths