from manim import *
import cv2
import numpy as np

import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

class AI_DRIVEN_COMPRESSION(Scene):
    def construct(self):
        self.AI_intro()
        self.AI()

    def AI_intro(self):
        title = Tex("AI Driven Image Compression", font_size = 80)
        title.color = RED
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(UP*3+LEFT*4).scale(0.5))
        self.wait(1)

        # paragraph
        text = Tex(
            "Besides reducing statistical redundancy by entropy coding and transform techniques, \nthe prediction and quantization techniques are used in here, \nto reduce spatial redundancy and visual redundancy in images."
        ).scale(0.7)
        text.color = YELLOW
        self.play(Write(text))
        self.wait(1)

        path = os.path.join(main_dir, "Data","ai.png")
        img = ImageMobject(path).scale(1.5)
        self.play(FadeOut(text))
        self.play(FadeIn(img))
        self.wait(1)

        text = Tex(
            "CCTV footage will only store the important information such as faces, \nin higher resolution and the rest of the background in lower resolution."
        ).scale(0.7).move_to(DOWN*2.5)
        text.color = YELLOW
        self.play(Write(text))
        self.wait(1)    

        self.play(FadeOut(text), FadeOut(img), FadeOut(title))

    def AI(self):
        text = Tex(
            "This information is derived from the research paper:",
            "'Image and Video Compression with Neural Networks \nA Review'",
            " by Siwei Ma et al."
        ).scale(0.5).move_to(RIGHT*2)
        text.color = YELLOW

        path = os.path.join(main_dir, "Data","paper.png")
        img = ImageMobject(path).move_to(LEFT*4)
        self.play(FadeIn(img), Write(text))
        self.wait(1)

        self.play(FadeOut(img), FadeOut(text))

    def CNN(self):
        pass


        


        
        

    