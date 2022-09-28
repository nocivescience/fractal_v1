from manim import *
import itertools as it
import turtle
import matplotlib.pyplot as plt 
from random import randint
class FractalScene(Scene):
    CONFIG={
        'sequences':[
            0,1,5,10,20,100,200,500,100,1500,2000,3000
        ]
    }
    def construct(self):
        DOTS=VGroup()
        for sq in self.CONFIG['sequences']:
            [sequences_x,sequences_y]=self.getting_sequence(sq)
            positions=self.getting_postions(sequences_x,sequences_y)
            dots=self.getting_dots(positions=positions)
            dots.center()
            DOTS.add(dots)
        self.play(Create(DOTS[0]))
        for dots in DOTS[1:]:
            if dots.get_height()>7:
                dots.set_height(7)
            self.play(Transform(DOTS[0],dots))
        self.wait()
    def getting_sequence(self,numbers):
        x = [0]
        y = [0]
        for i in range(numbers): 
            p = randint(1, 100) 

            if p == 1: 
                x.append(0) 
                y.append(0.16*(y[i])) 

            if p >= 2 and p <= 86: 
                x.append(0.85*(x[i]) + 0.04*(y[i])) 
                y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) 

            if p >= 87 and p <= 93: 
                x.append(0.2*(x[i]) - 0.26*(y[i])) 
                y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 

            if p >= 94 and p <= 100: 
                x.append(-0.15*(x[i]) + 0.28*(y[i])) 
                y.append(0.26*(x[i]) + 0.24*(y[i])+0.44)
        return [x,y]
    def getting_postions(self,x,y):
        positions=[]
        for sub_x, sub_y in zip(x,y):
            pos=np.array([sub_x,sub_y,0])
            positions.append(pos)
        return positions
    def getting_dots(self,positions):
        dots=VGroup()
        for pos in positions:
            dot=Dot(radius=0.02,color=BLUE_E).move_to(pos)
            dots.add(dot)
        return dots