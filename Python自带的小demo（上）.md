[点击这里去《Python自带的小demo（下）》！](https://blog.csdn.net/PanDaoxi2020/article/details/119147032)
<hr>

①绘制一朵花：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/51240873b83b7b0a9e0a2211efca155f.png)

```python
#!/usr/bin/env python3
"""      turtle-example-suite:

        tdemo_bytedesign.py

An example adapted from the example-suite
of PythonCard's turtle graphics.

It's based on an article in BYTE magazine
Problem Solving with Logo: Using Turtle
Graphics to Redraw a Design
November 1982, p. 118 - 134

-------------------------------------------

Due to the statement

t.delay(0)

in line 152, which sets the animation delay
to 0, this animation runs in "line per line"
mode as fast as possible.
"""

from turtle import Turtle, mainloop
from time import clock

# wrapper for any additional drawing routines
# that need to know about each other
class Designer(Turtle):

    def design(self, homePos, scale):
        self.up()
        for i in range(5):
            self.forward(64.65 * scale)
            self.down()
            self.wheel(self.position(), scale)
            self.up()
            self.backward(64.65 * scale)
            self.right(72)
        self.up()
        self.goto(homePos)
        self.right(36)
        self.forward(24.5 * scale)
        self.right(198)
        self.down()
        self.centerpiece(46 * scale, 143.4, scale)
        self.getscreen().tracer(True)

    def wheel(self, initpos, scale):
        self.right(54)
        for i in range(4):
            self.pentpiece(initpos, scale)
        self.down()
        self.left(36)
        for i in range(5):
            self.tripiece(initpos, scale)
        self.left(36)
        for i in range(5):
            self.down()
            self.right(72)
            self.forward(28 * scale)
            self.up()
            self.backward(28 * scale)
        self.left(54)
        self.getscreen().update()

    def tripiece(self, initpos, scale):
        oldh = self.heading()
        self.down()
        self.backward(2.5 * scale)
        self.tripolyr(31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.down()
        self.backward(2.5 * scale)
        self.tripolyl(31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)
        self.getscreen().update()

    def pentpiece(self, initpos, scale):
        oldh = self.heading()
        self.up()
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pentr(18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pentl(18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)
        self.getscreen().update()

    def pentl(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.left(ang)
        self.pentl(side - (.38 * scale), ang, scale)

    def pentr(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.right(ang)
        self.pentr(side - (.38 * scale), ang, scale)

    def tripolyr(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.right(111)
        self.forward(side / 1.78)
        self.right(111)
        self.forward(side / 1.3)
        self.right(146)
        self.tripolyr(side * .75, scale)

    def tripolyl(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.left(111)
        self.forward(side / 1.78)
        self.left(111)
        self.forward(side / 1.3)
        self.left(146)
        self.tripolyl(side * .75, scale)

    def centerpiece(self, s, a, scale):
        self.forward(s); self.left(a)
        if s < (7.5 * scale):
            return
        self.centerpiece(s - (1.2 * scale), a, scale)

def main():
    t = Designer()
    t.speed(0)
    t.hideturtle()
    t.getscreen().delay(0)
    t.getscreen().tracer(0)
    at = clock()
    t.design(t.position(), 2)
    et = clock()
    return "runtime: %.2f sec." % (et-at)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

```

②绘制折线图：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/1e64cf3a0ce24697bfbe7a4a09770ea7.png)

```python
# File: tdemo_chaos.py
# Author: Gregor Lingl
# Date: 2009-06-24

# A demonstration of chaos

from turtle import *

N = 80

def f(x):
    return 3.9*x*(1-x)

def g(x):
    return 3.9*(x-x**2)

def h(x):
    return 3.9*x-3.9*x*x

def jumpto(x, y):
    penup(); goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)

def plot(fun, start, color):
    pencolor(color)
    x = start
    jumpto(0, x)
    pendown()
    dot(5)
    for i in range(N):
        x=fun(x)
        goto(i+1,x)
        dot(5)

def main():
    reset()
    setworldcoordinates(-1.0,-0.1, N+1, 1.1)
    speed(0)
    hideturtle()
    coosys()
    plot(f, 0.35, "blue")
    plot(g, 0.35, "green")
    plot(h, 0.35, "red")
    # Now zoom in:
    for s in range(100):
        setworldcoordinates(0.5*s,-0.1, N+1, 1.1)
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

```
③时钟：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/bde39d491a20a7211e25f72142f84cc6.png)

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""       turtle-example-suite:

             tdemo_clock.py

Enhanced clock-program, showing date
and time
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray20", "gray80")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "red1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "red3")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)

def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(wochentag(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        tracer(True)
        second_hand.setheading(6*sekunde)  # or here
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*stunde)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()

```
④颜色搭配：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/0f91461c3a9f722dd66dffb7c398feec.png)


```python
# colormixer

from turtle import Screen, Turtle, mainloop

class ColorTurtle(Turtle):

    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("turtle")
        self.resizemode("user")
        self.shapesize(3,3,5)
        self.pensize(10)
        self._color = [0,0,0]
        self.x = x
        self._color[x] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x,0)
        self.pd()
        self.sety(1)
        self.pu()
        self.sety(y)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0,min(y,1)))
        self._color[self.x] = self.ycor()
        self.fillcolor(self._color)
        setbgcolor()

def setbgcolor():
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())

def main():
    global screen, red, green, blue
    screen = Screen()
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)

    red = ColorTurtle(0, .5)
    green = ColorTurtle(1, .5)
    blue = ColorTurtle(2, .5)
    setbgcolor()

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1,1.15)
    writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

```
⑤绘制一片森林：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/270b794026beb0802c9ce70c58e3340d.png)

```python
#!/usr/bin/env python3
"""     turtlegraphics-example-suite:

             tdemo_forest.py

Displays a 'forest' of 3 breadth-first-trees
similar to the one in tree.
For further remarks see tree.py

This example is a 'breadth-first'-rewrite of
a Logo program written by Erich Neuwirth. See
http://homepage.univie.ac.at/erich.neuwirth/
"""
from turtle import Turtle, colormode, tracer, mainloop
from random import randrange
from time import clock

def symRandom(n):
    return randrange(-n,n+1)

def randomize( branchlist, angledist, sizedist ):
    return [ (angle+symRandom(angledist),
              sizefactor*1.01**symRandom(sizedist))
                     for angle, sizefactor in branchlist ]

def randomfd( t, distance, parts, angledist ):
    for i in range(parts):
        t.left(symRandom(angledist))
        t.forward( (1.0 * distance)/parts )

def tree(tlist, size, level, widthfactor, branchlists, angledist=10, sizedist=5):
    # benutzt Liste von turtles und Liste von Zweiglisten,
    # fuer jede turtle eine!
    if level > 0:
        lst = []
        brs = []
        for t, branchlist in list(zip(tlist,branchlists)):
            t.pensize( size * widthfactor )
            t.pencolor( 255 - (180 - 11 * level + symRandom(15)),
                        180 - 11 * level + symRandom(15),
                        0 )
            t.pendown()
            randomfd(t, size, level, angledist )
            yield 1
            for angle, sizefactor in branchlist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(branchlist, angledist, sizedist))
                t.right(angle)
        for x in tree(lst, size*sizefactor, level-1, widthfactor, brs,
                      angledist, sizedist):
            yield None


def start(t,x,y):
    colormode(255)
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x,y)
    t.pendown()

def doit1(level, pen):
    pen.hideturtle()
    start(pen, 20, -208)
    t = tree( [pen], 80, level, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -130)
    t = tree( [pen], 120, level, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree( [pen], 100, level, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

# Hier 3 Baumgeneratoren:
def main():
    p = Turtle()
    p.ht()
    tracer(75,0)
    u = doit1(6, Turtle(undobuffersize=1))
    s = doit2(7, Turtle(undobuffersize=1))
    t = doit3(5, Turtle(undobuffersize=1))
    a = clock()
    while True:
        done = 0
        for b in u,s,t:
            try:
                b.__next__()
            except:
                done += 1
        if done == 3:
            break

    tracer(1,10)
    b = clock()
    return "runtime: %.2f sec." % (b-a)

if __name__ == '__main__':
    main()
    mainloop()

```
⑥绘制两个图形：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/cc58358ea88b43300f144b0f9a1dd8d1.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/d3bbe8a077af04ab487b883d6eaf718c.png)

```python
#!/usr/bin/env python3
"""      turtle-example-suite:

        tdemo_fractalCurves.py

This program draws two fractal-curve-designs:
(1) A hilbert curve (in a box)
(2) A combination of Koch-curves.

The CurvesTurtle class and the fractal-curve-
methods are taken from the PythonCard example
scripts for turtle-graphics.
"""
from turtle import *
from time import sleep, clock

class CurvesTurtle(Pen):
    # example derived from
    # Turtle Geometry: The Computer as a Medium for Exploring Mathematics
    # by Harold Abelson and Andrea diSessa
    # p. 96-98
    def hilbert(self, size, level, parity):
        if level == 0:
            return
        # rotate and draw first subcurve with opposite parity to big curve
        self.left(parity * 90)
        self.hilbert(size, level - 1, -parity)
        # interface to and draw second subcurve with same parity as big curve
        self.forward(size)
        self.right(parity * 90)
        self.hilbert(size, level - 1, parity)
        # third subcurve
        self.forward(size)
        self.hilbert(size, level - 1, parity)
        # fourth subcurve
        self.right(parity * 90)
        self.forward(size)
        self.hilbert(size, level - 1, -parity)
        # a final turn is needed to make the turtle
        # end up facing outward from the large square
        self.left(parity * 90)

    # Visual Modeling with Logo: A Structural Approach to Seeing
    # by James Clayson
    # Koch curve, after Helge von Koch who introduced this geometric figure in 1904
    # p. 146
    def fractalgon(self, n, rad, lev, dir):
        import math

        # if dir = 1 turn outward
        # if dir = -1 turn inward
        edge = 2 * rad * math.sin(math.pi / n)
        self.pu()
        self.fd(rad)
        self.pd()
        self.rt(180 - (90 * (n - 2) / n))
        for i in range(n):
            self.fractal(edge, lev, dir)
            self.rt(360 / n)
        self.lt(180 - (90 * (n - 2) / n))
        self.pu()
        self.bk(rad)
        self.pd()

    # p. 146
    def fractal(self, dist, depth, dir):
        if depth < 1:
            self.fd(dist)
            return
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.rt(120 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)

def main():
    ft = CurvesTurtle()

    ft.reset()
    ft.speed(0)
    ft.ht()
    ft.getscreen().tracer(1,0)
    ft.pu()

    size = 6
    ft.setpos(-33*size, -32*size)
    ft.pd()

    ta=clock()
    ft.fillcolor("red")
    ft.begin_fill()
    ft.fd(size)

    ft.hilbert(size, 6, 1)

    # frame
    ft.fd(size)
    for i in range(3):
        ft.lt(90)
        ft.fd(size*(64+i%2))
    ft.pu()
    for i in range(2):
        ft.fd(size)
        ft.rt(90)
    ft.pd()
    for i in range(4):
        ft.fd(size*(66+i%2))
        ft.rt(90)
    ft.end_fill()
    tb=clock()
    res =  "Hilbert: %.2fsec. " % (tb-ta)

    sleep(3)

    ft.reset()
    ft.speed(0)
    ft.ht()
    ft.getscreen().tracer(1,0)

    ta=clock()
    ft.color("black", "blue")
    ft.begin_fill()
    ft.fractalgon(3, 250, 4, 1)
    ft.end_fill()
    ft.begin_fill()
    ft.color("red")
    ft.fractalgon(3, 200, 4, -1)
    ft.end_fill()
    tb=clock()
    res +=  "Koch: %.2fsec." % (tb-ta)
    return res

if __name__  == '__main__':
    msg = main()
    print(msg)
    mainloop()

```
⑦绘制两个以美丽的线条组成的矩形：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/bc90f0e2bb105b29b90faf1a0c353789.png)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/8a2225490773f4b168f8b52804173756.png)

```python
#!/usr/bin/env python3
"""       turtle-example-suite:

        xtx_lindenmayer_indian.py

Each morning women in Tamil Nadu, in southern
India, place designs, created by using rice
flour and known as kolam on the thresholds of
their homes.

These can be described by Lindenmayer systems,
which can easily be implemented with turtle
graphics and Python.

Two examples are shown here:
(1) the snake kolam
(2) anklets of Krishna

Taken from Marcia Ascher: Mathematics
Elsewhere, An Exploration of Ideas Across
Cultures

"""
################################
# Mini Lindenmayer tool
###############################

from turtle import *

def replace( seq, replacementRules, n ):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq = newseq + replacementRules.get(element,element)
        seq = newseq
    return seq

def draw( commands, rules ):
    for b in commands:
        try:
            rules[b]()
        except TypeError:
            try:
                draw(rules[b], rules)
            except:
                pass


def main():
    ################################
    # Example 1: Snake kolam
    ################################


    def r():
        right(45)

    def l():
        left(45)

    def f():
        forward(7.5)

    snake_rules = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    snake_replacementRules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_replacementRules, 3)

    reset()
    speed(3)
    tracer(1,0)
    ht()
    up()
    backward(195)
    down()
    draw(drawing, snake_rules)

    from time import sleep
    sleep(3)

    ################################
    # Example 2: Anklets of Krishna
    ################################

    def A():
        color("red")
        circle(10,90)

    def B():
        from math import sqrt
        color("black")
        l = 5/sqrt(2)
        forward(l)
        circle(l, 270)
        forward(l)

    def F():
        color("green")
        forward(10)

    krishna_rules = {"a":A, "b":B, "f":F}
    krishna_replacementRules = {"a" : "afbfa", "b" : "afbfbfbfa" }
    krishna_start = "fbfbfbfb"

    reset()
    speed(0)
    tracer(3,0)
    ht()
    left(45)
    drawing = replace(krishna_start, krishna_replacementRules, 3)
    draw(drawing, krishna_rules)
    tracer(1)
    return "Done!"

if __name__=='__main__':
    msg = main()
    print(msg)
    mainloop()

```
⑧汉诺塔小游戏：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/c1b568d9de9886299188da3fc1de7944.png)

```python
#!/usr/bin/env python3
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    try:
        hanoi(6, t1, t2, t3)
        write("press STOP button to exit",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()

```
⑧矩形小游戏：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/239cac303acebcea6db04af7b1c8f30e.png)

```python
"""      turtle-example-suite:

            tdemo_nim.py

Play nim against the computer. The player
who takes the last stick is the winner.

Implements the model-view-controller
design pattern.
"""


import turtle
import random
import time

SCREENWIDTH = 640
SCREENHEIGHT = 480

MINSTICKS = 7
MAXSTICKS = 31

HUNIT = SCREENHEIGHT // 12
WUNIT = SCREENWIDTH // ((MAXSTICKS // 5) * 11 + (MAXSTICKS % 5) * 2)

SCOLOR = (63, 63, 31)
HCOLOR = (255, 204, 204)
COLOR = (204, 204, 255)

def randomrow():
    return random.randint(MINSTICKS, MAXSTICKS)

def computerzug(state):
    xored = state[0] ^ state[1] ^ state[2]
    if xored == 0:
        return randommove(state)
    for z in range(3):
        s = state[z] ^ xored
        if s <= state[z]:
            move = (z, s)
            return move

def randommove(state):
    m = max(state)
    while True:
        z = random.randint(0,2)
        if state[z] > (m > 1):
            break
    rand = random.randint(m > 1, state[z]-1)
    return z, rand


class NimModel(object):
    def __init__(self, game):
        self.game = game

    def setup(self):
        if self.game.state not in [Nim.CREATED, Nim.OVER]:
            return
        self.sticks = [randomrow(), randomrow(), randomrow()]
        self.player = 0
        self.winner = None
        self.game.view.setup()
        self.game.state = Nim.RUNNING

    def move(self, row, col):
        maxspalte = self.sticks[row]
        self.sticks[row] = col
        self.game.view.notify_move(row, col, maxspalte, self.player)
        if self.game_over():
            self.game.state = Nim.OVER
            self.winner = self.player
            self.game.view.notify_over()
        elif self.player == 0:
            self.player = 1
            row, col = computerzug(self.sticks)
            self.move(row, col)
            self.player = 0

    def game_over(self):
        return self.sticks == [0, 0, 0]

    def notify_move(self, row, col):
        if self.sticks[row] <= col:
            return
        self.move(row, col)


class Stick(turtle.Turtle):
    def __init__(self, row, col, game):
        turtle.Turtle.__init__(self, visible=False)
        self.row = row
        self.col = col
        self.game = game
        x, y = self.coords(row, col)
        self.shape("square")
        self.shapesize(HUNIT/10.0, WUNIT/20.0)
        self.speed(0)
        self.pu()
        self.goto(x,y)
        self.color("white")
        self.showturtle()

    def coords(self, row, col):
        packet, remainder = divmod(col, 5)
        x = (3 + 11 * packet + 2 * remainder) * WUNIT
        y = (2 + 3 * row) * HUNIT
        return x - SCREENWIDTH // 2 + WUNIT // 2, SCREENHEIGHT // 2 - y - HUNIT // 2

    def makemove(self, x, y):
        if self.game.state != Nim.RUNNING:
            return
        self.game.controller.notify_move(self.row, self.col)


class NimView(object):
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.model = game.model
        self.screen.colormode(255)
        self.screen.tracer(False)
        self.screen.bgcolor((240, 240, 255))
        self.writer = turtle.Turtle(visible=False)
        self.writer.pu()
        self.writer.speed(0)
        self.sticks = {}
        for row in range(3):
            for col in range(MAXSTICKS):
                self.sticks[(row, col)] = Stick(row, col, game)
        self.display("... a moment please ...")
        self.screen.tracer(True)

    def display(self, msg1, msg2=None):
        self.screen.tracer(False)
        self.writer.clear()
        if msg2 is not None:
            self.writer.goto(0, - SCREENHEIGHT // 2 + 48)
            self.writer.pencolor("red")
            self.writer.write(msg2, align="center", font=("Courier",18,"bold"))
        self.writer.goto(0, - SCREENHEIGHT // 2 + 20)
        self.writer.pencolor("black")
        self.writer.write(msg1, align="center", font=("Courier",14,"bold"))
        self.screen.tracer(True)

    def setup(self):
        self.screen.tracer(False)
        for row in range(3):
            for col in range(self.model.sticks[row]):
                self.sticks[(row, col)].color(SCOLOR)
        for row in range(3):
            for col in range(self.model.sticks[row], MAXSTICKS):
                self.sticks[(row, col)].color("white")
        self.display("Your turn! Click leftmost stick to remove.")
        self.screen.tracer(True)

    def notify_move(self, row, col, maxspalte, player):
        if player == 0:
            farbe = HCOLOR
            for s in range(col, maxspalte):
                self.sticks[(row, s)].color(farbe)
        else:
            self.display(" ... thinking ...         ")
            time.sleep(0.5)
            self.display(" ... thinking ... aaah ...")
            farbe = COLOR
            for s in range(maxspalte-1, col-1, -1):
                time.sleep(0.2)
                self.sticks[(row, s)].color(farbe)
            self.display("Your turn! Click leftmost stick to remove.")

    def notify_over(self):
        if self.game.model.winner == 0:
            msg2 = "Congrats. You're the winner!!!"
        else:
            msg2 = "Sorry, the computer is the winner."
        self.display("To play again press space bar. To leave press ESC.", msg2)

    def clear(self):
        if self.game.state == Nim.OVER:
            self.screen.clear()


class NimController(object):

    def __init__(self, game):
        self.game = game
        self.sticks = game.view.sticks
        self.BUSY = False
        for stick in self.sticks.values():
            stick.onclick(stick.makemove)
        self.game.screen.onkey(self.game.model.setup, "space")
        self.game.screen.onkey(self.game.view.clear, "Escape")
        self.game.view.display("Press space bar to start game")
        self.game.screen.listen()

    def notify_move(self, row, col):
        if self.BUSY:
            return
        self.BUSY = True
        self.game.model.notify_move(row, col)
        self.BUSY = False


class Nim(object):
    CREATED = 0
    RUNNING = 1
    OVER = 2
    def __init__(self, screen):
        self.state = Nim.CREATED
        self.screen = screen
        self.model = NimModel(self)
        self.view = NimView(self)
        self.controller = NimController(self)


def main():
    mainscreen = turtle.Screen()
    mainscreen.mode("standard")
    mainscreen.setup(SCREENWIDTH, SCREENHEIGHT)
    nim = Nim(mainscreen)
    return "EVENTLOOP"

if __name__ == "__main__":
    main()
    turtle.mainloop()

```
⑨跟着鼠标走的小红点：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/35a1994302c2c7ac7b07f49ee5e588b6.png)

```python
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_paint.py

A simple  event-driven paint program

- left mouse button moves turtle
- middle mouse button changes color
- right mouse button toogles betweem pen up
(no line drawn when the turtle moves) and
pen down (line is drawn). If pen up follows
at least two pen-down moves, the polygon that
includes the starting point is filled.
 -------------------------------------------
 Play around by clicking into the canvas
 using all three mouse buttons.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle import *

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

def main():
    global colors
    shape("circle")
    resizemode("user")
    shapesize(.5)
    width(3)
    colors=["red", "green", "blue", "yellow"]
    color(colors[0])
    switchupdown()
    onscreenclick(goto,1)
    onscreenclick(changecolor,2)
    onscreenclick(switchupdown,3)
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

```

