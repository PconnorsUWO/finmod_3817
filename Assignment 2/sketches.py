from manim import *
import numpy as np

# ---------------------------
# System (a)
# ---------------------------
class SystemAScene(Scene):
    def construct(self):
        # Create axes with a suitable range.
        axes = Axes(
            x_range=[-6, 2, 1],
            y_range=[-15, 5, 1],
            x_length=7,
            y_length=7,
            tips=False,
        )
        # Add basic axis labels ("x" and "y").
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Define functions for the lines:
        # Line 1: x + 2y = 1  ->  y = (1 - x)/2
        line1 = axes.plot(lambda x: (1 - x) / 2, x_range=[-5, 1], color=BLUE)
        line1_label = axes.get_graph_label(line1, label="x+2y=1", x_val=0.5, direction=UP)
        
        # Line 2: y - 2x = -2 ->  y = 2x - 2
        line2 = axes.plot(lambda x: 2 * x - 2, x_range=[-5, 1], color=GREEN)
        line2_label = axes.get_graph_label(line2, label="y=2x-2", x_val=-4, direction=RIGHT)
        
        # Vertical line: x + 5 >= 0  ->  x = -5 (drawn from y=-12 to y=3)
        p_low = axes.c2p(-5, -12)
        p_high = axes.c2p(-5, 3)
        vert_line = Line(p_low, p_high, color=RED)
        vert_line_label = Tex("x=-5", font_size=24).next_to(vert_line, LEFT)

        # Draw boundary lines.
        self.play(Create(line1), Write(line1_label))
        self.play(Create(line2), Write(line2_label))
        self.play(Create(vert_line), Write(vert_line_label))
        self.wait(0.5)

        # Shade the feasible region: triangle with vertices (1,0), (-5,3), (-5,-12)
        A = axes.c2p(1, 0)
        B = axes.c2p(-5, 3)
        C = axes.c2p(-5, -12)
        region = Polygon(A, B, C, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        self.play(Create(region))
        self.wait(2)
# ---------------------------
# System (b)
# ---------------------------
class SystemBScene(Scene):
    def construct(self):
        # For (b) we use a restricted view since the set is unbounded.
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=6,
            tips=False,
        )
        # Use get_axis_labels instead of add_coordinate_labels
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Line: y = x (from inequality x - y <= 0)
        line_y_eq_x = axes.plot(lambda x: x, x_range=[0, 4], color=BLUE)
        line_y_eq_x_label = axes.get_graph_label(line_y_eq_x, label="y=x", x_val=3.5, direction=UP)
        self.play(Create(line_y_eq_x), Write(line_y_eq_x_label))
        self.wait(0.5)

        # The effective constraints are x >= 0 and y >= x.
        # For display, we approximate the unbounded region by filling the rectangle in our view that lies above y=x.
        poly = Polygon(
            axes.c2p(0, 0),    # Intersection of x=0 and y=x.
            axes.c2p(4, 4),    # Intersection of y=x with right boundary.
            axes.c2p(4, 5),    # Top-right corner of the axes.
            axes.c2p(0, 5),    # Top-left corner (x=0)
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.5
        )
        self.play(Create(poly))
        self.wait(2)

# ---------------------------
# System (c) – Bonus
# ---------------------------

class C(Scene):
    def construct(self):
        # Create a grid using NumberPlane
        grid = NumberPlane(
            x_range=[-2, 3, 1],
            y_range=[-2, 3, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        self.add(grid)
        
        # Create the unit circle
        circle = Circle(radius=1, color=WHITE)
        
        # Create the line x+y = 1.
        line = Line(start=np.array([-2, 3, 0]), end=np.array([3, -2, 0]), color=GREEN)
        
        # Create the arc of the circle from (1,0) to (0,1)
        arc = Arc(radius=1, start_angle=0, angle=PI/2, color=YELLOW)
        
        # Create the chord joining (0,1) and (1,0)
        chord = Line(start=np.array([0, 1, 0]), end=np.array([1, 0, 0]), color=YELLOW)
        
        # Construct the filled cap region
        arc_points = arc.get_points()
        chord_points = chord.get_points()
        cap_points = np.vstack((arc_points, chord_points))
        cap = Polygon(*cap_points, color=BLUE, fill_opacity=0.5, stroke_width=2)
        
        # Mark the extreme points (the chord endpoints)
        dot_A = Dot(point=np.array([0, 1, 0]), color=RED)
        label_A = MathTex("(0,1)").next_to(dot_A, UP)
        dot_B = Dot(point=np.array([1, 0, 0]), color=RED)
        label_B = MathTex("(1,0)").next_to(dot_B, RIGHT)
        
        # Animate the elements
        self.play(Create(circle))
        self.play(Create(line))
        self.play(Create(arc), Create(chord))
        self.play(FadeIn(cap))
        self.play(FadeIn(dot_A), FadeIn(dot_B), Write(label_A), Write(label_B))
        self.wait(2)