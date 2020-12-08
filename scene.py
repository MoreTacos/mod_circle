#!/usr/bin/env python

from manimlib.imports import *

class Updater2(Scene):
    CONFIG={
        "x": 100,
        "radius": 3.5,
        "end_value": 25,
        "total_time": 30,
        "gradient_colors": [RED,YELLOW,BLUE],
    }
    def construct(self):
        mod_tracker = ValueTracker(0)
        circle = Circle()
        circle.scale(self.radius)
        lines = self.get_obj(circle, mod_tracker.get_value())
        lines.add_updater(
            lambda m: m.become(
                self.get_obj(circle, mod_tracker.get_value())
            )
        )
        self.play(ShowCreation(circle))
        self.play(ShowCreation(lines))
        self.wait()
        self.play(
            mod_tracker.set_value, self.end_value,
            rate_func=linear,
            run_time=self.total_time
        )
        self.wait(3)

    def get_obj(self, circle, mod):
        lines = VGroup()
        for i in range(self.x):
            start = circle.point_from_proportion((i%self.x)/self.x)
            end = circle.point_from_proportion(((i*mod)%self.x)/self.x)
            line = Line(start, end).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*self.gradient_colors)
        return lines
