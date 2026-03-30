import sys
import turtle

class CavePlugin:
    def __init__(self):
        self._methods = {}

    def method(self, name):
        def decorator(func):
            self._methods[name] = func
            return func
        return decorator

    def run(self):
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            
            line = line.strip() 
            if not line:
                continue

            if line.startswith("CALL"):
                parts = line.split(" ")
                if len(parts) >= 2:
                    method_name = parts[1]
                    args = parts[2:]
                    if method_name in self._methods:
                        try:
                            clean_args = [int(a) for a in args]
                            self._methods[method_name](*clean_args)
                            sys.stdout.flush()
                        except Exception as e:
                            pass

plugin = CavePlugin()

@plugin.method("forward")
def move_forward(*args):
    val = args[0] if args else 0
    turtle.forward(val)

@plugin.method("backward")
def move_backward(*args):
    val = args[0] if args else 0
    turtle.back(val)

@plugin.method("winh")
def screen_window_height(*args):
    val = args[0] if args else 0
    turtle.window_height(val)

@plugin.method("winw")
def screen_window_width(*args):
    val = args[0] if args else 0
    turtle.window_width(val)

@plugin.method("clear")
def screen_clear(*args):
    val = args[0] if args else 0
    turtle.clear()

@plugin.method("colorstr")
def change_color_str(*args):
    val = args[0] if args else 0
    turtle.color(str(val))

@plugin.method("colorrgb")
def change_color_rgb(*args):
    r = args[0] if len(args) > 0 else 0
    g = args[1] if len(args) > 1 else 0
    b = args[2] if len(args) > 2 else 0
    turtle.color(r, g, b)

@plugin.method("pos")
def return_pos(*args):
    x = args[0] if len(args) > 0 else 0
    y = args[1] if len(args) > 1 else 0
    turtle.pos(x, y)

@plugin.method("speed")
def change_speed(*args):
    val = args[0] if len(args) > 0 else 5
    turtle.speed(val)

@plugin.method("right")
def move_right(*args):
    val = args[0] if len(args) > 0 else 0
    turtle.right(val)

@plugin.method("left")
def move_left(*args):
    val = args[0] if len(args) > 0 else 0
    turtle.left(val)

@plugin.method("main")
def main_main(*args):
    val = args[0] if len(args) > 0 else 0
    turtle.mainloop()

@plugin.method("goto")
def move_goto(*args):
    x = args[0] if len(args) > 0 else 0
    y = args[0] if len(args) > 1 else 0
    turtle.goto()

@plugin.method("show")
def main_show(*args):
    x = args[0] if len(args) > 0 else 0
    y = args[0] if len(args) > 1 else 0
    turtle.showturtle()

@plugin.method("tp")
def main_teleport(*args):
    x = args[0] if len(args) > 0 else 0
    y = args[0] if len(args) > 1 else 0
    turtle.teleport(float(x), float(y))

@plugin.method("setpos")
def main_position_set(*args):
    x = args[0] if len(args) > 0 else 0
    y = args[0] if len(args) > 1 else 0
    turtle.setposition(float(x), float(y))

@plugin.method("dir")
def main_head_set(*args):
    dir = args[0] if len(args) > 0 else 0
    turtle.setheading(dir)

@plugin.method("pup")
def main_pen_up(*args):
    val = args[0] if len(args) > 0 else 0
    turtle.penup()

@plugin.method("pdown")
def main_pen_down(*args):
    val = args[0] if len(args) > 0 else 0
    turtle.pendown()

@plugin.method("setx")
def main_position_x_set(*args):
    x = args[0] if len(args) > 0 else 0
    turtle.setx(x)

@plugin.method("sety")
def main_position_y_set(*args):
    y = args[0] if len(args) > 0 else 0
    turtle.sety(y)

@plugin.method("psize")
def main_pen_size(*args):
    size = args[0] if len(args) > 0 else 0
    turtle.pensize(size)

@plugin.method("title")
def main_screen_title(*args):
    title = args[0] if len(args) > 0 else 0
    turtle.title(str(title))

@plugin.method("bye")
def main_endtype_bye(*args):
    turtle.bye()

@plugin.method("done")
def main_endtype_done(*args):
    turtle.done()

if __name__ == "__main__":
    plugin.run()