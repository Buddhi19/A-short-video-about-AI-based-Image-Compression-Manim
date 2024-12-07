from manim import *
import cv2
import numpy as np

import os
import sys

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(main_dir)

class INTRO_FOR_COMPRESSION(Scene):
    def construct(self):
        # self.intro_hello()
        self.what_is_compression()

    def intro_hello(self):
        # Create a text in the center of the screen
        text = Tex("Hello!",font_size=100)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        
        # write in two lines
        text1 = Tex("Quick Review for AI Driven", font_size=80).move_to(UP*0.5)
        text2 = Tex("Image Compression Techniques", font_size=80).move_to(DOWN*0.5)
        text1.color = YELLOW
        text2.color = YELLOW
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2))

    def what_is_compression(self):
        text1 = Tex("What is Image Compression?", font_size=80)
        text1.color = RED
        self.play(Write(text1))
        self.wait(1)
        self.play(text1.animate.move_to(UP*3 + LEFT*4).scale(0.5))
        self.wait(1)

        # add image
        path = os.path.join(main_dir, "Data","photo.png")
        img = ImageMobject(path).scale(0.5)
        self.play(FadeIn(img))
        self.play(img.animate.scale(0.5))
        text2 = Tex("Consider capturing a raw image with your new camera", font_size=50).move_to(DOWN*2.5)
        text2.color = YELLOW
        self.play(Write(text2))
        self.wait(1)
        self.play(img.animate.move_to(RIGHT*3))

        path = os.path.join(main_dir, "Data","1.jpg")
        img_took = ImageMobject(path).scale(0.2).move_to(LEFT*2)
        self.play(FadeIn(img_took))
        self.wait(1)
        self.play(FadeOut(text2))
        text2 = Tex("The image is too large to store or transmit", font_size=50).move_to(DOWN*2.5)
        text2.color = YELLOW
        self.play(Write(text2))
        self.wait(1)

        path = os.path.join(main_dir, "Data","1_blurred.jpg")
        img_blurred = ImageMobject(path).scale(0.15).move_to(LEFT)
        text3 = Tex("Reducing resolution results in quality loss", font_size=50).move_to(DOWN*2.5)
        text3.color = YELLOW
        self.play(FadeOut(text2))
        self.play(Write(text3), FadeIn(img_blurred))
        self.wait(1)

        Text = Tex("Hence, we compress the original raw image", font_size=50).move_to(DOWN*2.5)
        Text.color = YELLOW
        Text2 = Tex("to reduce the size while maintaining redundancy", font_size=50).move_to(DOWN*3)
        Text2.color = YELLOW
        self.play(FadeOut(text3))
        self.play(FadeOut(img_blurred))
        self.play(Write(Text))
        self.play(Write(Text2))
        self.wait(2)

        self.play(FadeOut(Text2), FadeOut(img), FadeOut(Text))
        self.play(img_took.animate.move_to(ORIGIN))

        text12 = Tex("Consider the RGB channels", font_size=50).move_to(DOWN*2.5)
        text12.color = YELLOW
        self.play(Write(text12))
        self.wait(1)

        path = os.path.join(main_dir, "Data","1_g.png")
        img_g = ImageMobject(path).scale(0.15).move_to(RIGHT*0.5+UP*0.5)
        img_g.z_index = -1
        path = os.path.join(main_dir, "Data","1_b.png")
        img_b = ImageMobject(path).scale(0.15).move_to(RIGHT*1+UP*1)
        img_b.z_index = -2
        path = os.path.join(main_dir, "Data","1_r.png")
        img_r = ImageMobject(path).scale(0.15)


        self.play(Transform(img_took, img_r))
        self.play(FadeIn(img_g), FadeIn(img_b))
        self.wait(1)

        img_width, img_height = img_r.width, img_r.height
        grid_size = 8 # 16x16 grid
        cell_width = img_width / grid_size
        cell_height = img_height / grid_size

        # Top-left corner of the image
        top_left = img_r.get_corner(UL)

        # Create and display rectangles
        rectangles = []
        for i in range(grid_size):
            for j in range(grid_size):
                # Calculate the position of each rectangle
                rect_x = top_left[0] + j * cell_width + cell_width / 2
                rect_y = top_left[1] - i * cell_height - cell_height / 2
                rect_position = np.array([rect_x, rect_y, 0])

                # Create the rectangle
                rect = Rectangle(
                    width=cell_width,
                    height=cell_height,
                    color=BLUE,
                    stroke_width=1,
                ).move_to(rect_position)

                rectangles.append(rect)
                # Draw the entire grid at once 
        Text = Tex("Types of redundancies in images", font_size=50).move_to(DOWN*2.5)
        Text.color = YELLOW
        self.play(Transform(text12, Text))
        self.wait(1)

        ### spatial and spectral mentioned
        text_spectral = Tex("Spectral redundancy exists between RGB channels", font_size=40).move_to(DOWN*2.5)
        text_spectral.color = YELLOW
        self.play(Transform(text12, text_spectral))
        self.wait(1)
        
        self.remove(text12)
        self.remove(text_spectral)
        self.play(*[Create(rect) for rect in rectangles])
        self.wait(1)
        ### draw 4 arrows in 4 directions in 28th rectangle
        self.play(FadeOut(img_b), FadeOut(img_g), FadeOut(img_r))

        arrow1 = Arrow(start=rectangles[27].get_center(), end=rectangles[35].get_center(), color=WHITE)
        arrow2 = Arrow(start=rectangles[27].get_center(), end=rectangles[19].get_center(), color=WHITE)
        arrow3 = Arrow(start=rectangles[27].get_center(), end=rectangles[27].get_center()+LEFT, color=WHITE)
        arrow4 = Arrow(start=rectangles[27].get_center(), end=rectangles[27].get_center()+RIGHT, color=WHITE)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3), Create(arrow4))
        self.wait(2)

        text_spatial = Tex("Spatial Redundancy exists among neighboring pixels ", font_size=40).move_to(DOWN*2.5)
        self.play(Write(text_spatial))

        self.wait(1)
        self.play(FadeOut(text_spatial))
        text_summary = Tex("Considering these facts, we compress the image to retain only meaningful information.", font_size=40).move_to(DOWN*3)
        text_summary.color = YELLOW
        self.play(Write(text_summary))
        self.wait(2)

        # img = cv2.imread(os.path.join(main_dir, "Data","1.jpg"))
        # b,g,r = cv2.split(img)
        # r = cv2.resize(r, (8,8))
        # r_array = []
        # for i in range(8):
        #     for j in range(8):
        #         r_array.append(r[i][j])

        # texts = []
        # for i in range(len(rectangles)):
        #     # print the value of each pixel
        #     text = Tex(str(r_array[i]), color=WHITE).scale(0.5)
        #     text.move_to(rectangles[i].get_center())
        #     texts.append(text)
        # self.play(*[Write(text) for text in texts])
        # self.wait(1)
        
    