from manim import *

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)

class MovingAngle(Scene):
    def construct(self):
        rotation_center = RIGHT

        theta_tracker = ValueTracker(10)
        line1 = Line(LEFT, RIGHT)
        dot1 = Dot(point=line1.get_end())
        line_moving = Line(LEFT, RIGHT).set_color(RED)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point= line1.get_end()
        )
        dot2 = Dot(point=line_moving.get_start())
        # a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        # tex = MathTex(r"\theta").move_to(
        #     Angle(
        #         line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
        #     ).point_from_proportion(0.5)
        # )

        self.add(dot1, line1, line_moving)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=line1.get_end()
            )
        )

        dot2.add_updater(
            lambda x: x.set_x(line_moving.get_x())
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        # self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))



class anim1(Scene):
    def construct(self):
        path = VMobject()
        line1 = Line(ORIGIN, RIGHT*2).set_color(ORANGE)
        line1_ref = line1.copy()
        
        numberplane = NumberPlane()
        

        # Create Line, Rotate it at origin
        theta1_tracker = ValueTracker(0)
        theta2_tracker = ValueTracker(0)
    
        # line1.rotate(
        #     theta1_tracker.get_value() * DEGREES, about_point= line1.get_start()
        # )

        line1.add_updater(
            lambda x: x.become(line1_ref.copy()).rotate(
                theta1_tracker.get_value() * DEGREES, about_point=line1.get_start()
            )
        )

        # Draw line2
        line2 = always_redraw(
            lambda: Line(
                line1.get_end(), 
                line1.get_end() + UP, 
                color=BLUE
            )
        )

        line2.add_updater(
            lambda x: x.become(line2.copy()).rotate(
                theta1_tracker.get_value() * 20 * DEGREES, about_point=line1.get_end()
            )
        )

        # Draw dot
        # dot = Dot(point=line1.get_end())
        dot = always_redraw(
                lambda: Dot(point=line2.get_end())
            )
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        dot.add_updater(update_path)
        
        self.add(path, line1,line2,dot)
        # self.play(dot.animate.shift(UP)) #animate dot
        self.play(theta1_tracker.animate.set_value(1340),rate_func=rate_functions.linear,run_time=60) #animate line