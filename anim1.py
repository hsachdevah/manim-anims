from manim import *

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
                line1.get_end() + UP*1.33, 
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
        path.set_color(RED)
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        dot.add_updater(update_path)
        
        self.add(numberplane, line1, line2, dot, path)
        # self.play(dot.animate.shift(UP)) #animate dot
        self.play(theta1_tracker.animate.set_value(370),rate_func=rate_functions.linear,run_time=20) #animate line