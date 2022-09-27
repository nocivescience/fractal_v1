from manim import *
class ExampleScene(Scene):
    CONFIG={
        'colors':[GREEN,BLUE_A,YELLOW,RED],
    }
    def construct(self):
        path=MathTex('2\cdot \pi+\sigma^3')
        for element,color in zip(path.family_members_with_points(),self.CONFIG['colors']):
            element.set_color(color)
        self.play(Create(path))
        self.wait()