from manim import *
CONFIG={
        'points':[
            np.array([-4,0,0]),
            np.array([4,1,0])
        ]
    }
dot=np.cross(CONFIG['points'][0],CONFIG['points'][1])
print(dot)