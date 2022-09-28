from manim import *
class FractalCreation(Scene):
    CONFIG = {
        "fractal_class" : PentagonalFractal,
        "max_order" : 5,
        "transform_kwargs" : {
            "path_arc" : np.pi/6,
            "lag_ratio" : 0.5,
            "run_time" : 2,
        },
        "fractal_kwargs" : {},
    }
    def construct(self):
        fractal = self.CONFIG['fractal_class'](order = 0, **self.fractal_kwargs)
        self.play(FadeIn(fractal))
        for order in range(1, self.max_order+1):
            new_fractal = self.fractal_class(
                order = order,
                **self.CONFIG['fractal_kwargs']
            )
            fractal.align_data(new_fractal)
            self.play(Transform(
                fractal, new_fractal,
                **self.CONFIG['transform_kwargs']
            ))
            self.wait()
        self.wait()
        self.fractal = fractal
