from manim import *
import numpy as np

class MomentOfInertia(Scene):
    def construct(self):
        
        # Create retctangle that represents beam cross section
        rectangle = Rectangle(color=BLUE, fill_opacity=0.6, height=4, width=2)
        # rectangle.to_corner(DL)
        # rectangle.shift(RIGHT*1.2)
        # rectangle.shift(UP*0.4)        
        rectangle.shift(DOWN)
        self.add(rectangle)
        self.play(Create(rectangle,run_time=2))
        b_text = Text("b").next_to(rectangle, DOWN)
        h_text = Text("h").next_to(rectangle, RIGHT)
        self.add(b_text, h_text)
        self.play(Write(b_text), Write(h_text),run_time=2)
        self.wait(1)  
        
        # Create cross section axes
        arrow = Arrow(start=rectangle.get_center(), end=rectangle.get_center() + DOWN*1.8, buff=0.)
        self.play(Create(arrow))
        left_arrow = Arrow(start=rectangle.get_center(), end=rectangle.get_center() + LEFT*1.8, buff=0.)
        self.play(Create(left_arrow))
        y_text = Text("z").next_to(left_arrow.get_end(), DOWN*0.8)
        z_text = Text("y").next_to(arrow.get_end(), LEFT*0.8 + UP*0.8)
        self.play(Write(y_text), Write(z_text))
        self.wait()

        # Create equation for moment of inertia of beam in relation to b and h
        equation = MathTex("I_z = \\frac{bh^3}{12}")
        equation.to_edge(UP)
        self.play(Write(equation))
        self.wait(2)

        # Rotate the cross section by 90 degrees and update the formula for the moment of inertia
        b_text2 = Text("b").next_to(rectangle, RIGHT)
        h_text2 = Text("h").next_to(rectangle, UP)
        b_text2.shift(RIGHT)
        h_text2.shift(DOWN)
        self.play(
            Rotate(rectangle, angle=PI/2, run_time=2),
            Transform(b_text, b_text2),
            Transform(h_text, h_text2),
            run_time=2
        )
        self.wait()


        self.play(
            Indicate(equation[0][3]),
            Indicate(b_text),
            run_time=2
        )
        self.play(
            Indicate(equation[0][4]),
            Indicate(h_text),
            run_time=2
        )        

        equation_new = MathTex("I_z = \\frac{b^3 h}{12}")
        equation_new.to_edge(UP)
        self.play(Transform(equation, equation_new))
        self.wait(2)

        # Bring rectangle back to initial position and fade out equation
        self.play(
            Rotate(rectangle, angle=-PI/2, run_time=2), run_time=1
        )
        b_text2 = Text("b").next_to(rectangle, DOWN)
        h_text2 = Text("h").next_to(rectangle, RIGHT)
        self.play(
            Transform(b_text, b_text2),
            Transform(h_text, h_text2),         
        )
        self.play(FadeOut(equation))
        self.wait()

        # Fade out b and h
        self.play(FadeOut(b_text), FadeOut(h_text))

        # Rotate rectangle by 30 degrees
        self.play(Rotate(rectangle, angle=PI/6, run_time=2))
        self.wait()

        # Create a second rotated axes by 30 degrees of the original axes
        arrow2 = Arrow(start=rectangle.get_center(), end=rectangle.get_center() + DOWN*2, buff=0.)
        arrow2.rotate(PI/6,about_point=rectangle.get_center())
        self.play(Create(arrow2))
        left_arrow2 = Arrow(start=rectangle.get_center(), end=rectangle.get_center() + LEFT*2., buff=0.)
        left_arrow2.rotate(PI/6,about_point=rectangle.get_center())
        self.play(Create(left_arrow2))
        y_text2 = Text("v").next_to(left_arrow2.get_end(), DOWN*0.8)
        z_text2 = Text("u").next_to(arrow2.get_end(), RIGHT*0.8 + UP*0.8)
        self.play(Write(y_text2), Write(z_text2))
        self.wait()

        # Create an arc between arrow and arrow2 and put a text with theta next to it
        arc = Arc(start_angle=arrow.get_angle(), angle=PI/6, radius=1,arc_center=rectangle.get_center())
        theta_text = MathTex("\\theta").next_to(arc, DOWN*0.8)
        theta_text.shift(RIGHT*0.1)
        self.play(Create(arc), Write(theta_text))
        self.wait(2)

        # Create an equation for the moment of inertia with I = ?
        equation = MathTex("I_z =\\ ?")
        equation.to_edge(UP)        
        self.play(Write(equation), run_time=2)
        self.wait()

        # Indicate the Inertia equation and the angle theta for 3 seconds
        self.play(Indicate(equation), run_time=3)
        self.play(Indicate(theta_text), run_time=3)

        # Transform equation2 to the equation that depends on theta
        equation3 = MathTex("I_z = \\frac{bh^3}{12} \\cos^2(\\theta) + \\frac{b^3h}{12} \\sin^2(\\theta)")
        equation3.to_edge(UP)
        self.play(Transform(equation, equation3))
        self.wait(2)

        # # Put \theta = 0 beneath equation to the left and indicate it
        # theta_0 = MathTex("\\theta = 0").next_to(equation3, DOWN).to_edge(LEFT)
        theta_0 = MathTex("\\theta = 0").next_to(equation3, DOWN)
        self.play(Write(theta_0))
        self.play(Indicate(theta_0),run_time=2)
        self.wait()

        # Substitute theta in equation to 0
        theta_zero = MathTex("0")
        theta_zero2 = MathTex("0")
        theta_zero.move_to(equation[0][14])
        theta_zero2.move_to(equation[0][28])
        self.play(
            Transform(equation[0][14], theta_zero),
            Transform(equation[0][28], theta_zero2)
        )
        self.wait(2)

        # Add = 0 at the end of the equation
        equals_normal = MathTex("=\\frac{bh^3}{12}").next_to(equation, RIGHT)
        self.play(Write(equals_normal))
        self.wait(2)

        # Fade out equals_normal and change back equation to have theta
        self.play(FadeOut(equals_normal))
        self.play(Transform(equation, equation3))

        # Fade out axes u and v and the arc theta
        self.play(
            FadeOut(arrow2),
            FadeOut(left_arrow2),
            FadeOut(y_text2),
            FadeOut(z_text2),
            FadeOut(arc),
            FadeOut(theta_text),
            FadeOut(theta_0)
        )

        # Rotate rectangle by 30 degrees negative
        self.play(Rotate(rectangle, angle=-PI/6, run_time=2))
        self.wait()

        # Send both rectangle and equations to the left
        val = 4.8        
        self.play(
            rectangle.animate.shift(LEFT * val),
            equation.animate.to_edge(LEFT),
            left_arrow.animate.shift(LEFT * val),
            arrow.animate.shift(LEFT * val),
            y_text.animate.shift(LEFT * val),
            z_text.animate.shift(LEFT * val)               
        )
        
        # Create a plot to the right of the rectangle with axes theta and I
        axes = Axes(
            x_range=[0, 2*PI, 0.5*PI],
            y_range=[0, 1.2, 0.1],
            axis_config={"color": BLUE},
            y_axis_config={"numbers_to_include": np.arange(0, 1.2, 0.2)},
            x_length=8.6,  # Change the length of the x-axis
            y_length=5.1   # Change the length of the y-axis
        ).to_edge(RIGHT).to_edge(DOWN)

        x_labels = {
            PI/2: MathTex("\\frac{\\pi}{2}"),
            PI: MathTex("\\pi"),
            3*PI/2: MathTex("\\frac{3\\pi}{2}"),
        }

        zero_plot = axes.plot(lambda x: 0.)
        labels = VGroup()
        for x_val, label_tex in x_labels.items():
            label = axes.get_graph_label(
                graph=zero_plot,
                label=label_tex,
                x_val=x_val,
                dot=False,
                direction=UP,
            )
            labels.add(label)

        self.add(axes, zero_plot, labels)
        self.remove(zero_plot)
        

        labels = axes.get_axis_labels(
            MathTex("\\theta"), MathTex("I_z")
        )
        self.add(axes, labels)        

        self.play(Create(axes),run_time=2)

        inertia = axes.plot(lambda x: np.cos(x)*np.cos(x) + 0.5625*np.sin(x)*np.sin(x), color=WHITE)
        maxinertia = axes.plot(lambda x: 1., color=RED)
        mininertia = axes.plot(lambda x: 0.5625, color=YELLOW)

        # parabola_label = axes.get_graph_label(parabola, label="y = x^2")

        # Create text "Assume that b=1 and h=1", then fade it out
        b1h1 = Text("Assume that b = 1.5 and h = 2",font_size=32).to_edge(UP).to_edge(RIGHT)
        self.play(Write(b1h1))
        self.wait(2)


        # Transform equation to the equation with b = 1.5 and h = 2
        equation4 = MathTex("I_z = \\frac{1.5 \\cdot 2^3}{12} \\cos^2(\\theta) + \\frac{1.5^3 \\cdot 2}{12} \\sin^2(\\theta)")
        equation4.to_corner(UL)
        self.play(Transform(equation, equation4))
        self.wait(2)
        equation4 = MathTex(
            "I_z = 1\\cos^2(\\theta) + 0.5625 \\sin^2(\\theta)",
            tex_to_color_map={"1": RED, "0.5625": YELLOW}
        )

        equation4.to_corner(UL)
        self.play(Transform(equation, equation4))
        self.wait(2)

        self.play(FadeOut(b1h1))
        self.wait(2)

        # Create theta = below equation and indicate it
        # theta_0 = MathTex("\\theta = ").next_to(equation4, DOWN).to_edge(LEFT)
        # self.play(Write(theta_0))
        # self.play(Indicate(theta_0),run_time=2)
        # self.wait(2)

        # Create number zero to the right of theta = 
        # theta_zero = MathTex("0^\\circ").next_to(theta_0, RIGHT)
        # self.play(Write(theta_zero))
        # self.wait(2)

        
        # Creata number and vary its value from 0 to 360 smoothly in an animation
        # theta_tracker = ValueTracker(0)

        # theta_zero.add_updater(lambda m: m.set_value(theta_tracker.get_value()))
        # theta_zero.add_updater(lambda m: m.become(MathTex(f"{int(theta_tracker.get_value())}^\\circ").next_to(theta_0, RIGHT)))

        # self.play(theta_tracker.animate.set_value(360), run_time=10, rate_func=linear)
        # self.wait(2)

        # Plot maxinertia and mininertia
        self.play(Create(maxinertia), Create(mininertia),run_time=3)
        self.wait(2)
                
        # Create a bent counter clockwise arrow above the rectangle
        carrow = CurvedArrow(
            rectangle.get_center() + UP*2.3 + RIGHT*1.5,
            rectangle.get_center() + UP*2.3 + LEFT*1.5,
            angle=PI/6
        )
        self.play(Create(carrow),run_time=2)
        self.wait(2)

        # Create curve for plot with equation cos^2(theta) + sin^2(theta)
        self.play(
            Rotate(rectangle, angle=2*PI),
            Create(inertia)
            ,run_time=10,
            rate_func=linear
        )
        self.wait(2)   

        # Fade out the curved arrow
        self.play(FadeOut(carrow))
        self.wait(2)

        # Create 2 green points, at coordinates (PI/4, 0.5625), (3*PI/4, 0.5625)
        point = Dot(axes.c2p(PI/2, 0.5625), color=PURPLE)
        point2 = Dot(axes.c2p(3*PI/2, 0.5625), color=PURPLE)
        self.play(
            Rotate(rectangle, angle=PI/2)
        )
        self.play(
            rectangle.animate.set_color(PURPLE)
        )
        self.play(Create(point),Create(point2))
        self.play(Indicate(point), Indicate(point2))
        self.wait(2)

        # Create 3 cyan points, at coordinates (0, 1), (PI, 1) and (2*PI, 1)
        point3 = Dot(axes.c2p(0, 1), color=GREEN)
        point4 = Dot(axes.c2p(PI, 1), color=GREEN)
        point5 = Dot(axes.c2p(2*PI, 1), color=GREEN)
        self.play(
            Rotate(rectangle, angle=-PI/2),
        )            
        self.play(
            rectangle.animate.set_color(GREEN)
        )        
        self.play(Create(point3),Create(point4),Create(point5))
        self.play(Indicate(point3), Indicate(point4), Indicate(point5))
        self.wait(2)

        # Make a dot that is blue that moves along the curve inertia
        dot = Dot(axes.c2p(0, 1), color=BLUE)
        self.play(Create(dot))
        self.play(
            rectangle.animate.set_color(BLUE)
        )                    
        self.wait(2)
        self.play(
            Rotate(rectangle, angle=2*PI),
            MoveAlongPath(dot, inertia),
            run_time=10,
            rate_func=linear
        )
        self.wait(5)

        # Create a point at the coordinate (PI/4, 1)


        # # self.play(Rotate(rectangle, angle=2*PI, run_time=4, rate_func=linear))
        # # self.wait()