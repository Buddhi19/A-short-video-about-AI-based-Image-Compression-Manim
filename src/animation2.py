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
        self.AI_HISTORY()
        self.CNN_architecture()

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

    def AI_HISTORY(self):
        Title = Tex("History of AI Driven Image Compression", font_size = 80).scale(0.7)
        Title.color = RED
        self.play(Write(Title))
        self.wait(1)
        self.play(Title.animate.shift(UP*3+LEFT*4).scale(0.5))

        text = Tex(
            "Since the 1980s, image compression techniques utilizing machine learning methods, "
            "particularly neural networks, have emerged."
        ).move_to(DOWN*2.5).scale(0.7)
        text.color = YELLOW
        self.play(Write(text))

        MLP_block = Rectangle(width=2.5, height=1, fill_color=BLUE, fill_opacity=1).move_to(LEFT*5)
        MLP_block_text = Text("Multilayer \nPerceptron", font_size=20).move_to(MLP_block.get_center())
        self.play(FadeIn(MLP_block), Write(MLP_block_text))
        RNN_block = Rectangle(width=2.5, height=1, fill_color=BLUE, fill_opacity=1).move_to(LEFT*2)
        RNN_block_text = Text("Recurrent \nNeural Network", font_size=20).move_to(RNN_block.get_center())
        self.play(FadeIn(RNN_block), Write(RNN_block_text))
        RN_block = Rectangle(width=2.5, height=1, fill_color=BLUE, fill_opacity=1).move_to(RIGHT*5)
        RN_block_text = Text("Random \nNeural Network", font_size=20).move_to(RN_block.get_center())
        self.play(FadeIn(RN_block), Write(RN_block_text))
        CNN_block = Rectangle(width=2.5, height=1, fill_color=BLUE, fill_opacity=1).move_to(RIGHT*2)
        CNN_block_text = Text("Convolutional \nNeural Network", font_size=20).move_to(CNN_block.get_center())
        self.play(FadeIn(CNN_block), Write(CNN_block_text))

        group1 = Group(
            MLP_block, MLP_block_text, RNN_block, RNN_block_text, RN_block, RN_block_text, CNN_block, CNN_block_text,
            text
        )

        self.wait(1)

        GAN_block = Rectangle(width=5, height=2, fill_color=BLUE, fill_opacity=1)
        GAN_block_text = Text("Generative \nAdversarial Network", font_size=20).move_to(GAN_block.get_center())
        group2 = Group(GAN_block, GAN_block_text)

        self.play(Transform(group1, group2))
        
        text = Tex(
            "Recently Image Coding Techniques vastly improved with GANs"
        ).scale(0.7).move_to(DOWN*2.5)
        text.color = YELLOW
        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(Group(*self.mobjects)))


    def CNN_architecture(self):
        Title = Tex("Multi-layer Perceptron based Image Coding", font_size = 80).scale(0.7)
        Title.color = RED
        self.play(Write(Title))
        self.wait(1)
        self.play(Title.animate.shift(UP*3+LEFT*4).scale(0.5))


        input_neurons = VGroup(*[Circle(radius=0.2, color=BLUE,fill_opacity = 0.5).move_to(UP * i + LEFT * 5) for i in range(-2, 3)])
        input_label = Text("Input Layer\n Pixels", font_size=18).next_to(input_neurons, LEFT)

        # Hidden Layers
        compression_neurons = VGroup(*[Circle(radius=0.2, color=GREEN, fill_opacity = 0.5).move_to(UP * i + LEFT * 3) for i in range(-1, 2)])
        hidden_label_1 = Tex("Compression Net (Coder)", font_size=20).next_to(compression_neurons, UP)

        reconstruction_neurons = VGroup(*[Circle(radius=0.2, color=ORANGE, fill_opacity = 0.5).move_to(UP * i + RIGHT * 3) for i in range(-1, 2)])
        hidden_label_2 = Tex("Reconstruction Net (Decoder)", font_size=20).next_to(reconstruction_neurons, UP)

        # Output Layer
        output_neurons = VGroup(*[Circle(radius=0.2, color=RED,fill_opacity = 0.5).move_to(UP * i + RIGHT * 5) for i in range(-2, 3)])
        output_label = Text("Output Layer\n Pixels", font_size=15).next_to(output_neurons, RIGHT)

        # Connections
        input_to_compression = VGroup(*[Line(start, end, stroke_width=2)
                 for start in input_neurons
                 for end in compression_neurons])
        
        quantizer_box = Rectangle(width=1.2, height=1, color=YELLOW,fill_opacity = 0.5).move_to(LEFT * 1.5)
        quantizer_label = Tex("Quantizer", font_size=18).move_to(quantizer_box)

        transmission_box = Rectangle(width=2, height=1, color=PURPLE,fill_opacity = 0.5).move_to(RIGHT * 0.5)
        transmission_label = Tex("Transmission Channel", font_size=18).move_to(transmission_box)

        compression_to_quantizer = VGroup(*[Line(start,quantizer_box.get_left() , stroke_width=2)
                      for start in compression_neurons])
        
        quantizer_to_transmission = VGroup(
            Line(quantizer_box.get_right(), transmission_box.get_left(), stroke_width=2)
        )

        transmission_to_reconstruction = VGroup(
            *[Line(transmission_box.get_right(), start, stroke_width=2)
            for start in reconstruction_neurons]
        )

        reconstruction_to_output = VGroup(*[Line(start, end, stroke_width=2)
                     for start in reconstruction_neurons
                     for end in output_neurons])


        # Adding elements to the scene
        self.play(FadeIn(input_neurons, input_label))
        self.play(Create(input_to_compression))

        self.play(FadeIn(compression_neurons, hidden_label_1))
        self.play(Create(compression_to_quantizer))

        self.play(FadeIn(quantizer_box, quantizer_label))
        
        self.play(FadeIn(quantizer_to_transmission))
        self.play(FadeIn(transmission_box, transmission_label))
        
        self.play(FadeIn(reconstruction_neurons, hidden_label_2))
        self.play(FadeIn(transmission_to_reconstruction))
        
        self.play(FadeIn(output_neurons, output_label))
        self.play(Create(reconstruction_to_output))

        # Highlight flow
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)

    