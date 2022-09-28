from manim import *
class NpDotScene(Scene):
    CONFIG={
        'points':[
            np.array([-1,0,0]),
            np.array([1,0,0])
        ]
    }
    def construct(self):
        dot_1=Dot().move_to(self.CONFIG['points'][0])
        dot_2=Dot().move_to(self.CONFIG['points'][1])
        dot_3=Dot().move_to(
            midpoint(self.CONFIG['points'][0],self.CONFIG['points'][1])
        )
        self.play(Create(dot_1),Create(dot_2),Create(dot_3))
        self.wait()